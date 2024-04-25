import tkinter as tk  # Importa la biblioteca tkinter y la renombra como tk

# Función para calcular el resultado
def calcular():
    try:
        expresion = entrada.get()  # Obtiene la expresión de la entrada de texto
        resultado = eval(expresion)  # Calcula el resultado de la expresión
        resultado_var.set(resultado)  # Establece el resultado en la variable resultado_var
    except Exception as e:  # Maneja cualquier error que ocurra durante el cálculo
        resultado_var.set("Error")  # Establece "Error" en la variable resultado_var si ocurre un error

# Función para agregar el signo "=" a la entrada de texto y calcular el resultado
def agregar_igual():
    entrada.insert(tk.END, "=")  # Agrega el signo "=" al final de la entrada de texto
    calcular()  # Calcula el resultado

# Crear una nueva ventana
ventana = tk.Tk()  # Crea una nueva ventana principal
ventana.title("Calculadora")  # Establece el título de la ventana como "Calculadora"

# Variables
resultado_var = tk.StringVar()  # Crea una variable de tipo StringVar para almacenar el resultado
resultado_var.set("")  # Inicializa la variable resultado_var con una cadena vacía

# Entrada de texto para la expresión
entrada = tk.Entry(ventana, textvariable=resultado_var, font=('Arial', 14))  # Crea una entrada de texto para la expresión
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")  # Coloca la entrada de texto en la ventana

# Estilos de los botones
estilo_botones = {'font': ('Arial', 12), 'width': 5, 'height': 2}  # Define un diccionario de estilos para los botones

# Botones numericos
botones_numericos = [  # Define una lista de tuplas con el texto y la posición de los botones numéricos
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),  # Define los botones del 7 al 9 en la primera fila
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),  # Define los botones del 4 al 6 en la segunda fila
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2),  # Define los botones del 1 al 3 en la tercera fila
    ('0', 4, 0), ('.', 4, 1)  # Define el botón 0 y el botón de punto en la cuarta fila
]

for texto, fila, columna in botones_numericos:  # Itera sobre la lista de botones numéricos
    tk.Button(ventana, text=texto, bg="lightblue", **estilo_botones,  # Crea un botón numérico con el texto y el estilo correspondiente
              command=lambda t=texto: entrada.insert(tk.END, t)).grid(row=fila, column=columna)  # Coloca el botón en la ventana

# Botones de operaciones
botones_operaciones = [  # Define una lista de tuplas con el texto y la posición de los botones de operaciones
    ('/', 1, 3), ('*', 2, 3), ('-', 3, 3), ('+', 4, 3)  # Define los botones de división, multiplicación, resta y suma en la cuarta columna
]

for texto, fila, columna in botones_operaciones:  # Itera sobre la lista de botones de operaciones
    tk.Button(ventana, text=texto, bg="lightgreen", **estilo_botones,  # Crea un botón de operación con el texto y el estilo correspondiente
              command=lambda t=texto: entrada.insert(tk.END, t)).grid(row=fila, column=columna)  # Coloca el botón en la ventana

# Botón para borrar
tk.Button(ventana, text="C", bg="red", **estilo_botones,  # Crea un botón de borrado con el texto y el estilo correspondiente
          command=lambda: entrada.delete(0, tk.END)).grid(row=4, column=2)  # Coloca el botón en la ventana

# Botón para calcular el resultado
tk.Button(ventana, text="=", bg="orange", **estilo_botones,  # Crea un botón de resultado con el texto y el estilo correspondiente
          command=calcular).grid(row=4, column=1)  # Coloca el botón en la ventana

# Mostrar la ventana
ventana.mainloop()  # Inicia el bucle principal de la ventana
