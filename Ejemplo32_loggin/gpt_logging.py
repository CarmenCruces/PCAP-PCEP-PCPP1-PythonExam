# El módulo logging en Python proporciona una forma flexible y fácil de registrar mensajes de registro (logs) en tus aplicaciones. Los registros son útiles para rastrear el flujo de ejecución de un programa, depurar problemas y proporcionar información sobre el funcionamiento del mismo.

# Aquí tienes una explicación de los conceptos básicos del manejo del logging en Python:

# Importar el módulologging : Para empezar a utilizar el módulo logging, primero necesitas importarlo en tu script de Python:
# pitón

import logging

# Configurar el registro : Puedes configurar la salida de los mensajes de registro utilizando la función basicConfig()del módulo logging. Esta función te permite especificar dónde quieres que se envíen los mensajes de registro, el nivel mínimo de severidad que quieres registrar y el formato en el que quieres que aparezcan los mensajes.
# pitón


logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# filename: Especifique el nombre del archivo donde se guardarán los registros. Si no se proporciona, los registros se enviarán a la consola.
# level: Especifica el nivel mínimo de gravedad para los mensajes del registrador. Los niveles de gravedad disponibles son DEBUG, INFO, WARNING, ERROR y CRÍTICO.
# format: Especifica el formato en el que se presentarán los mensajes de registro.
# Mensajes del registrador : Una vez configurado el registro, puede registrar mensajes utilizando las funciones de registro proporcionadas por el módulo logging. Las funciones de registro más comunes son:

logging.debug()
logging.info()
logging.warning()
logging.error()
logging.critical()

# Por ejemplo:

logging.debug('Este es un mensaje de depuración')
logging.info('Esta es una información general')
logging.warning('Este es un mensaje de advertencia')
logging.error('¡Se ha producido un error!')
logging.critical('¡Esto es crítico!')

# Gestión de objetos Logger : Además de las funciones de registro mencionadas anteriormente, también puedes crear y usar objetos Loggerpersonalizados para registrar mensajes en tu aplicación. Esto te permite tener un mayor control sobre el manejo de los registros.

logger = logging.getLogger('mi_aplicacion')
logger.setLevel(logging.DEBUG)

# Agregar un controlador (handler) para enviar los registros a un archivo
handler = logging.FileHandler('mi_aplicacion.log')
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# Registrar mensajes utilizando el objeto Logger
logger.debug('Este es un mensaje de depuración')
logger.info('Esta es una información general')
logger.warning('Este es un mensaje de advertencia')
logger.error('¡Se ha producido un error!')
logger.critical('¡Esto es crítico!')

# Gestión de Niveles de Severidad : Los mensajes de registro se filtran según su nivel de severidad. Puedes configurar el nivel de gravedad para los mensajes que deseas registrar utilizando la función setLevel(). Los mensajes con un nivel de gravedad igual o superior al nivel configurado se registrarán.Por ejemplo:

logging.basicConfig(level=logging.DEBUG)

# Esto registrará todos los mensajes de DEBUG y niveles superiores.