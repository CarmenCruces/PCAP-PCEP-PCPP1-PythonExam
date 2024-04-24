# En Tkinter, puedes crear menús utilizando las clases Menu y MenuItem.
import tkinter as tk

# Función para mostrar un mensaje cuando se selecciona una opción del menú
def mostrar_mensaje():
    print("Opción seleccionada")

# Crear una nueva ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Menú")

# Crear un objeto Menu para la barra de menú de la ventana
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

# Crear un menú desplegable "Archivo"
menu_archivo = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)
menu_archivo.add_command(label="Abrir", command=mostrar_mensaje)
menu_archivo.add_command(label="Guardar", command=mostrar_mensaje)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=ventana.quit)

# Crear un menú desplegable "Editar"
menu_editar = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Editar", menu=menu_editar)
menu_editar.add_command(label="Cortar", command=mostrar_mensaje)
menu_editar.add_command(label="Copiar", command=mostrar_mensaje)
menu_editar.add_command(label="Pegar", command=mostrar_mensaje)

# Mostrar la ventana
ventana.mainloop()

# En este ejemplo:

# Se crea una ventana (ventana) y se configura su título.
# Se crea un objeto Menu llamado barra_menu y se configura como el menú principal de la ventana
# utilizando ventana.config(menu=barra_menu).
# Se crean dos menús desplegables, "Archivo" y "Editar", 
# utilizando Menu y se agregan a la barra de menú (barra_menu) usando add_cascade.
# Se añaden elementos de menú a cada menú desplegable utilizando add_command. 
# Cada elemento de menú se puede asociar a una función que se ejecuta cuando se selecciona el elemento.
# Se utiliza tearoff=0 para evitar que los menús desplegables se puedan separar de la barra de menú.
# Finalmente, se inicia el bucle principal de la aplicación con ventana.mainloop().