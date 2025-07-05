
import requests


graphhopper_api_key = "18bb06b4-322a-4748-b36c-c80780b0f7b8"  
locale = "es"

# Santiago de Chile 
origen_coord = "-33.4489,-70.6693"

# Mendoza, Argentina 
destino_coord = "-32.8908,-68.8272"


while True:
    print("\n==== Calculador de Distancia Chile - Argentina ====")
    ciudad_origen = input("Ciudad de Origen (o s para salir): ")
    if ciudad_origen.lower() == "s":
        print("Programa finalizado.")
        break

    ciudad_destino = input("Ciudad de Destino: ")
    medio = input("Medio de transporte (car/bike/foot): ")

    url = (
        f"https://graphhopper.com/api/1/route"
        f"?point={origen_coord}"
        f"&point={destino_coord}"
        f"&vehicle={medio}"
        f"&locale={locale}"
        f"&key={graphhopper_api_key}"
    )

    response = requests.get(url)
    data = response.json()

    if "paths" not in data:
        print("No se encontró ruta.")
        continue

    ruta = data['paths'][0]

    distancia_km = ruta['distance'] / 1000
    distancia_millas = distancia_km * 0.621371
    duracion_hr = ruta['time'] / 3600000
    duracion_min = ruta['time'] / 60000

    print(f"\nDistancia aproximada: {distancia_km:.2f} km / {distancia_millas:.2f} millas")
    print(f"Duración aproximada: {duracion_hr:.2f} horas\n")
    print(f"Duración aproximada: {duracion_min:.2f} minutos\n")
    

    print("Narrativa del viaje:")
    for paso in ruta['instructions']:
        print(f" - {paso['text']}")