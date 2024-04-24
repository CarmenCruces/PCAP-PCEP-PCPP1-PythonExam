# Los messagebox son ventanas emergentes que se utilizan para mostrar mensajes al usuario en una aplicación GUI. Tkinter proporciona la clase messagebox para crear y mostrar diferentes tipos de messagebox, como messagebox de información, advertencia, error, pregunta, etc.
import tkinter as tk
from tkinter import messagebox

# Crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de MessageBox')

# Función para mostrar un MessageBox de Información
def mostrar_mensaje():
    messagebox.showinfo("Mensaje", "¡Esto es un MessageBox de Información!")

# Botón para mostrar el MessageBox
boton = tk.Button(ventana, text="Mostrar MessageBox", command=mostrar_mensaje)
boton.pack()

# Mostrar la ventana
ventana.mainloop()
