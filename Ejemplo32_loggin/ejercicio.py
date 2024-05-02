# Con una lista de numeros en modo texto "1", colocar "tres"
# parsear a numero entero
# mostrar la suma
# manejo de errores, excepciones
# los errores llevarlos a una archivo de log
import logging

logging.basicConfig(level=logging.CRITICAL, filename="ejercicio.log", filemode="a", format='[%(asctime)s] %(levelname)s - %(message)s')
logger = logging.getLogger()

datos = ["1","2","tres","4","5"]
suma = 0
for dato in datos:
    try:
        num = int(dato)
    except Exception as ex:
        print(ex)
        logger.setLevel(logging.CRITICAL)
        logger.critical(ex)
    else:
        suma += num

print("Suma:", suma)
