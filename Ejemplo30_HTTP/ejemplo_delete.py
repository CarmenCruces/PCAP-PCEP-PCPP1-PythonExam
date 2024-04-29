import json
import requests

# Definir los nuevos datos del alumno para la solicitud PUT
by_pedro =  {
      "id": "f907",
    "nombre": "Lorena",
    "apellido": "Cruces",
    "nota": 7,
    "repetidor": True
  },
cabeceras = {'Content-type': 'application/json'}

try:
    # Realizar la solicitud PUT para modificar los datos del alumno
    respuesta = requests.delete("http://localhost:3000/alumnos/f907", headers=cabeceras, data=json.dumps(by_pedro))

    # Verificar si la solicitud PUT fue exitosa
    if respuesta.status_code == 200:
        print("Alumno borrado correctamente")
    else:
        print("Error al borrar el alumno:", respuesta.status_code)
except requests.RequestException as e:
    print("Error al borrar el alumno:", e)
