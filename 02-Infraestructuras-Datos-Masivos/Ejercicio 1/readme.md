# Trabajo Práctico 1: Procesamiento de Datos Masivos con PySpark

Este proyecto constituye la primera entrega práctica de la asignatura **Infraestructuras Computacionales para Procesamiento de Datos Masivos**. El objetivo es aplicar los fundamentos de **Apache Spark** mediante su API **PySpark** para el procesamiento distribuido de datos masivos.

**Nota obtenida:** 8.8

---

## 1. Descripción y Objetivos

El trabajo se centra en el desarrollo de soluciones de Big Data utilizando dos componentes clave: el procesamiento programático con **DataFrames** y el análisis declarativo mediante **Spark SQL**.



### Objetivos principales:
* Configuración de sesiones de Spark en entornos basados en la nube como Google Colab.
* Definición manual de esquemas de datos para garantizar la integridad de la información cargada.
* Implementación de transformaciones distribuidas: filtrado, selección y agregación.
* Resolución de problemas de negocio mediante consultas SQL sobre motores de ejecución masiva.

---

## 2. Tecnologías Utilizadas

* **Apache Spark 3.x:** Motor de procesamiento distribuido.
* **PySpark:** Interfaz de Python para Spark.
* **Spark SQL:** Módulo para datos estructurados que optimiza las consultas mediante el motor Catalyst.
* **Google Colab:** Entorno de ejecución de los notebooks.

---

## 3. Estructura del Proyecto

El desarrollo técnico se divide en dos secciones principales integradas en los notebooks adjuntos:

### Parte 1: Manipulación con Spark DataFrames
En esta fase se procesa información de clientes y países para generar reportes regionales:
* **Esquemas Estrictos:** Se definen estructuras `StructType` y `StructField` para cargar `countries.csv` y `clients.csv` con los tipos de datos correctos.
* **Filtrado Regional:** Selección de clientes pertenecientes exclusivamente a España, Francia e Italia.
* **Joins Distribuidos:** Unión de las tablas de clientes y países para asociar nombres geográficos a los registros individuales.
* **Métricas:** Conteo distribuido del número de clientes por cada país.



### Parte 2: Análisis con Spark SQL
Se utiliza un conjunto de datos real sobre subvenciones públicas para realizar un análisis exploratorio avanzado:
* **Registro de Vistas:** El archivo `convocatorias-2020.csv` se registra como una vista temporal para permitir el acceso mediante lenguaje SQL.
* **Consultas de Negocio:**
    * Cálculo de la suma de importes de las ayudas concedidas por Comunidad Autónoma.
    * Identificación de los 10 beneficiarios con mayores cuantías económicas recibidas.
    * Análisis de la distribución de las ayudas según el órgano que las concede.



---

## 4. Conjuntos de Datos

El análisis se nutre de tres fuentes principales en formato CSV:
1.  **countries.csv:** Listado maestro de países e identificadores.
2.  **clients.csv:** Base de datos con información demográfica de clientes.
3.  **convocatorias-2020.csv:** Datos extraídos de la Base de Datos Nacional de Subvenciones en España, que detalla importes, beneficiarios y órganos concedentes.

---

## 5. Conclusiones Técnicas

* **Evaluación Perezosa (Lazy Evaluation):** El uso de Spark permite que las transformaciones solo se ejecuten cuando se solicita una acción, optimizando el plan de ejecución.
* **Eficiencia de SQL:** La integración de SQL en Spark permite realizar análisis complejos de forma declarativa, aprovechando la potencia del motor de optimización Catalyst.
* **Escalabilidad Horizontal:** Al utilizar DataFrames, Spark distribuye los datos en particiones a través de diferentes nodos, permitiendo procesar archivos que superan la capacidad de una sola máquina.