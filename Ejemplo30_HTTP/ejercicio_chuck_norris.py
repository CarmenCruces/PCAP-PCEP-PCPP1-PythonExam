# Importar la biblioteca requests
import requests
import json

# Intentar hacer una solicitud GET para obtener información 
try:
    respuesta = requests.get("https://api.chucknorris.io/jokes/random")
except requests.RequestException:
    print("ha ocurrido un error")
else:
    # Si la solicitud es exitosa (código de estado 200 OK), imprimir la respuesta JSON
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json()['value'])
        
try:
    respuesta = requests.get("https://api.chucknorris.io/jokes/categories")
except requests.RequestException:
    print("ha ocurrido un error")
else:
    # Si la solicitud es exitosa (código de estado 200 OK), imprimir la respuesta JSON
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())
        
# try:
#     respuesta = requests.get("https://api.chucknorris.io/jokes/random?category={animal}")
# except requests.RequestException:
#     print("ha ocurrido un error")
# else:
#     # Si la solicitud es exitosa (código de estado 200 OK), imprimir la respuesta JSON
#     if respuesta.status_code == requests.codes.ok:
#         print(respuesta.json())
        
        
# try:
#     respuesta = requests.get("https://api.chucknorris.io/jokes/search?query={query}")
# except requests.RequestException:
#     print("ha ocurrido un error")
# else:
#     # Si la solicitud es exitosa (código de estado 200 OK), imprimir la respuesta JSON
#     if respuesta.status_code == requests.codes.ok:
#         print(respuesta.json())