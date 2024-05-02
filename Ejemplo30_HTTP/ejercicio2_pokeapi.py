'''
    1ª version: buscar un pokemon y sacar la informacion por consola
    2ª version: crear una GUI solicitar el nombre del pokemon en un Entry
                boton que al pulsar buscar lanza la peticion
                mostrar la informacion en una etiqueta
'''

# # Importar la biblioteca requests
# import requests
# import json
# #import tinker

# # Intentar hacer una solicitud GET para obtener información 
# try:
#     nombre = input('Introduce el nombre del Pokémon: ')
#     print("Realizando solicitud GET...")
#     respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre}")
#     print("Solicitud GET completada.")
# except requests.RequestException:
#     print("Ha ocurrido un error al hacer la solicitud")
# else:
#     if respuesta.status_code == 200:
#         datos = respuesta.json()
        
#         print("Nombre: ", datos['name'])
#         print("Order: ", datos['order'])
#         print("Peso: ", datos['weight'])
#         print("Altura: ", datos['height'])
#         print("Habilidades: ")
        
#         for habilidad in datos ['abilities']:
#             print("\t-", habilidad['ability']['name'])
            
import tkinter as tk
import requests

def buscar_pokemon():
    nombre = entry_pokemon.get()
    try:
        respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}")
        if respuesta.status_code == 200:
            datos = respuesta.json()
            # Actualizar la etiqueta con la información del Pokémon y sus habilidades
            habilidades = ", ".join(habilidad['ability']['name'] for habilidad in datos['abilities'])
            etiqueta_info.config(text=f"Nombre: {datos['name']}\nOrden: {datos['order']}\nPeso: {datos['weight']}\nAltura: {datos['height']}\nHabilidades: {habilidades}")
        else:
            etiqueta_info.config(text="No se encontró el Pokémon")
    except requests.RequestException:
        etiqueta_info.config(text="Error al hacer la solicitud")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Búsqueda de Pokémon")
ventana.geometry("400x200")  # Ajustar el tamaño de la ventana

# Crear un Entry para ingresar el nombre del Pokémon
entry_pokemon = tk.Entry(ventana)
entry_pokemon.pack()

# Crear un botón para realizar la búsqueda
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_pokemon)
boton_buscar.pack()

# Crear una etiqueta para mostrar la información del Pokémon
etiqueta_info = tk.Label(ventana, text="", wraplength=380)  # Ajustar el ancho de la etiqueta
etiqueta_info.pack()

# Ejecutar el bucle de eventos de la ventana
ventana.mainloop()


