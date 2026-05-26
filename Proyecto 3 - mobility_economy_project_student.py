#!/usr/bin/env python
# coding: utf-8

# ## Introducción
# 
# Como analista de datos, tu objetivo es **evaluar cómo la movilidad urbana se relaciona con la productividad económica en las principales ciudades latinoamericanas**. 
# Para ello trabajarás con datos reales de TomTom Traffic Index y OECD Cities, que deberás limpiar, combinar y analizar para identificar en qué ciudades conviene invertir en infraestructura de transporte.

#  

# ## 🧩 Paso 1: Cargar y explorar
# 
# Antes de limpiar o combinar los datos, es necesario **familiarizarte con la estructura de ambos datasets**.
# En esta etapa, validarás que los archivos se carguen correctamente, conocerás sus columnas y tipos de datos, y detectarás posibles inconsistencias.
# 
# ### 1.1 Carga de datos y vista rápida
# 
# **🎯Objetivo:**
# Importar las librerías necesarias, cargar los archivos CSV en DataFrames y realizar una revisión preliminar para entender su contenido.
# 
# **Instrucciones:**
# - Importa las librerías `pandas`, `numpy`, `seaborn` y `matplotlib.pyplot`.
# - Carga los archivos usando `pd.read_csv()`:
#   - `'/datasets/tomtom_traffic.csv'`
#   - `/datasets/oecd_city_economy.csv` `.
# - Guarda los DataFrames en las variables `traffic` y `eco`.
# - Muestra las primeras 5 filas de cada DataFrame.
# 

# In[2]:


# importar librerías
import pandas as pd
import numpy as nm
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


# cargar archivos
traffic = pd.read_csv('/datasets/tomtom_traffic.csv')
eco = pd.read_csv('/datasets/oecd_city_economy.csv')


# In[4]:


# mostrar las primeras 5 filas de traffic
traffic.head()


# In[5]:


# mostrar las primeras 5 filas de eco
eco.head()


# **Tip:** Si no usas `print()` la tabla se vera mejor.

# 
# ---
# 
# ## 🧩Paso 2: Explorar, limpiar y preparar los datos
# 
# Antes de combinar los datasets, inspecciona su estructura, tipos de datos, columnas y valores faltantes.
# Anota las columnas que necesiten limpieza y luego estandariza los nombres de columnas.
# 
# ### 2.1 Explorar la estructura y tipos de datos
# 
# **🎯Objetivo:**
# Identificar columnas con tipos incorrectos, distribución y nulos, anotar las columnas que requieren conversión.
# 
# **Instrucciones:**
# 
# - Usa `.info()` para conocer la estructura de ambos DataFrames.
# - Muestra los primeros 3 renglones de cada DF.
# - Identifica si los detalles de cada DF estan bien o si requieren correcciones y escribe tus conclusiones en el bloque Markdown.
#   - ¿Hay columnas que requieren conversión?¿ Cuáles son? ¿Que tipo de dato ienen y cuál deberían de tener?
#   - ¿Hay datos ausentes en alguna columna?
# 

# In[6]:


# Examinar la estructura de traffic
traffic.info()
traffic.head(3)


# En la estructura del DF traffic, se observa que:
# - Las columnas `UpdateTimeUTC` y `UpdateTimeUTCWeekAgo` actualmente son de tipo object (texto), pero deberían ser datetime (fecha) porque contiene fechas con formato YYYY-MM-DD.

# In[7]:


# Examinar la estructura de eco
eco.info()
eco.head(3)


# En la estructura del DF eco, se observa que:
# - Las columnas `City GDP/capita`, `Unemployment %`, 'PM2.5 (μg/m³)', 'population' actualmente son de tipo object (texto), pero debería ser float64 o int64 (numérico) ya que representa montos/cantidades.
# 

# ### 2.2 Renombrar columnas
# 
# **🎯Objetivo:**
# Estandarizar los nombres de columnas para evitar errores y facilitar la unión de los datasets.
# 
# **Instrucciones:**
# 
# - Cambia los nombres de las columnas para que tengan el formato `snake_case`.
#     - `Country` → `country`
#     - `UpdateTimeUTC` → `update_time_utc`
# - Verifica que los cambios se hayan aplicado correctamente usando `.columns`.
# 

# In[8]:


