from flask import Flask, render_template, request, session
from datos import lista_cantantes
import requests
import random
from validacion import validacion
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

app.secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def home():
    return render_template("index.html", cantantes=lista_cantantes)


@app.route(
    "/cargar", methods=["POST"]
)  # dejamos claro que esto es solo para mandar información
def jugar():
    cantante_seleccionado = str(request.form.get("cantante_elegido"))
    cantante_seleccionado = cantante_seleccionado.replace(" ", "-")
    r_id = requests.get(f"https://api.deezer.com/artist/{cantante_seleccionado}")
    diccionario_id = r_id.json()
    id = diccionario_id["id"]

    # hacemos una primera petición para saber cuantas canciones tiene el artista
    temp = requests.get(f"https://api.deezer.com/artist/{id}/top?limit=1")
    diccionario_temp = temp.json()
    total = diccionario_temp["total"]

    index = random.randint(0, total - 1)
    r = requests.get(f"https://api.deezer.com/artist/{id}/top?limit=1&index={index}")
    diccionario = r.json()
    nombre = diccionario["data"][0]["title"]
    audio = diccionario["data"][0]["preview"]
    session["cancion_correcta"] = nombre
    session["audio"] = audio

    return render_template("index.html", cantantes=lista_cantantes, preview=audio)


@app.route(
    "/comprobar", methods=["POST"]
)  # dejamos claro que esto es solo para mandar información
def validar():
    respuesta_correcta = session["cancion_correcta"]
    audio = session["audio"]
    respuesta_usuario = str(request.form.get("respuesta"))
    if validacion(respuesta_correcta, respuesta_usuario):
        return render_template(
            "index.html",
            cantantes=lista_cantantes,
            preview=audio,
            mensaje="¡Acertaste!",
        )
    else:
        return render_template(
            "index.html",
            cantantes=lista_cantantes,
            preview=audio,
            mensaje=f"¡Fallaste! La canción era {respuesta_correcta}",
        )


if __name__ == "__main__":
    app.run(debug=True)
