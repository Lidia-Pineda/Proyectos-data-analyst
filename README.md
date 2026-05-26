# Proyectos-data-analyst

¡Bienvenido/a a mi repositorio de proyectos! Este espacio compila los trabajos y análisis prácticos realizados durante mi formación en Análisis de Datos. Aquí encontrarás soluciones a problemas de negocio utilizando Python, SQL y Google Sheets, abarcando desde la limpieza de datos hasta la creación de dashboards interactivos.

##  Tecnologías y Herramientas
* **Python:** Manipulación de datos (Pandas, NumPy) y visualización (Matplotlib, Seaborn).
* **SQL:** Consultas estructuradas, filtrado, agregaciones y unión de tablas (JOINs).
* **Google Sheets:** Análisis exploratorio rápido, tablas dinámicas y reportería.

---

##  Proyectos Incluidos

# Proyecto 1 - Resumen Ejecutivo de Ventas - Walmart (Google Sheets)

## Introducción y Contexto de Negocio
En este proyecto asumí el rol de Analista de Datos para la Dirección Comercial de Walmart. El objetivo principal fue transformar un conjunto de datos brutos de ventas semanales del año 2012 en un **Resumen Ejecutivo estratégico e interactivo**. Este análisis sirve como base para que la dirección tome decisiones fundamentadas sobre ajustes de presupuesto, optimización de inventario y estrategias comerciales.

## Objetivos del Proyecto
* **Limpieza y Preparación:** Tratamiento de datos nulos, eliminación de duplicados y formateo estructurado de fechas y monedas en Google Sheets.
* **Definición de KPIs:** Diseño y cálculo de métricas clave de rendimiento (Ventas totales, promedio semanal, margen de crecimiento y rendimiento por tienda/departamento).
* **Construcción de Dashboard:** Creación de un cuadro de mando interactivo y visualmente atractivo para facilitar la exploración de datos a los *stakeholders*.
* **Comunicación Ejecutiva:** Presentación de conclusiones accionables utilizando la metodología **C-F-I** (Context, Finding, Implication).

## Herramientas y Funciones Utilizadas
* **Tablas Dinámicas y Gráficos:** Para resumir grandes volúmenes de datos y detectar tendencias estacionales rápidamente.
* **Funciones Avanzadas:** Uso de fórmulas de búsqueda y lógica (`VLOOKUP`, `INDEX/MATCH`, `IFERROR`, `SUMIFS`, `COUNTIFS`) para la automatización del reporte.
* **Formatos Condicionales y Filtros Interactivos:** Implementación de segmentadores de datos (*slicers*) para permitir que los usuarios filtren las ventas por fecha o tienda de forma dinámica.

---

## Metodología C-F-I (Ejemplo de Comunicación Ejecutiva)
Para asegurar que los hallazgos técnicos se traduzcan en valor de negocio, el reporte final se estructuró bajo el método C-F-I:

---



# Proyecto 2 - Análisis de Embudo de Conversión y Retención - MercadoLibre (SQL)

## Introducción y Rol
En este proyecto asumí el rol de **Analista de Producto** dentro del equipo de *Crecimiento y Retención (Growth & Retention)* de MercadoLibre. El desafío planteado por el Director de Producto consistió en diagnosticar en qué etapas del proceso de compra se pierden los usuarios y evaluar el comportamiento de su retención a lo largo del tiempo, con el fin de proponer mejoras accionables respaldadas por datos.

## Objetivos del Proyecto
* **Mapeo del Macro Journey:** Construir un embudo de conversión multietapa utilizando consultas avanzadas en SQL.
* **Diagnóstico de Fugas:** Identificar los pasos con mayor caída porcentual (*drop-off*) y segmentar el comportamiento por país, dispositivo y fuente de tráfico.
* **Análisis de Cohortes:** Evaluar la retención de usuarios en ventanas críticas de tiempo (D7, D14, D21, D28) para cuentas creadas en el primer semestre de 2025.
* **Simulación de Impacto:** Estimar el incremento en ingresos o conversión tras proponer optimizaciones en los puntos críticos de fuga.

---

## Estructura y Dataset de la Base de Datos
El análisis se realizó sobre dos tablas principales indexadas:

1. `mercadolibre_funnel`: Registro de eventos cronológicos (Unix timestamp) a nivel de sesión y usuario. Incluye dimensiones como `country`, `device_category`, `platform` y `referral_source`.
2. `mercadolibre_retention`: Tabla de actividad recurrente con métricas de usuarios activos (`active`) y días transcurridos desde su registro (`day_after_signup`).

### El Embudo Analizado (Macro Journey)
La consulta SQL rastrea el comportamiento secuencial de los usuarios a través de 7 etapas críticas:
1. **Descubrimiento** (`first_visit`)
2. **Interés / Consideración** (`select_item` / `select_promotion`)
3. **Intención de Compra** (`add_to_cart`)
4. **Inicio de Compra** (`begin_checkout`)
5. **Información de Envío** (`add_shipping_info`)
6. **Información de Pago** (`add_payment_info`)
7. **Conversión / Compra** (`purchase`)

---

## Técnicas y Conceptos de SQL Aplicados
* **Expresiones de Tabla Comunes (CTEs):** Segmentación y aislamiento secuencial de cada etapa del embudo para mantener un código limpio y optimizado.
* **Funciones de Agregación Condicional:** Uso de `COUNT(DISTINCT case when...)` para calcular usuarios únicos por paso.
* **Análisis de Cohortes:** Agrupación y cálculo de tasas de retención temporal basándose en la diferencia de días (`day_after_signup`).
* **Filtrado Avanzado y Formateo:** Manipulación de variables de tiempo (`DATETIME`) para acotar los periodos del negocio (Enero - Agosto 2025).

