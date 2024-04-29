# Importar la biblioteca requests, que permite realizar solicitudes HTTP en Python
import requests

# Realizar una solicitud GET al servidor local en el puerto 3000
respuesta = requests.get("http://localhost:3000")
# Imprimir el código de estado de la respuesta, por ejemplo, 200 para OK
print(respuesta.status_code)  # 200   OK

# Iterar sobre todos los códigos de estado HTTP definidos en la biblioteca requests
for code in requests.codes.__dict__:
    print(code)

# Condición para ejecutar algo solo si la respuesta se ha recibido correctamente (código 200 OK)
if respuesta.status_code == requests.codes.ok:
    print("Conexion correcta")

# Obtener las cabeceras de la respuesta HTTP
cabeceras = respuesta.headers
print(cabeceras)
print(type(cabeceras))

# Imprimir el valor de una cabecera específica (Content-Type)
print(cabeceras['Content-Type'])
print(respuesta.headers['Connection'])

# Mostrar el texto de la respuesta HTTP
print(respuesta.text)

# Manejo de excepciones: intentar hacer una solicitud con un tiempo de espera de 1 segundo
try:
    respuesta = requests.get("http://localhost:3000", timeout=1)
except requests.exceptions.Timeout:
    print("Error de timeout")
else:
    print("Conexion ok")

# Manejo de excepciones: intentar hacer una solicitud a un servidor que no está disponible en el puerto 3010
try:
    respuesta = requests.get("http://localhost:3010")
except requests.exceptions.ConnectionError:
    print("Error de conexion")
else:
    print("Conexion ok")

# Manejo de excepciones: intentar hacer una solicitud a una URL inválida
try:
    respuesta = requests.get("http:/localhost3010")
except requests.exceptions.InvalidURL:
    print("Error de url")
else:
    print("Conexion ok")

# Imprimir todas las excepciones definidas en la biblioteca requests
print(requests.exceptions)
