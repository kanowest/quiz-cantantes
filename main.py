"""Como esto es para ver y probar la lógica de validación, no necesitamos sacar el audio."""

from datos import lista_cantantes
from validacion import validacion
import random
import requests


def obtener_cancion_deezer(nombre_artista):
    nombre_artista = nombre_artista.replace(" ", "-")
    r_id = requests.get(f"https://api.deezer.com/artist/{nombre_artista}")
    diccionario_id = r_id.json()
    id = diccionario_id["id"]

    # hacemos una primera petición para saber cuantas canciones tiene el artista
    temp = requests.get(f"https://api.deezer.com/artist/{id}/top?limit=1")
    diccionario_temp = temp.json()
    total = diccionario_temp["total"]

    index = random.randint(0, total - 1)
    r = requests.get(f"https://api.deezer.com/artist/{id}/top?limit=1&index={index}")
    diccionario = r.json()
    return diccionario["data"][0]["title"]


if __name__ == "__main__":
    fin = False

    print("¡Saludos y bienvenido al juego!")
    while not fin:
        cantante_input = input("¿Con qué cantante quieres jugar? ").strip()
        cambio_cantante = False

        cantante = next(
            (c for c in lista_cantantes if c.lower() == cantante_input.lower()), None
        )

        if cantante is None:
            print(
                f"'{cantante_input}' no está en nuestra base de datos. Inténtalo de nuevo"
            )
            continue

        while not cambio_cantante:
            print(f"Seleccionando una canción al azar de {cantante} desde Deezer...")
            nombre_cancion = obtener_cancion_deezer(cantante)

            if not nombre_cancion:
                print(
                    "No se pudo obtener ninguna canción para este artista en este momento."
                )
                break

            print("Canción seleccionada.")

            intento = input("Introduce el nombre de la canción que crees que es: ")

            if validacion(nombre_cancion, intento):
                print("¡Enhorabuena, has acertado!")
            else:
                print("Lástima, no es correcto.")

            print(f"Tu respuesta: {intento}")
            print(f"Respuesta correcta: {nombre_cancion}")

            opcion = input(
                "¿Qué quieres hacer? (F: fin, C: cambiar de cantante, S: seguir con este cantante): "
            ).upper()

            while opcion not in ["F", "C", "S"]:
                opcion = input("Opción no válida. Inténtalo de nuevo: ").upper()

            if opcion == "F":
                fin = True
                cambio_cantante = True
                print("¡Hasta pronto!")
            elif opcion == "C":
                cambio_cantante = True
