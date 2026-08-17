from flask import Flask, render_template, request, session
from datos import lista_cantantes
import requests
import random
from validacion import validacion
from dotenv import load_dotenv
import os
from urllib.parse import quote

SEPARADORES = [" (feat.", " (ft.", " feat.", " ft.", "(hosted by"]


app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    session["total"] = 0
    session["aciertos"] = 0
    return render_template("index.html", cantantes=lista_cantantes)


@app.route(
    "/cargar", methods=["POST"]
)  # dejamos claro que esto es solo para mandar información
def jugar():
    cantante_seleccionado = str(request.form.get("cantante_elegido"))

    if cantante_seleccionado not in lista_cantantes:
        return render_template(
            "index.html",
            cantantes=lista_cantantes,
            mensaje="Selección de cantante no válida.",
        )

    session["seleccionado"] = cantante_seleccionado

    # fix para cantantes que dan fallos con la búsqueda del id
    if cantante_seleccionado == "Raul Clyde":
        id = 102152692
    elif cantante_seleccionado == "ladiferencia2006":
        id = 302009581
    elif cantante_seleccionado == "JHAYCO":
        id = 105047672
    elif cantante_seleccionado == "Lucho RK":
        id = 151322852
    elif cantante_seleccionado == "La Pantera":
        id = 7524936
    elif cantante_seleccionado == "Soge Culebra":
        id = 9305278
    else:
        artist_search_terms = {cantante: cantante for cantante in lista_cantantes}
        search_term = artist_search_terms.get(cantante_seleccionado)

        if search_term is None:
            return render_template(
                "index.html",
                cantantes=lista_cantantes,
                mensaje="Selección de cantante no válida.",
            )

        cantante_seleccionado_safe = quote(search_term).replace("%20", "-")

        r_id = requests.get(
            f"https://api.deezer.com/artist/{cantante_seleccionado_safe}",
            timeout=10,
        )

        diccionario_id = r_id.json()

        if "error" in diccionario_id or "id" not in diccionario_id:
            return render_template(
                "index.html",
                cantantes=lista_cantantes,
                mensaje="No se pudo encontrar el artista seleccionado.",
            )

        id = diccionario_id["id"]

    safe_artist_id = str(id)
    if not safe_artist_id.isdigit():
        return render_template(
            "index.html",
            cantantes=lista_cantantes,
            mensaje="ID de artista inválido.",
        )

    # hacemos una primera petición para saber cuantas canciones tiene el artista
    temp = requests.get(
        f"https://api.deezer.com/artist/{safe_artist_id}/top?limit=1", timeout=10
    )
    diccionario_temp = temp.json()
    total = diccionario_temp["total"]

    if total == 0:
        return render_template(
            "index.html",
            cantantes=lista_cantantes,
            mensaje="Este artista no tiene canciones disponibles.",
        )

    index = random.randint(0, total - 1)
    r = requests.get(
        f"https://api.deezer.com/artist/{safe_artist_id}/top?limit=1&index={index}",
        timeout=10,
    )
    diccionario = r.json()
    nombre = diccionario["data"][0]["title"]
    for separador in SEPARADORES:
        if separador in nombre.lower():
            indice = nombre.lower().find(separador)
            nombre = nombre[:indice]
            break
    audio = diccionario["data"][0]["preview"]
    session["cancion_correcta"] = nombre
    session["audio"] = audio

    return render_template(
        "index.html",
        cantantes=lista_cantantes,
        preview=audio,
        seleccion=cantante_seleccionado,
    )


@app.route(
    "/comprobar", methods=["POST"]
)  # dejamos claro que esto es solo para mandar información
def validar():
    if "cancion_correcta" not in session:
        return render_template(
            "index.html",
            cantantes=lista_cantantes,
            mensaje="Primero selecciona un cantante.",
        )
    session["total"] += 1
    respuesta_correcta = session["cancion_correcta"]
    audio = session["audio"]
    cantante_seleccionado = session["seleccionado"]

    respuesta_usuario = str(request.form.get("respuesta"))
    if validacion(respuesta_correcta, respuesta_usuario):
        session["aciertos"] += 1
        return render_template(
            "index.html",
            cantantes=lista_cantantes,
            preview=audio,
            mensaje="¡Acertaste!",
            seleccion=cantante_seleccionado,
            porcentaje=round((session["aciertos"] / session["total"]) * 100, 2),
        )
    else:
        return render_template(
            "index.html",
            cantantes=lista_cantantes,
            preview=audio,
            mensaje=f"¡Fallaste! La canción era {respuesta_correcta}",
            seleccion=cantante_seleccionado,
            porcentaje=round((session["aciertos"] / session["total"]) * 100, 2),
        )


if __name__ == "__main__":
    app.run(debug=False)
