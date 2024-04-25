import tkinter as tk

def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)
        resultado_var.set(resultado)
    except Exception as e:
        resultado_var.set("Error")

def agregar_igual():
    entrada.insert(tk.END, "=")
    calcular()

ventana = tk.Tk()
ventana.title("Calculadora")

resultado_var = tk.StringVar()
resultado_var.set("")

entrada = tk.Entry(ventana, textvariable=resultado_var, font=('Arial', 14))
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="ew")

botones = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

fila = 1
columna = 0

for boton_texto in botones:
    tk.Button(ventana, text=boton_texto, width=5, height=2, command=lambda text=boton_texto: entrada.insert(tk.END, text)).grid(row=fila, column=columna)
    columna += 1
    if columna > 3:
        columna = 0
        fila += 1

tk.Button(ventana, text="C", width=5, height=2, command=lambda: entrada.delete(0, tk.END)).grid(row=fila, column=1)

tk.Button(ventana, text="=", width=5, height=2, command=calcular).grid(row=fila, column=2)

ventana.mainloop()



