
print("Amador Omar")

import requests


def obtener_clima(latitud, longitud):
  """Consulta la API de Open-Meteo y devuelve un diccionario

  con la temperatura y la velocidad del viento.
  """
  url = "https://api.open-meteo.com/v1/forecast"

  # Parámetros de consulta
  parametros = {
      "latitude": latitud,
      "longitude": longitud,
      "current": "temperature_2m,wind_speed_10m",
  }

  # Petición GET
  respuesta = requests.get(url, params=parametros, timeout=10)
  respuesta.raise_for_status()

  # Extraemos solo el diccionario con los datos actuales
  datos_actuales = respuesta.json()["current"]

  return {
      "temperatura": datos_actuales["temperature_2m"],
      "viento": datos_actuales["wind_speed_10m"],
  }


# -------------------------------------------------------------
# Pruebas con 3 ciudades diferentes
# -------------------------------------------------------------
if __name__ == "__main__":
  # Guadalajara, Monterrey y Cancún
  ciudades = [
      {"nombre": "Guadalajara", "lat": 20.67, "lon": -103.35},
      {"nombre": "Monterrey", "lat": 25.67, "lon": -100.31},
      {"nombre": "Cancún", "lat": 21.16, "lon": -86.85},
  ]

  # Encabezado de la tabla
  print("=" * 60)
  print(f"{'Ciudad':<20} | {'Temp. (°C)':<15} | {'Viento (km/h)':<15}")
  print("-" * 60)

  # Consultamos cada ciudad e imprimimos resultados
  for ciudad in ciudades:
    try:
      clima = obtener_clima(ciudad["lat"], ciudad["lon"])
      print(
          f"{ciudad['nombre']:<20} | {clima['temperatura']:<15} |"
          f" {clima['viento']:<15}"
      )
    except requests.exceptions.RequestException as e:
      print(f"{ciudad['nombre']:<20} | Error al consultar la API")

  print("=" * 60)