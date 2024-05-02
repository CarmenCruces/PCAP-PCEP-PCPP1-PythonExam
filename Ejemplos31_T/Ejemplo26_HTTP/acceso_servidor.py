'''
    Para crear el servidor
    1.- Descargar node e instalarlo: https://nodejs.org/en/download
    2.- Desde un cmd con permisos de administrador: npm i -g json-server
    3.- Crear el archivo alumnos.json
    4.- En el cmd nos hemos posicionado donde tenemos ese archivo alumnos.json
    5.-  Publicar el archivo en el servidor: json-server --watch alumnos.json
'''

import requests

respuesta = requests.get("http://localhost:3000")
print(respuesta.status_code)  # 200   OK

# Ver todos los codigos de respuesta
for code in requests.codes.__dict__:
    #print(code)
    pass

# Condicional para ejecutar algo, solo si la respuesta se ha recibido correctamente
if respuesta.status_code == requests.codes.ok:
    print("Conexion correcta")

# Obtener las cabeceras
cabeceras = respuesta.headers
print(cabeceras)
print(type(cabeceras))

# Ver una cabecera en concreto
print(cabeceras['Content-Type'])
print(respuesta.headers['Connection'])

# Mostrar el texto de la respuesta
print(respuesta.text)  # mostrar la pagina index.html

# Manejo de excepciones
try:
    respuesta = requests.get("http://localhost:3000", timeout=1)
except requests.exceptions.Timeout:
    print("Error de timeout")
else:
    print("Conexion ok")

try:
    respuesta = requests.get("http://localhost:3010")
except requests.exceptions.ConnectionError:
    print("Error de conexion")
else:
    print("Conexion ok")

try:
    respuesta = requests.get("http:/localhost3010")
except requests.exceptions.InvalidURL:
    print("Error de url")
else:
    print("Conexion ok")

# Ver todas las excepciones
print(requests.exceptions)