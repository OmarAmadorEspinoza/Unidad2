import requests
print("Amador Omar")

BASE = "https://jsonplaceholder.typicode.com"

respuesta = requests.get(f"{BASE}/posts/1", timeout=10) 

print("Código de estado:", respuesta.status_code)
print("Tipo de contenido:", respuesta.headers["Content-Type"])

publicacion = respuesta.json()	# convierte el JSON en un diccionario de Python 
print("Título:", publicacion["title"])

respuesta = requests.get(f"{BASE}/posts", params={"userId": 3}, timeout=10) 
publicaciones = respuesta.json()	# lista de diccionarios

print("Total:", len(publicaciones)) 
for p in publicaciones:
	print(f"{p['id']:>3} | {p['title']}")
