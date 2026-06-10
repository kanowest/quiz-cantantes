"""Módulo que contiene dos funciones para formatear y comparar las respuestas con los intentos de los usuarios."""

CAMBIO_ACENTOS = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")


def formateo(cadena: str) -> str:
    """Formatea una cadena eliminando acentos, espacios al inicio y al final, y cambiando todo a minúsculas."""
    cadena = cadena.lower()
    cadena = cadena.translate(CAMBIO_ACENTOS)
    cadena = cadena.strip()
    for caracter in cadena:
        if not caracter.isalnum() and caracter != " ":
            cadena = cadena.replace(caracter, "")
    return cadena


def validacion(respuesta: str, intento: str) -> bool:
    """Compara si la respuesta correcta es igual al intento del usuario."""
    return formateo(respuesta) == formateo(intento)
