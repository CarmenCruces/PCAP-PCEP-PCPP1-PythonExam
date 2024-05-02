import requests
import json
import tkinter as tk
from PIL import ImageTk, Image
import io

def mostrar_personajes(event):
    try:
        respuesta = requests.get("https://rickandmortyapi.com/api/character?page=1")
    except requests.RequestException:
        print("Ha ocurrido un error")
    else:
        if respuesta.status_code == requests.codes.ok:
            datos = respuesta.json()['results']
            columna=0
            fila=0
            for item in datos:
                print(item['image'])
                imagen_response = requests.get(item['image'])
                imagen_data = Image.open(io.BytesIO(imagen_response.content))
                imagen_data = imagen_data.resize((100, 100))
                foto = ImageTk.PhotoImage(imagen_data)
                etiqueta = tk.Label(ventana, image=foto)
                etiqueta.image = foto
                etiqueta.grid(row=fila, column=columna)
                columna += 1
                if columna == 4:
                    fila +=1
                    columna = 0

ventana = tk.Tk()
ventana.title("Personajes Rick and Morty")
ventana.geometry("400x400")
ventana.bind("<Enter>", mostrar_personajes)

ventana.mainloop()
