# Práctica Final: Procesamiento y Análisis de Datos Bibliotecarios (2001-2024)

Este proyecto constituye la práctica integral de la asignatura **Programación en Entornos de Datos**. El objetivo es procesar y analizar una serie histórica de registros de préstamos bibliotecarios distribuidos en múltiples archivos CSV, aplicando técnicas de programación vectorizada para maximizar la eficiencia.

---

## 1. Descripción del Proyecto

La aplicación automatiza la carga y consolidación de datos de lectura de casi un cuarto de siglo (2001-2024). El sistema no solo agrega la información, sino que genera métricas críticas sobre hábitos de lectura, popularidad de títulos y cumplimiento de plazos de devolución.

### Objetivos Clave:
* Consolidación de múltiples fuentes de datos distribuidas por año.
* Análisis de popularidad de libros y autores por periodos temporales.
* Evaluación del rendimiento de lectura por género literario.
* Implementación de un sistema de alertas para devoluciones fuera de plazo.

---

## 2. Tecnologías y Metodología

El desarrollo se ha realizado íntegramente en **Python**, priorizando el uso de la librería **Pandas** para evitar el uso de bucles explícitos sobre los datos, garantizando así la escalabilidad de la solución.



### Optimizaciones Técnicas:
* **Gestión de Memoria:** Uso de tipos de datos eficientes (`int8`, `int16`, `category`) para reducir la carga en RAM al procesar miles de registros simultáneamente.
* **Modularidad:** Separación de la lógica de procesamiento (`practica.py`) de la interfaz de ejecución (`main.py`).
* **Vectorización:** Aplicación de operaciones booleanas y de agregación (`groupby`, `mean`, `count`) sobre columnas completas.

---

## 3. Estructura del Software

El código se organiza de forma funcional para facilitar su mantenimiento:

* **Carga e Ingesta (`createDF` / `loadData`):** Lee archivos anuales, infiere el año desde la cabecera del fichero y normaliza las columnas de nombres, autores y duraciones de préstamo.
* **Métricas de Popularidad:** Identificación del "Libro más prestado" tanto a nivel global como desglosado por año.
* **Análisis de Duración:** Funciones para detectar los géneros y libros más rápidos y lentos de leer, permitiendo entender el comportamiento de los lectores según la temática.
* **Sistema de Alertas:** Detección automática de préstamos que superan los 30 días de duración (`addAlerts`) y generación de estadísticas de reincidencia por usuario.



---

## 4. Funcionalidades Destacadas

### Análisis Temporal
El sistema permite filtrar dinámicamente cualquier estadística por año, permitiendo observar tendencias como el auge de ciertos géneros (Distopía, Ciencia Ficción) o autores a lo largo de las décadas analizadas.

### Gestión de Excesos (`tooLate`)
Una de las partes más complejas del análisis es la métrica de exceso, donde el sistema calcula:
1. Media total de días de retraso en la biblioteca.
2. Identificación de los usuarios con mayor y menor acumulación de días de exceso.

---

## 5. Ejecución y Validación

Para ejecutar el análisis, se debe utilizar la línea de comandos indicando la ruta donde se encuentran los archivos CSV:

```bash
python main.py --path /Data