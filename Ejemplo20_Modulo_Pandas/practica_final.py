#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Crear un dfNavegacion a partir del fichero navegacion.csv
dfNavegacion = pd.read_csv("archivos_practica/navegacion.csv", sep=";")
dfNavegacion


# In[3]:


# Comprobar cuantos id_user repetidos hay
# groupby
#print(dfNavegacion.groupby(["id_user"]).size())
# value_counts
print(dfNavegacion["id_user"].value_counts().head(50))


# In[4]:


# Comprobar cuantos gclid repetidos hay
print(dfNavegacion["gclid"].value_counts().head(50))


# In[5]:


# El gclid = 0 con 35 ocurrencias lo borramos
gclid0 = dfNavegacion[dfNavegacion["gclid"] == '0'].index
# compruebo que me devuelve los 35 indices
gclid0
# borramos los indices almacenados en gclid0
dfNavegacion = dfNavegacion.drop(gclid0)


# In[6]:


# El gclid = 'EAIaIQobChMIwPu5t4qs3AIVAQAAAB0BAAAAEAAYACAAEgJVzfD_BwE' con 124 ocurrencias lo borramos
gclid124 = dfNavegacion[dfNavegacion["gclid"] == 'EAIaIQobChMIwPu5t4qs3AIVAQAAAB0BAAAAEAAYACAAEgJVzfD_BwE'].index
# compruebo que me devuelve los 124 indices
gclid124.size
# borramos los indices almacenados en gclid0
dfNavegacion = dfNavegacion.drop(gclid124)


# In[7]:


# El gclid = 'CjwKCAjwjbCDBhAwEiwAiudBy3jlJeW4vAzqieU59RXrhxtMvbHXgK5UdK0KHtUCtcp6GWd38D0u6BoC76EQAvD_BwE' con 10 ocurrencias comprobar si pertenece al mismo usuario (id_user)
dfNavegacion['id_user'][dfNavegacion["gclid"] == 'CjwKCAjwjbCDBhAwEiwAiudBy3jlJeW4vAzqieU59RXrhxtMvbHXgK5UdK0KHtUCtcp6GWd38D0u6BoC76EQAvD_BwE']


# In[8]:


# No tiene sentido que el mismo identificador de clic (gclid) lo asigne a diferentes usuarios (id_user)
# Eliminar las lineas con ese gclid = 'CjwKCAjwjbCDBhAwEiwAiudBy3jlJeW4vAzqieU59RXrhxtMvbHXgK5UdK0KHtUCtcp6GWd38D0u6BoC76EQAvD_BwE'
gclid10 = dfNavegacion[dfNavegacion["gclid"] == 'CjwKCAjwjbCDBhAwEiwAiudBy3jlJeW4vAzqieU59RXrhxtMvbHXgK5UdK0KHtUCtcp6GWd38D0u6BoC76EQAvD_BwE'].index
# compruebo que me devuelve los 10 indices
gclid10.size
# borramos los indices almacenados en gclid10
dfNavegacion = dfNavegacion.drop(gclid10)


# # Empezamos a procesar la url que contiene mucha informacion

# In[9]:


# Me quedo con las url que no son nulas
serieUrlLanding = dfNavegacion["url_landing"][dfNavegacion["url_landing"].notnull()]
# con la url, utilizamos split=& y con cada fragmento genero una nueva columna
dfNavegacion[['url_base','idUser','uuid_url','camp','adg','device','sl','adv','rec','vacia' ]] = (
    serieUrlLanding.str.split(pat="&",n=10, expand=True))


# In[10]:


dfNavegacion.columns


# In[11]:


dfNavegacion.shape


# In[12]:


# Eliminar las columnas que no necesitamos: idUser, uuid_url, rec, vacia   axis=1
dfNavegacion = dfNavegacion.drop(['idUser', 'uuid_url', 'rec', 'vacia'], axis= 1)


# In[13]:


# comprobar url_base   url/modelo?parametro-1
dfNavegacion['url_base']
# split por ?  lambda
dfNavegacion['url_base'] = dfNavegacion['url_base'].apply(lambda url: str(url).split('?')[0])  # url/modelo
dfNavegacion['url_base'] 


# In[14]:


# buscar la posicion de la ultima /    funcion obtenerModelo
# nos quedamos con el modelo y generamos columna modelo 
def obtenerModelo(url):
    posicion = url.rfind('/')  # busca posicion del ultimo / de la url 
    modelo = url[posicion + 1:]
    if modelo == '' or modelo == 'renting':
        modelo = 'home'
    return modelo
    
