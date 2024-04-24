import tkinter as tk
from tkinter import ttk

# Crear una nueva ventana
ventana = tk.Tk()
ventana.title('Ejemplo de widgets')
ventana.geometry('400x600+500+200')  # anchoxalto+desp_x+desp_y

# Paleta de colores
color_azul = '#5DADE2'  # Azul claro
color_rosa = '#F1948A'  # Rosa claro
color_amarillo = '#F7DC6F'  # Amarillo claro
color_verde = '#82E0AA'  # Verde claro

# Añadir los widgets a la ventana
boton = tk.Button(ventana, text='Pulsame', bg=color_azul)
boton.place(x=10,y=20)

# Frame 1 - Datos Personales
frame_1 = tk.LabelFrame(ventana, width=400, height=150, text="Datos Personales", bg=color_rosa)
frame_1.place(x=10, y= 50)

etiqueta_nombre = tk.Label(frame_1, text='Introduce tu nombre:', bg=color_rosa, fg='white')
etiqueta_nombre.place(x=10, y=50)

caja_texto_nombre = tk.Entry(frame_1,width=20)
caja_texto_nombre.place(x=150, y=50)

etiqueta_password = tk.Label(frame_1, text='Introduce tu contraseña:', bg=color_rosa, fg='white')
etiqueta_password.place(x=10, y=80)

caja_texto_password = tk.Entry(frame_1, show='*')
caja_texto_password.place(x=150, y=80)

etiqueta_default = tk.Label(frame_1, text='Texto predeterminado:', bg=color_rosa, fg='white')
etiqueta_default.place(x=10, y=110)

mystr = tk.StringVar()
mystr.set('This is the default text')
caja_texto_deshabilitada = tk.Entry(frame_1,width=20, state='readonly', textvariable=mystr)
caja_texto_deshabilitada.place(x=150, y=110)

# Checkbutton
acepto = tk.Checkbutton(ventana, text='Acepto condiciones', bg=color_amarillo)
acepto.place(x=200, y= 200)

# Radiobuttons
sexo_var = tk.StringVar()
sexo_h = tk.Radiobutton(ventana, text="Hombre", variable=sexo_var, value="H", bg=color_amarillo)
sexo_m = tk.Radiobutton(ventana, text="Mujer", variable=sexo_var, value="M", bg=color_amarillo)
sexo_h.place(x=10, y= 250)
sexo_m.place(x=100, y= 250)

# Listbox
colores = ['Azul','Rosa','Amarillo','Verde']
color = tk.Listbox(ventana, selectmode='multiple', activestyle="dotbox", bg=color_verde)
for item in colores:
    color.insert(tk.END, item)
color.place(x=10, y=300)

# Combobox
colores_2= ['--Selecciona--'] + colores
combo = ttk.Combobox(ventana, values=colores_2, state="readonly")
combo.current(0)
combo.place(x=10, y=480)
combo.configure(background=color_verde)  # Configurar el color de fondo después de crear el widget

# OptionMenu
opciones = ['--Selecciona--',"Opción 1", "Opción 2", "Opción 3"]
opcion_seleccionada = tk.StringVar(ventana)
opcion_seleccionada.set(opciones[0])
combobox = tk.OptionMenu(ventana, opcion_seleccionada, *opciones)
combobox.place(x=10, y=550)
combobox.configure(background=color_verde)  # Configurar el color de fondo después de crear el widget

# Mostrar la ventana
ventana.mainloop()


