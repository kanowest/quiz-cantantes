"""Módulo que contiene dos funciones para formatear y comparar las respuestas con los intentos de los usuarios."""

CAMBIO_ACENTOS = str.maketrans("áéíóúÁÉÍÓÚ", "aeiouAEIOU")


def formateo(cadena: str) -> str:
    """Formatea una cadena eliminando acentos, espacios al inicio y al final, y cambiando todo a minúsculas."""
    cadena = cadena.lower()
    cadena = cadena.translate(CAMBIO_ACENTOS)
    return cadena.strip()


def validacion(respuesta: str, intento: str) -> bool:
    """Compara si la respuesta correcta es igual al intento del usuario."""
    resp_norm = formateo(respuesta)
    int_norm = formateo(intento)

    resp_ajustada = ""
    for caracter in resp_norm:
        if caracter.isalnum() or caracter == " " or caracter in int_norm:
            resp_ajustada += caracter

    return resp_ajustada == int_norm