dfNavegacion.insert(loc=7, column='modelo', value= dfNavegacion['url_base'].apply(obtenerModelo))    
print(dfNavegacion['modelo'].head(50))


# # Crear un orden de usuarios. Como tenemos usuarios repetidos me daria un problema al hacer el merge con conversiones.csv

# In[15]:


# Crear una columna llamada orden que almacene el orden de los id_user
dfNavegacion = dfNavegacion.sort_values(['id_user','ts'])
dfNavegacion.insert(loc=1, column='orden', value=dfNavegacion.groupby('id_user')['ts'].cumcount())


# In[21]:


# Filtrar por orden = 0
dfNavegacion = dfNavegacion[dfNavegacion['orden'] == 0]
dfNavegacion['orden'].head(50)


# # Empezamos a procesar conversiones.csv

# In[19]:


# crear dfConversiones
dfConversiones = pd.read_csv("archivos_practica/conversiones.csv", sep=";")
dfConversiones


# In[20]:


# hacer el merge por id_user con modo outer para no perder nada de informacion
dfFinal = pd.merge(dfNavegacion, dfConversiones, how='outer', on=['id_user'])
dfFinal


# In[23]:


# Crear una nueva columna conversiones donde colocais:
# 1 (es conversion), 0 (no es conversion)
# si CALL o FORM es conversion
def esConversion(dato):
    if dato in ['CALL', 'FORM']:
        return 1
    else:
        return 0

dfFinal.insert(loc=1, column='conversiones', value=dfFinal['lead_type'].apply(esConversion))
dfFinal['conversiones'].value_counts().head(50)


# In[26]:


# en el dfFinal borrar las columnas que no se necesitan: orden, url_landing, url_base
dfFinal = dfFinal.drop(['orden', 'url_landing', 'url_base'], axis= 1)
dfFinal.columns


# # Preguntas a responder

# In[27]:


# Cuantas visitas recibe en el dia el cliente?
# En la columna ts esta el dia y hora -> crear una columna solo con el dia
dfFinal.insert(loc=1, column='dia', value=dfFinal['ts'].apply(lambda ts: str(ts).split(' ')[0]))
dfFinal.groupby('dia')['dia'].count()


# In[31]:


# Cuantas de ellas convierten y cuantas no? En %
# Filtro solo 6/9/2021
visitas_dia_6_septiembre = dfFinal[dfFinal['dia'] == '2021-09-06']

# Cuento cuantas visitas hubo ese dia
num_visitas_dia = visitas_dia_6_septiembre['dia'].count()

# Cuento las visitas con conversion
visitas_convierten = visitas_dia_6_septiembre[visitas_dia_6_septiembre['conversiones'] == 1]['ts'].count()

# Cuento las visitas sin conversion
visitas_no_convierten = visitas_dia_6_septiembre[visitas_dia_6_septiembre['conversiones'] == 0]['ts'].count()

# Calculo los portentajes
porcentaje_visitas_convierten = round((visitas_convierten / num_visitas_dia) * 100, 2 )
print("% Convierten: ", porcentaje_visitas_convierten)

porcentaje_visitas_no_convierten = round((visitas_no_convierten / num_visitas_dia) * 100, 2 )
print("% No Convierten: ", porcentaje_visitas_no_convierten)


# In[33]:


# Por tipo de conversion (CALL o FORM), Cuantas hay de cada una?
dfFinal.groupby('lead_type')['lead_type'].count()


# In[36]:


# Porcentaje de usuarios recurrentes sobre el total de usuarios
total_usuarios = dfFinal['id_user'].count()
usuarios_recurrentes = dfFinal[dfFinal.user_recurrent & dfFinal.user_recurrent.notnull()]['ts'].count()

porcentaje_usuarios_recurrentes = round((usuarios_recurrentes / total_usuarios) * 100, 2 )
print("% Usuarios recurrentes: ", porcentaje_usuarios_recurrentes)


# In[37]:


# Coche mas visitado
dfFinal['modelo'].value_counts()


# In[39]:


# Cual es el coche que mas convierte?
dfFinal[dfFinal['conversiones'] == 1].groupby('modelo')['conversiones'].count()


# In[40]:


# exportar el dfFinal a excel
dfFinal.to_excel('dfFinal.xlsx', index=False)


# In[ ]:




