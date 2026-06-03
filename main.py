from datos import cantantes
from validacion import validacion
import random

fin = False


print("¡Saludos y bienvenido al juego!")
while not fin:
    cantante = input("¿Con qué cantante quieres jugar? ")
    cambio_cantante = False
    if cantante not in cantantes:
        print(f"{cantante} no está en nuestra base de datos. Inténtalo de nuevo")
        continue
    while not cambio_cantante:
        print(f"Seleccionando una canción al azar de {cantante}...")
        nombre_cancion = random.choice(cantantes[cantante])
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
        )
        while opcion not in "FfCcSs":
            opcion = input("Opción no válida. Inténtalo de nuevo: ")
        if opcion == "F":
            fin = True
            cambio_cantante = True
            print("¡Hasta pronto!")
        elif opcion == "C":
            cambio_cantante = True