---

## Hallazgos Clave e Informe Ejecutivo

### 1. Embudo de Conversión (Periodo: 01/01/2025 - 31/08/2025)
* **Mayor punto de fuga:** *[Ejemplo: Se identificó que el 45% de los usuarios abandonan el embudo entre el "Inicio de Compra" y la "Información de Envío", siendo los dispositivos móviles los más afectados].*
* **Comportamiento geográfico:** *[Ejemplo: Brasil presentó una conversión final 3% más alta que Argentina, impulsada principalmente por tráfico orgánico].*

### 2. Análisis de Retención (Cohortes: 01/01/2025 - 01/06/2025)
* **Retención Crítica:** *[Ejemplo: La retención cae drásticamente en D7 (7 días posteriores al registro) estabilizándose hacia D28, lo que sugiere la necesidad de implementar campañas de reactivación temprana (push notifications)].*

---

##  Archivos en el Repositorio
* `queries_funnel_analysis.sql`: Scripts SQL dedicados al mapeo del embudo, tasas de conversión y segmentaciones de tráfico.
* `queries_retention_cohorts.sql`: Consultas para la construcción de la matriz de cohortes (D7 a D28).
* `informe_ejecutivo_mercadolibre.md`: Resumen con las propuestas de mejora simuladas y presentadas


---


# Proyecto 3 - Movilidad Urbana y Productividad Económica - American Development Bank (Python)

## Introducción y Contexto de Negocio
En este proyecto asumí el rol de **Analista de Datos para el American Development Bank**. El objetivo central fue desarrollar un reporte técnico e integrador para entender cómo la eficiencia de la movilidad urbana (congestión, tiempos de viaje y retrasos) impacta directamente en la productividad económica (PIB per cápita y desempleo) de las principales ciudades del mundo. 

La finalidad última de este análisis es servir como herramienta estratégica para la toma de decisiones del banco al momento de **priorizar inversiones en infraestructura de transporte público y vialidad**, buscando maximizar el bienestar de la población y el crecimiento económico local.

## Objetivos del Proyecto
* **Integración de Fuentes Heterogéneas:** Fusionar datos de tráfico en tiempo real con indicadores socioeconómicos globales de base anual.
* **Procesamiento de Datos a Gran Escala:** Limpiar, estandarizar y agregar registros continuos de tráfico a nivel ciudad-año.
* **Filtrado y Enfoque Temporal:** Consolidar y aislar la información correspondiente al año **2024** para un análisis de coyuntura reciente.
* **Análisis Exploratorio y Visual (EDA):** Identificar correlaciones y patrones visuales entre los embotellamientos y el desarrollo económico.

---

## Fuentes de Datos Utilizadas
El proyecto unifica dos datasets globales de alta relevancia:
1. `tomtom_traffic.csv` (**TomTom Traffic Index**): Datos geolocalizados de tráfico vehicular en tiempo real (mide índices de congestión, retrasos en minutos por cada 10 km y longitud de embotellamientos).
2. `oecd_city_economy.csv` (**OECD Cities**): Indicadores anuales de la Organización para la Cooperación y el Desarrollo Económicos (PIB per cápita, porcentaje de desempleo, población y contaminación por partículas PM2.5).

---

## Tecnologías y Pipeline de Datos (Python)
Para garantizar la reproducibilidad y el orden del análisis, implementé el siguiente flujo de trabajo dentro de un **Jupyter Notebook**:

* **Estructuración y Limpieza (Pandas & NumPy):** Estandarización de nombres de columnas a formatos limpios, conversión y validación de tipos de datos (`DATETIME`, `FLOAT`), y tratamiento de strings en nombres de ciudades para asegurar la compatibilidad entre ambas fuentes.
* **Agregación de Datos:** Reducción de la alta cardinalidad de los registros de TomTom mediante agrupaciones (`.groupby()`) para obtener promedios consolidados por ciudad.
* **Fusión de Datos (Merging):** Combinación de las variables de movilidad y economía mediante cruces relacionales precisos basados en llaves de ciudad y país para el periodo 2024.
* **Visualización de Datos (Seaborn & Matplotlib):** Creación de gráficos de dispersión (*scatter plots*), mapas de calor de correlación y diagramas de distribución para responder preguntas clave como:
  * ¿Qué ciudades presentan alta congestión y baja productividad (prioridades de inversión)?
  * ¿Existe una correlación directa entre el tiempo de retraso vehicular y los niveles de desempleo o PIB?

---

## Preguntas de Negocio Respondidas en el Reporte
* **Ciudades en Alerta:** Identificación de urbes con alta congestión y baja productividad económica (focos rojos de inversión).
* **Casos de Éxito:** Ciudades con movilidad eficiente y economías fuertes (modelos de infraestructura a replicar).
* **Métricas Clave:** Determinación de qué variables de tráfico muestran el impacto más severo en el desarrollo urbano.

---

## Archivos en el Repositorio
* `movilidad_productividad_analysis.ipynb`: Jupyter Notebook con el código documentado paso a paso, la justificación de cada limpieza y el análisis visual.
* `data/`: Carpeta con los datasets originales (`tomtom_traffic.csv` y `oecd_city_economy.csv`).
* `dataset_final_limpio_2024.csv`: Archivo depurado y unificado listo para ser consumido en herramientas de BI (Tableau o Power BI).

