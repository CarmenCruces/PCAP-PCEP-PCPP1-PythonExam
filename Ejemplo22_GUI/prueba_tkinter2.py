import tkinter as tk

def obtener_seleccion():
    seleccion = combobox.get()
    etiqueta.config(text="Seleccionaste: " + seleccion)

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Widgets")

# Crear un combobox (selector)
opciones = ["Opción 1", "Opción 2", "Opción 3"]
combobox = tk.OptionMenu(ventana, tk.StringVar(ventana), *opciones)
combobox.pack(pady=10)

# Crear un botón
boton = tk.Button(ventana, text="Obtener selección", command=obtener_seleccion)
boton.pack(pady=5)

# Crear una etiqueta para mostrar la selección
etiqueta = tk.Label(ventana, text="")
etiqueta.pack(pady=10)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
