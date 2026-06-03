CAMBIO_ACENTOS = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")


def formateo(cadena):
    cadena = cadena.lower()
    cadena = cadena.translate(CAMBIO_ACENTOS)
    cadena = cadena.strip()
    for caracter in cadena:
        if not caracter.isalnum():
            cadena = cadena.replace(caracter, "")
    return cadena


def validacion(respuesta, intento):
    return formateo(respuesta) == formateo(intento)
