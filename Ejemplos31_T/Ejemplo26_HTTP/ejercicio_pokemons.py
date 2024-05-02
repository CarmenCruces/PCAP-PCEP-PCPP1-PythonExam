'''
    1ª version: buscar un pokemon y sacar la informacion por consola
    2ª version: crear una GUI solicitar el nombre del pokemon en un Entry
                boton que al pulsar buscar lanza la peticion
                mostrar la informacion en una etiqueta
'''
import requests
import json
import tkinter as tk

'''     1ª version
try:
    nombre = input("Introduce el nombre del pokemon:")
    respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre}")

except requests.RequestException:
    print("Ha ocurrido un error")
else:
    if respuesta.status_code == requests.codes.ok:
        datos = respuesta.json()
        print("Nombre:", datos['name'])
        print("Order:", datos['order'])
        print("Peso:", datos['weight'])
        print("Altura:", datos['height'])
        print("Habilidades:")
        for habilidad in datos['abilities']:
            print("\t.",habilidad['ability']['name'])
'''

def buscar(event):
    global resultado
    try:
        respuesta = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nombre.get()}")

    except requests.RequestException:
        print("Ha ocurrido un error")
    else:
        if respuesta.status_code == requests.codes.ok:
            datos = respuesta.json()
            resultado.set(f"Nombre: {datos['name']} \n"
                          + f"Order: {datos['order']} \n"
                          + f"Peso: {datos['weight']} \n"
                          + f"Altura: {datos['height']} \n"
                          + f"Habilidades:\n")
            for habilidad in datos['abilities']:
                resultado.set(resultado.get() + f"\t. {habilidad['ability']['name']} \n")


ventana = tk.Tk()
ventana.title("Buscar pokemons")
ventana.geometry("400x400")

nombre = tk.StringVar()
label1 = tk.Label(ventana,text="Introduce nombre del pokemon:")
caja1 = tk.Entry(ventana, textvariable=nombre)
label1.pack()
caja1.pack()

boton = tk.Button(ventana, text="Buscar pokemon")
boton.bind("<Button-1>", buscar)
boton.pack()

resultado = tk.StringVar()
label_resultado = tk.Label(ventana, textvariable=resultado )
label_resultado.pack()

ventana.mainloop()