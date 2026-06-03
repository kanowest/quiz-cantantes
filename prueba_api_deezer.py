import requests

# comprobamos que todo vaya bien con la API
r = requests.get("https://api.deezer.com/search?q=Quevedo")

diccionario = r.json()

# nos interesa el nombre de la canción y el preview (audio de 30 segundos)
for cancion in diccionario["data"]:
    # 'cancion' es ahora el pequeño diccionario de cada pista individual
    nombre = cancion["title"]
    audio = cancion["preview"]

    print(f"Título: {nombre}")
    print(f"Audio: {audio}")
    print("-" * 20)
