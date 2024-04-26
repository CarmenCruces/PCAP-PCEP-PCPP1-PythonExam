import os
import pandas as pd # Importamos la biblioteca Pandas y la renombramos como pd para abreviar su uso en el código.

# Obtener la ruta del directorio actual del script
dir_path = os.path.dirname(os.path.realpath(__file__))

# Construir la ruta completa a los archivos CSV
navegacion_csv_path = os.path.join(dir_path, "archivos_practica", "navegacion.csv")
conversiones_csv_path = os.path.join(dir_path, "archivos_practica", "conversiones.csv")

# Paso 1: Cargar datos
# Cargamos los datos del archivo "navegacion.csv" en un DataFrame llamado navegacion_df.
# Este DataFrame contendrá los datos de navegación de los usuarios.
navegacion_df = pd.read_csv(navegacion_csv_path)
print(navegacion_df.head())

# Cargamos los datos del archivo "archivo_conversiones.csv" en otro DataFrame llamado conversiones_df.
# Este DataFrame contendrá los datos de conversiones de los usuarios.
# Cargar datos con eliminación de espacios en los nombres de las columnas
conversiones_df = pd.read_csv(conversiones_csv_path)
print(conversiones_df.head())

#--------------------------------------------------------------------------------------------------------
conversiones_df = pd.read_csv("archivos_practica/conversiones.csv", delimiter=';', skipinitialspace=True)
print(conversiones_df.columns)
#--------------------------------------------------------------------------------------------------------

# Paso 2: Análisis de visitas
# Calculamos el número total de visitas contando el número de filas en el DataFrame navegacion_df.
total_visitas = len(navegacion_df)

# Calculamos el número total de conversiones contando el número de filas en el DataFrame conversiones_df.
total_conversiones = len(conversiones_df)

# Calculamos el porcentaje de conversiones dividiendo el número total de conversiones entre el número total de visitas y multiplicándolo por 100.
porcentaje_conversiones = (total_conversiones / total_visitas) * 100

# Calculamos el porcentaje de no conversiones restando el porcentaje de conversiones del 100%.
porcentaje_no_conversiones = 100 - porcentaje_conversiones

# Paso 3: Análisis por tipo de conversión
# Contamos el número de conversiones de cada tipo ("CALL" y "FORM") y almacenamos los resultados en una Serie de Pandas llamada conversiones_por_tipo.
conversiones_por_tipo = conversiones_df['lead_type'].value_counts()

# Calculamos el porcentaje de conversiones de tipo "CALL" dividiendo el número de conversiones de tipo "CALL" entre el número total de conversiones y multiplicándolo por 100.
porcentaje_calls = (conversiones_por_tipo.get('CALL', 0) / total_conversiones) * 100

# Calculamos el porcentaje de conversiones de tipo "FORM" de manera similar al paso anterior.
porcentaje_forms = (conversiones_por_tipo.get('FORM', 0) / total_conversiones) * 100

# Paso 4: Análisis de usuarios recurrentes
# Filtramos el DataFrame navegacion_df para obtener solo las filas donde la columna "user_recurrent" es igual a True, es decir, los usuarios recurrentes.
usuarios_recurrentes = navegacion_df[navegacion_df['user_recurrent'] == True]

# Calculamos el porcentaje de usuarios recurrentes dividiendo el número de usuarios recurrentes entre el número total de visitas y multiplicándolo por 100.
porcentaje_recurrentes = (len(usuarios_recurrentes) / len(navegacion_df)) * 100

# Se imprime el resultado de los análisis en la consola utilizando la función print().
print("Análisis de visitas:")
print("Total de visitas:", total_visitas)
print("Porcentaje de conversiones:", porcentaje_conversiones)
print("Porcentaje de no conversiones:", porcentaje_no_conversiones)

print("\nAnálisis por tipo de conversión:")
print("Porcentaje de conversiones CALL:", porcentaje_calls)
print("Porcentaje de conversiones FORM:", porcentaje_forms)

print("\nAnálisis de usuarios recurrentes:")
print("Porcentaje de usuarios recurrentes:", porcentaje_recurrentes)