# Estandarizar los nombres de las columnas de traffic
#tu código aquí
traffic= traffic.rename(columns={
    'Country': 'country',
    'City': 'city',
    'UpdateTimeUTC': 'update_time_utc',
    'JamsDelay': 'jams_delay',
    'TrafficIndexLive': 'traffic_index_live',
    'JamsLengthInKms': 'jams_length_in_kms',
    'JamsCount': 'jams_count',
    'TrafficIndexWeekAgo': 'traffic_index_week_ago',
    'UpdateTimeUTCWeekAgo': 'update_time_utc_week_ago',
    'TravelTimeLivePer10KmsMins': 'travel_time_live_per_10kms_mins',
    'TravelTimeHistoricPer10KmsMins': 'travel_time_historic_per_10kms_mins',
    'MinsDelay': 'mins_delay'
})
# verificar cambios
traffic.columns


# In[10]:


# Estandarizar los nombres de las columnas de eco
#tu código aquí
eco = eco.rename(columns={
    'Year': 'year',
    'City': 'city',
     'Country': 'country',
    'City GDP/capita': 'city_gdp_capita',
    'Unemployment %': 'unemployment',
    'PM2.5 (μg/m³)': 'pm2_5_ug_m3',
    'Population (M)': 'population_m'
      })
# verificar cambios
eco.columns


# 
# 
# ### 2.3 Corregir formatos numéricos y de fecha
# 
# **🎯Objetivo:**
# Asegurar que las columnas de fechas y valores numéricos estén en formatos correctos para permitir análisis, cálculos y comparaciones precisas.
# 
# **Instrucciones:**
# 
# - Convierte las columnas de fecha de `traffic` a formato `datetime`. Haz el cambio a prueba de errores.
# - En el dataset `eco`, limpia los valores numéricos:
#     - En `city_gdp_capita`: elimina separadores de miles (`.`) y reemplaza las comas (`','`) por puntos (`'.'`) antes de convertir a tipo `float`.
#     - En `unemployment_pct`: elimina el símbolo de porcentaje (`%`) y reemplaza las comas (`','`) por puntos (`'.'`) antes de convertir a tipo `float`.
#     - En `population_m`: reemplaza las comas (`','`) por puntos (`'.'`) antes de convertir a tipo `float`.
# - Finalmente, crea una nueva columna llamada `population` multiplicando `population_m` por 1,000,000 para obtener la población total.
# 
# 

# <details>
# <summary>Haz clic para ver la pista</summary>
# para eliminar símbolos, puedes reemplazarlos por un texto vacío.

# In[11]:


# Convertir las columnas de traffic a tipo fecha con pd.to_datetime()
traffic['update_time_utc'] = pd.to_datetime(traffic["update_time_utc"], errors="coerce")

traffic['update_time_utc_week_ago'] = pd.to_datetime(traffic["update_time_utc_week_ago"], errors="coerce")

# verificar el cambio
traffic.info()


# In[12]:


# Limpia separadores y convierte columnas numéricas en eco
eco['city_gdp_capita'] = (eco['city_gdp_capita']
    .astype(str)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float)
)
eco['unemployment'] = (eco['unemployment']
    .astype(str)
    .str.replace('%', '', regex=False)
    .str.replace(',', '.', regex=False)
    .astype(float)
)
eco['population_m']  = (eco['population_m']
    .astype(str)
    .str.replace(',', '.', regex=False)
    .astype(float)
)

# Calcula la población total en unidades absolutas (Multiplica * 1000000)
eco['population'] = eco['population_m'] * 1_000_000

# verificar el cambio
eco.info()
eco.head(3)


# 
# ---
# 
# ## 🧩Paso 3: Extraer año y filtrar
# 
# Extraer el año permite filtrar la información y trabajar solo con el período más reciente y relevante.
# 
# ### 3.1 Extraer columna año y filtrar 2024
# 
# **🎯Objetivo**
# Identificar el año de cada registro y mantener solo los registros del 2024.
# 
# **Intrucciones**
# 
# - Como el DataFrame `traffic` no tiene una columna de año, utiliza el atributo `.dt.year` sobre su columna de fecha para crear una nueva columna llamada `year`.
# - Filtra las filas donde el año sea **2024**.
# - Utiliza `.copy()` para crear dos nuevos DataFrames (`traffic_2024` y `eco_2024`) para evitar modificar el dataset original.

# In[13]:


# Extraer el año de las fechas en update_time_utc
traffic['year'] = traffic['update_time_utc'].dt.year
# Verificar cambio
traffic.head(3)


# In[14]:


# Filtra los registros del año 2024
traffic_2024 = traffic.query('year == 2024').copy()
eco_2024 = eco.query('year == 2024').copy()

# Revisar dataframes nuevos
display(traffic_2024.head())
display(eco_2024.head())


# 
# ---
# 
# ## 🧩Paso 4: Analizar y resumir datos de movilidad
# 
# Como el dataset de tráfico contiene **múltiples registros por ciudad**. En esta parte, calcularás los promedios anuales por ciudad para simplificar el análisis y obtener una visión más clara de las tendencias generales.
# 
# ### 4.1 Calcular promedios de tráfico por ciudad
# 
# **🎯Objetivo:**
# Obtener una vista consolidada del tráfico promedio por ciudad y año, para analizar patrones generales sin depender de datos diarios.
# 
# **Instrucciones**
# 
# - Agrupa los datos por `city`, `country` y `year`.
# - Calcula el promedio **solo de las métricas de tráfico más relevantes**: como `jams_delay`, `traffic_index_live`, `jams_length_kms`, `jams_count`, `mins_delay`, y tiempos de viaje (`travel_time_live_per_10kms_mins` y `travel_time_hist_per_10kms_mins`).
# - Guarda el resultado como `traffic_city_year_2024`, mantén las columnas como variables (no índices).
# 

# <details>
# <summary>Haz clic para ver la pista</summary>
# Usa ".agg()" para aplicar funciones de promedio. Al final, reinicia el índice para mantener las columnas de la agrupación como variables (no índices).

# In[15]:


# Calcular los  promedios de trafico por ciudad, país y año
traffic_city_year_2024 = (traffic_2024   
    .groupby(['city', 'country', 'year'], as_index=False)
    .agg({
        'jams_delay': 'mean',
        'traffic_index_live': 'mean',
        'jams_length_in_kms': 'mean',
        'jams_count': 'mean',
        'mins_delay': 'mean',
        'travel_time_live_per_10kms_mins': 'mean',
        'travel_time_historic_per_10kms_mins': 'mean'
    })
 )
# Mostrar resultado
traffic_city_year_2024.head()


# ### 🧠 **Momento de reflexión**
# 
# ¡Excelente trabajo hasta aquí!
# 
# Ahora que ya tienes los promedios anuales por ciudad, es momento de **observarlos** con atención.
# 
# Piensa:
# 
# - ¿Cuál crees que tiene el mayor tiempo promedio de tráfico?
# - ¿Será una ciudad de **Europa**, de **Latinoamérica** o de **otra región** del mundo?
# 
# Para descubrirlo, ejecuta esta línea de código:
# 
# `traffic_city_year_2024.sort_values(["jams_delay"], ascending=False)`
# 
# 
# 🔍 Observa qué ciudad aparece en los primeros lugares.
# 
# ¿Te sorprenden los resultados? , ¿Coinciden con lo que imaginabas?

# In[40]:


traffic_city_year_2024.sort_values(["jams_delay"], ascending=False)


# La ciudad con el mayor tiempo promedio de tráfico es Manila, requiriendo más de 27 minutos para recorrer distancia.

# 
# ---
# 
# ## 🧩Paso 5: Unir movilidad y economía
# 
# Combinar datasets te permite analizar cómo se relacionan los indicadores económicos con los de movilidad.
# 
# ### 5.1 Unir tráfico (tabla principal) con indicadores económicos
# 
# **🎯Objetivo:**
# Combinar la información de tráfico y economía en un solo DataFrame para analizar cómo las condiciones económicas se relacionan con la movilidad urbana.
# 
# **Instrucciones**
# - Selecciona solo las **columnas relevantes** de cada dataset (por ejemplo, variables clave de tráfico y de economía).
# - Usa `.copy()` al crear subconjuntos para evitar modificar el dataset original.
# - Une ambos DataFrames y define como **claves de unión** a `city` y `year`.
# - Mantén solo las ciudades y años presentes en ambos datasets.
# - Guarda el resultado en una nueva variable llamada `merged` y muestra las primeras 5 filas.
# 

# <details>
# <summary>Haz clic para ver la pista</summary>
# Aplica una unión de tipo "inner" para mantener las ciudades y años presentes en ambos datasets.

# In[16]:


