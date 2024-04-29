import json
import requests

# Definir los nuevos datos del alumno para la solicitud PUT
new_juan = {
    "id": "7",
    "nombre": "Lorena",
    "apellido": "Cruces",
    "nota": 7,
    "repetidor": True
}
cabeceras = {'Content-type': 'application/json'}

try:
    # Realizar la solicitud PUT para modificar los datos del alumno
    respuesta = requests.put("http://localhost:3000/alumnos/7", headers=cabeceras, data=json.dumps(new_juan))

    # Verificar si la solicitud PUT fue exitosa
    if respuesta.status_code == 200:
        print("Alumno modificado correctamente")
        # Si la solicitud fue exitosa, intentar obtener los datos del alumno modificado
        juan = requests.get("http://localhost:3000/alumnos/7")
        # Imprimir los datos del alumno modificado
        print("Datos del alumno modificado:", juan.json())
    else:
        print("Error al modificar el alumno:", respuesta.status_code)
except requests.RequestException as e:
    print("Error al modificar el alumno:", e)
