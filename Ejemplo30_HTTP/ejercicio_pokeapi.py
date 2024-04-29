# Importar la biblioteca requests
import requests
import json

# Intentar hacer una solicitud GET para obtener información sobre todos los alumnos
try:
    respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/ditto")
except requests.RequestException:
    print("ha ocurrido un error")
else:
    # Si la solicitud es exitosa (código de estado 200 OK), imprimir la respuesta JSON
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json()['name'])
        