# Seleccionar columnas clave de tráfico y economía
left_cols = [ 'city',
    'year',
    'country',
    'jams_delay',
    'traffic_index_live',
    'jams_length_in_kms',
    'jams_count',
    'mins_delay',
    'travel_time_live_per_10kms_mins',
    'travel_time_historic_per_10kms_mins']

right_cols = ['city',
    'year',
    'city_gdp_capita',
    'unemployment',
    'population_m',
    'population']

# Usar .copy() para crear los dos nuevos datasets reducidos
traffic_2024_small = traffic_city_year_2024[left_cols].copy()
eco_2024_small = eco_2024[right_cols].copy()

# Unir datasets
merged = pd.merge(
    traffic_2024_small,
    eco_2024_small,
    on=['city', 'year'],
    how='inner'
)

# Mostrar las primeras 5 filas
merged.head()


# 
# ---
# 
# ## 🧩Paso 6: Visualización y análisis de relaciones
# 
# Ahora que tienes un dataset limpio y unificado, es momento de **visualizar patrones**.
# Los gráficos te ayudarán a entender cómo se relacionan las variables económicas con las de movilidad urbana.
# 
# ### 6.1 Visualizar relaciones entre economía y tráfico
# 
# **🎯Objetivo:**
# Analizar visualmente la distribución y la relación entre indicadores de tráfico y economía en 2024, para identificar posibles patrones o tendencias generales entre ambas variables.
# 
# **Instrucciones**
# - Usa las librerías `seaborn` y `matplotlib.pyplot` para generar los gráficos.
# - Visualiza la distribución del **tráfico** (`jams_delay`) mediante:
#     - **Boxplot** → para observar la media, mediana y detectar valores atípicos.
# - Visualiza la distribución de la **economía** (`city_gdp_capita`) mediante:
#     - **Histograma** → para analizar la forma de la distribución y el valor promedio del PIB per cápita.
# - Finalmente, **compara ambas variables**, para observar si existe alguna relación entre ellas, haciendo un solo gráfico de barras donde aparezcan ambos indicadores.
# - Recuerda agregar título y etiquetas a los ejes de tus gráficos.
# - Observa y comenta los patrones, valores extremos o posibles relaciones que identifiques.

# **Tip:** Dentro de los parentesis del boxplot, agrega `showmeans=True` para ver la media en el gráfico.

# In[19]:


# Crear boxplot para observar el comportamiento de los minutos de congestion JamsDelay
# crea tu gráfico
plt.figure(figsize=(8, 5))
sns.boxplot(data=merged, y='jams_delay', showmeans=True)
plt.title('Distribución del retraso por congestión (jams_delay) - 2024')
plt.ylabel('Minutos de retraso')
plt.show()





# In[20]:


# Crear histograma para ver la distribución de la economía (city_gdp_capita)
plt.figure(figsize=(8, 5))
sns.histplot(data=merged, x='city_gdp_capita', bins=20, kde=True)
plt.title('Distribución del PIB per cápita por ciudad - 2024')
plt.xlabel('PIB per cápita (USD)')
plt.ylabel('Frecuencia')
plt.show()


# In[23]:


# Gráfico de barras para comparar jams_delay y city_gdp_capita por ciudad
#merged.plot( ... , y=['jams_delay', 'city_gdp_capita'])
plt.figure(figsize=(8, 5))
merged[['jams_delay', 'city_gdp_capita']].mean().plot(kind='bar')
plt.title('Promedio de jams_delay y city_gdp_capita - 2024')
plt.ylabel('Valor promedio')
plt.xlabel('Indicadores')
plt.xticks(rotation=0)
plt.show()


# **Tip:** Antes del `plt.show()` agrega el código `plt.xticks(rotation=90)` para rotar las etiquetas del eje X en 90 grados.

# ### 🧠 **Reflexiona**
# Excelente trabajo llegando a esta etapa del análisis. Antes de avanzar, revisa tus gráficos, tómate un momento para pensar:
# 
# * ¿Las ciudades con mayor PIB per cápita también presentan más congestión?
# 
# * ¿O sucede lo contrario, o no existe una relación clara?

# Escribe tus comentarios:
# Al comparar esta distribución con los indicadores de congestión, no se observa una relación clara entre mayor PIB per cápita y mayores niveles de tráfico, lo que puede significar que la movilidad urbana puede depender también de factores como infraestructura, transporte público y planeación urbana.

