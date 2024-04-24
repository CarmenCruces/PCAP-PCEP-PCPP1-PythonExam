import tkinter as tk
from tkinter import messagebox

# Crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de MessageBox')

# Función para mostrar un MessageBox de Error
def mostrar_error():
    messagebox.showerror("Error", "¡Esto es un MessageBox de Error!")

# Botón para mostrar el MessageBox
boton = tk.Button(ventana, text="Mostrar MessageBox", command=mostrar_error)
boton.pack()

# Mostrar la ventana
ventana.mainloop()
