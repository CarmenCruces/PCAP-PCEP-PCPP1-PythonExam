import xml.etree.ElementTree as xmlet

# Elegir el documento.xml que vamos a procesar
empleados = xmlet.parse('empleados_2.xml')

# Nos posicionamos en la raiz del documento
root = empleados.getroot()

for hijo in root:
    hijo.remove(hijo.find("sueldo"))

# Volcamos los datos en empleados3.xml
empleados.write("empleados_3.xml" )