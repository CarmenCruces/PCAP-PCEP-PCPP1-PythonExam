import tkinter as tk
import requests
from PIL import Image, ImageTk
import io

def buscar_personaje():
    nombre = entry_personaje.get()
    try:
        respuesta = requests.get(f"https://rickandmortyapi.com/api/character/?name={nombre}")
        if respuesta.status_code == 200:
            datos = respuesta.json()
            if datos['results']:
                personaje = datos['results'][0]
                mostrar_info_personaje(personaje)
            else:
                print("No se encontró el personaje")
        else:
            print("Error al hacer la solicitud")
    except requests.RequestException:
        print("Error al hacer la solicitud")

def mostrar_info_personaje(personaje):
    nombre = personaje['name']
    especie = personaje['species']
    imagen_url = personaje['image']
    imagen_respuesta = requests.get(imagen_url)
    imagen = Image.open(io.BytesIO(imagen_respuesta.content))
    imagen = imagen.resize((100, 100), resample=Image.BILINEAR)  # Corrección aquí
    imagen = ImageTk.PhotoImage(imagen)
    
    etiqueta_nombre.config(text=f"Nombre: {nombre}")
    etiqueta_especie.config(text=f"Especie: {especie}")
    etiqueta_imagen.config(image=imagen)
    etiqueta_imagen.image = imagen  # Mantener una referencia para evitar que la imagen se borre

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Búsqueda de Personajes de Rick and Morty")
ventana.geometry("600x400")  # Ajustar el tamaño de la ventana

# Crear un Entry para ingresar el nombre del personaje
entry_personaje = tk.Entry(ventana)
entry_personaje.grid(row=0, column=0, padx=10, pady=10)  # Colocar el Entry en la primera fila, primera columna

# Crear un botón para realizar la búsqueda
boton_buscar = tk.Button(ventana, text="Buscar", command=buscar_personaje)
boton_buscar.grid(row=0, column=1, padx=10, pady=10)  # Colocar el botón en la primera fila, segunda columna

# Crear etiquetas para mostrar la información del personaje
etiqueta_nombre = tk.Label(ventana, text="Nombre: ")
etiqueta_nombre.grid(row=1, column=0, padx=10, pady=10)  # Colocar la etiqueta en la segunda fila, primera columna
etiqueta_especie = tk.Label(ventana, text="Especie: ")
etiqueta_especie.grid(row=2, column=0, padx=10, pady=10)  # Colocar la etiqueta en la tercera fila, primera columna
etiqueta_imagen = tk.Label(ventana)
etiqueta_imagen.grid(row=1, column=1, rowspan=2, padx=10, pady=10)  # Corrección aquí

# Ejecutar el bucle de eventos de la ventana
ventana.mainloop()





