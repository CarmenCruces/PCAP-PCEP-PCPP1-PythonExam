import tkinter as tk
from tkinter import messagebox

# Crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de MessageBox')

# Función para mostrar un MessageBox de Advertencia
def mostrar_advertencia():
    messagebox.showwarning("Advertencia", "¡Esto es un MessageBox de Advertencia!")

# Botón para mostrar el MessageBox
boton = tk.Button(ventana, text="Mostrar MessageBox", command=mostrar_advertencia)
boton.pack()

# Mostrar la ventana
ventana.mainloop()
