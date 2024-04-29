import json
import requests

# Definir los nuevos datos del alumno para la solicitud POST
new_alumno = {
    "id": "7",
    "nombre": "Lorena",
    "apellido": "Cruces",
    "nota": 7,
    "repetidor": True
}
cabeceras = {'Content-type': 'application/json'}

try:
    # Realizar la solicitud PUT para modificar los datos del alumno
    respuesta = requests.post("http://localhost:3000/alumnos", headers=cabeceras, data=json.dumps(new_alumno))

    # Verificar si la solicitud PUT fue exitosa
    if respuesta.status_code == 200:
        print("Alumno insertado correctamente")
        # Si la solicitud fue exitosa, intentar obtener los datos del alumno modificado
        juan = requests.get("http://localhost:3000/alumnos")
        # Imprimir los datos del alumno modificado
        print("Datos del alumno insertado:", new_alumno.json())
    else:
        print("Error al insertado el alumno:", respuesta.status_code)
except requests.RequestException as e:
    print("Error al insertado el alumno:", e)