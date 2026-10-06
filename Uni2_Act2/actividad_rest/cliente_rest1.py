import requests
print("Amador Omar")

BASE = "https://jsonplaceholder.typicode.com"

respuesta = requests.get(f"{BASE}/posts/1", timeout=10) 

print("Código de estado:", respuesta.status_code)
print("Tipo de contenido:", respuesta.headers["Content-Type"])

publicacion = respuesta.json()	# convierte el JSON en un diccionario de Python 
print("Título:", publicacion["title"])

