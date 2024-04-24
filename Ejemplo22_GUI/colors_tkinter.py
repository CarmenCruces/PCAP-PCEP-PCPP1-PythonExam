# Aplicar colores a los widgets: Puedes aplicar colores a los widgets de Tkinter utilizando el método config y la opción bg (background) para establecer el color de fondo:
import tkinter as tk

# Crear una ventana
ventana = tk.Tk()
ventana.title("Estilo con colores RGB")

# Definir colores RGB
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)

# Convertir colores a formato hexadecimal
rojo_hex = "#{:02x}{:02x}{:02x}".format(rojo[0], rojo[1], rojo[2])
verde_hex = "#{:02x}{:02x}{:02x}".format(verde[0], verde[1], verde[2])
azul_hex = "#{:02x}{:02x}{:02x}".format(azul[0], azul[1], azul[2])
amarillo_hex = "#{:02x}{:02x}{:02x}".format(amarillo[0], amarillo[1], amarillo[2])

# Crear etiquetas con diferentes colores de fondo
etiqueta1 = tk.Label(ventana, text="Rojo", bg=rojo_hex)
etiqueta1.pack(pady=5)
etiqueta2 = tk.Label(ventana, text="Verde", bg=verde_hex)
etiqueta2.pack(pady=5)
etiqueta3 = tk.Label(ventana, text="Azul", bg=azul_hex)
etiqueta3.pack(pady=5)
etiqueta4 = tk.Label(ventana, text="Amarillo", bg=amarillo_hex)
etiqueta4.pack(pady=5)

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()

# La opción bg (background) no es una opción válida para el widget Combobox en Tkinter. Por lo tanto, no puedes establecer el color de fondo directamente con esta opción.

# En su lugar, puedes utilizar el método configure para cambiar el color de fondo después de crear el widget Combobox. Aquí tienes cómo hacerlo:

# combo = tk.ttk.Combobox(ventana, values=colores_2, state="readonly")
# combo.current(0)
# combo.place(x=10, y=480)
# combo.config(background=color_verde) ---> Configurar el color de fondo después de crear el widget
