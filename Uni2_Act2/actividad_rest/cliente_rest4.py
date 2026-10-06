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

nuevo = {"title": "Prueba de red", "body": "Contenido de ejemplo", "userId": 1}
r = requests.post(f"{BASE}/posts", json=nuevo, timeout=10) 
print("POST:", r.status_code, r.json())

r = requests.put(f"{BASE}/posts/1", json={**nuevo, "id": 1}, timeout=10) 
print("PUT:", r.status_code, r.json())

r = requests.delete(f"{BASE}/posts/1", timeout=10) 
print("DELETE:", r.status_code)

try:
	r = requests.get(f"{BASE}/posts/9999", timeout=10)
	r.raise_for_status()	# lanza excepción si el código es 4xx o 5xx 
	print(r.json())
except requests.exceptions.HTTPError as e: 
	print("Error HTTP:", e)
except requests.exceptions.RequestException as e: 
	print("Error de conexión:", e)
