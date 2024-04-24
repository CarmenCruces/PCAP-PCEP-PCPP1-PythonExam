# Definir colores RGB: Puedes definir tus propios colores en RGB como tuplas de tres números enteros:
rojo = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)
amarillo = (255, 255, 0)

# Convertir colores a formato hexadecimal: Tkinter generalmente usa el formato hexadecimal para los colores. Puedes convertir los valores RGB a formato hexadecimal fácilmente con una función auxiliar:
def rgb_a_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# Uso
print(rgb_a_hex(rojo))  # Output: "#ff0000"