# 
# ---
# 
# ## 🧩Paso 7: Exportar y documentar resultados
# 
# En esta etapa final consolidarás todo tu trabajo: guardarás el dataset limpio y crearás un resumen que documente los resultados del proyecto.
# 
# ### 7.1 Guardar dataset final
# 
# **🎯Objetivo:**
# Generar un CSV limpio, reproducible y con columnas relevantes para análisis posterior.
# 
# **Instrucciones**
# 
# - Exporta el DataFrame `merged` con el nombre: `ladb_mobility_economy_2024_clean.csv`
# - Usa `index=False` para no incluir el índice.
# 

# In[26]:


# Exporta el dataset final como CSV
merged.to_csv("ladb_mobility_economy_2024_clean.csv", index=False)


# Para poder ver o descargar el archivo generado:   
# En el menú lateral que esta a la izquierda, ve hasta la parte de abajo, a la sección de **Exportar dataset** para más información. 

# 
# ---
# 
# ## ✅ Entregables
# 
# 1. **Notebook `.ipynb`** con todas las celdas (código + comentarios).
# 2. **CSV final**: `ladb_mobility_economy_2024_clean.csv`.
# 3. **Resumen ejecutivo breve** en Markdown (3–5 párrafos).
# 

# 
# ---
# 
# # 🧾 Resumen ejecutivo (plantilla)
# 
# > Completa este resumen al finalizar el análisis. Mantén 3–5 párrafos cortos, claros y accionables.
# 
# **Contexto & objetivo:**  
# - Responde la pregunta central del análisis: ¿qué relación existe entre la movilidad urbana (congestión, tiempos de viaje) y la productividad económica (PIB per cápita)?
# - Explica brevemente las variables clave utilizadas y su relevancia para la toma de decisiones.
# 
# **Cobertura de datos:**  
# - Especifica los años analizados, número de ciudades y países incluidos.
# 
# **Metodología (alto nivel):**  
# - Describe los procesos principales: limpieza de datos (formatos, estandarización de columnas).
# - Explica la agregación por ciudad–año y el uso de una unión INNER para integrar tráfico y economía.
# - Menciona las validaciones visuales empleadas (distribuciones, outliers, tendencias generales).
# 
# **Hallazgos iniciales:**  
# - Resume los patrones más importantes entre índices de tráfico y PIB per cápita.
# - Destaca anomalías u outliers que podrían requerir revisión adicional o un análisis más profundo.
# 
# **Recomendaciones**  
# Aterriza los hallazgos en acciones: ciudades prioritarias, necesidad de validar fuentes, requerimiento de análisis adicionales, o propuestas de inversión.
# 
# - ¿Qué ciudad : Bogotá, Lima o Buenos Aires o alguna otra en particular, muestra la mayor correlación significativa entre altos niveles de congestión vehicular y bajos indicadores de productividad económica, sugiriendo ser una ciudad prioritaria para inversión en infraestructura de transporte?
# 

# El análisis combinó datos de movilidad urbana de TomTom con indicadores económicos de Organisation for Economic Co-operation and Development para estudiar la relación entre congestión vehicular y productividad económica en ciudades del mundo durante 2024. Las variables principales fueron jams_delay, traffic_index_live, travel_time_live_per_10kms_mins y city_gdp_capita, además de desempleo y población.
# 
# Primero se limpiaron y estandarizaron los datos: se corrigieron formatos de fechas y números, se homologaron los nombres de columnas en snake_case y se filtró únicamente el año 2024. Después, los datos de tráfico se agruparon por ciudad y año para calcular promedios y se integraron con los indicadores económicos mediante una unión INNER, conservando solo las ciudades presentes en ambos conjuntos.
# 
# Los resultados muestran que no existe una relación lineal clara entre un mayor PIB per cápita y menores niveles de congestión. Algunas ciudades con economías fuertes presentan tráfico intenso, mientras que otras con menor productividad también enfrentan importantes retrasos. Esto sugiere que la movilidad urbana depende también de factores como infraestructura, planeación urbana y calidad del transporte público.
# 
# Entre las ciudades analizadas, Bogotá destaca como la principal candidata para inversión en infraestructura de transporte, ya que combina altos niveles de congestión con indicadores económicos relativamente más bajos. Se recomienda priorizar proyectos de transporte masivo y gestión inteligente del tráfico para mejorar la productividad y el bienestar urbano.

# In[ ]:




