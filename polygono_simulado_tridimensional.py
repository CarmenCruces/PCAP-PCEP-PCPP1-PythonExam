#EN PROCESO........

import tkinter as tk

def proyectar(x, y, z):
    # Proyectar las coordenadas tridimensionales (x, y, z) en un plano bidimensional
    # Utilizamos una proyección simple para este ejemplo
    return x, y - z

# Coordenadas de los vértices del polígono tridimensional
vertices = [
    (100, 100, 100),
    (200, 100, 100),
    (200, 200, 100),
    (100, 200, 100),
    (100, 100, 200),
    (200, 100, 200),
    (200, 200, 200),
    (100, 200, 200)
]

# Crear una ventana
root = tk.Tk()
root.title("Polígono Tridimensional")

# Crear un lienzo
canvas = tk.Canvas(root, width=300, height=300)
canvas.pack()

# Dibujar las aristas del polígono tridimensional
for i in range(4):
    x1, y1 = proyectar(*vertices[i])
    x2, y2 = proyectar(*vertices[i + 4])
    canvas.create_line(x1, y1, x2, y2)

for i in range(4):
    x1, y1 = proyectar(*vertices[i])
    x2, y2 = proyectar(*vertices[(i + 1) % 4])
    canvas.create_line(x1, y1, x2, y2)

    x1, y1 = proyectar(*vertices[i + 4])
    x2, y2 = proyectar(*vertices[((i + 1) % 4) + 4])
    canvas.create_line(x1, y1, x2, y2)

    x1, y1 = proyectar(*vertices[i])
    x2, y2 = proyectar(*vertices[i + 4])
    canvas.create_line(x1, y1, x2, y2)

# Iniciar el bucle de eventos
root.mainloop()
