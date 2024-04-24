import tkinter as tk
from tkinter import messagebox

# Crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de MessageBox')

# Función para mostrar un MessageBox de Pregunta
def mostrar_pregunta():
    respuesta = messagebox.askquestion("Pregunta", "¿Quieres continuar?")
    if respuesta == 'yes':
        messagebox.showinfo("Respuesta", "Has elegido continuar.")
    else:
        messagebox.showinfo("Respuesta", "Has elegido cancelar.")

# Botón para mostrar el MessageBox
boton = tk.Button(ventana, text="Mostrar MessageBox", command=mostrar_pregunta)
boton.pack()

# Mostrar la ventana
ventana.mainloop()
