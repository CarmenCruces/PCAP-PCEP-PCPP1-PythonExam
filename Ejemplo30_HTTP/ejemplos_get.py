# Importar la biblioteca requests
import requests

# Intentar hacer una solicitud GET para obtener información sobre todos los alumnos
try:
    respuesta = requests.get("http://localhost:3000/alumnos")
except requests.RequestException:
    print("ha ocurrido un error")
else:
    # Si la solicitud es exitosa (código de estado 200 OK), imprimir la respuesta JSON
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())
        
# Consultar todos los alumnos ordenados por nota mediante el parámetro _sort
try:
    respuesta = requests.get("http://localhost:3000/alumnos?_sort=nota")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    # Si la solicitud es exitosa, imprimir la respuesta JSON ordenada por nota
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())
        

try:
    # Realizar una solicitud GET para obtener todos los alumnos ordenados por nota de forma des
    respuesta = requests.get("http://localhost:3000/alumnos?_sort=-nota")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    # Si la solicitud es exitosa, imprimir la respuesta JSON ordenada por nota
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())
        
#         #repetidor true
# try:
#     # Realizar una solicitud GET para obtener todos los alumnos donde la propiedad "repetidor" sea igual a true
#     respuesta = requests.get("http://localhost:3000/alumnos?repetidor=True")
# except requests.RequestException:
#     print("Ha ocurrido un error")
# else:
#     # Si la solicitud es exitosa, imprimir la respuesta JSON filtrada por la condición
#     if respuesta.status_code == requests.codes.ok:
#         print(respuesta.json())
        
try:
    # Realizar una solicitud GET para obtener todos los alumnos que son repetidores
    respuesta = requests.get("http://localhost:3000/alumnos?repetidor=1")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    # Si la solicitud es exitosa, imprimir la respuesta JSON filtrada por la condición
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())

# Buscar un alumno por su id
try:
    respuesta = requests.get("http://localhost:3000/alumnos/3")
except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        print(respuesta.json())  # Muestra como un json  # metodo
        



