import requests
import json

'''  Acceder al api de chistes de chuck norris '''
''' Mostrar el chiste  '''
try:
    respuesta = requests.get("https://api.chucknorris.io/jokes/random")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json()['value'])