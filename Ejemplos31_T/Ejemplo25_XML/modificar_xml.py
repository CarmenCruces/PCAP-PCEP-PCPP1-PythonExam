import xml.etree.ElementTree as xmlet

# Elegir el documento.xml que vamos a procesar
empleados = xmlet.parse('empleados_2.xml')

# Nos posicionamos en la raiz del documento
root = empleados.getroot()

for hijo in root:
    asignado = xmlet.SubElement(hijo, 'asignado', {'proyecto':'BBVA'})


# Escribimos el archivo
empleados.write("empleados_4.xml",method='')
