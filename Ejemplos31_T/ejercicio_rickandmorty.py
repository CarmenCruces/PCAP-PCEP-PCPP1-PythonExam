import requests
import json
import tkinter as tk
from urllib.request import urlopen
from PIL import ImageTk, Image

def mostrar_personajes(event):
    try:
        respuesta = requests.get("https://rickandmortyapi.com/api/character")
    except requests.RequestException:
        print("Ha ocurrido un error")
    else:
        if respuesta.status_code == requests.codes.ok:
            datos = respuesta.json()['results']
            columna=0
            fila=0
            for item in datos:
                print(item['image'])
                foto = Image.open(urlopen(item['image']))
                foto = ImageTk.PhotoImage(resultado['foto'])
                etiqueta = tk.Label(ventana, image=foto)
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

