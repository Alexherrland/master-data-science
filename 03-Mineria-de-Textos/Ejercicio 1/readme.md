# Práctica 1: Detección de Entidades Nombradas (NER) en Español

Este proyecto desarrolla la primera práctica de la asignatura Minería de Textos. El objetivo fundamental es utilizar y evaluar un etiquetador de entidades nombradas (Named Entity Recognition) sobre el corpus de referencia CoNLL-2002, analizando errores y proponiendo mejoras mediante reglas heurísticas.

**Nota obtenida:** 10/10

---

## 1. Descripción de la Tarea

La práctica consiste en procesar el archivo `esp.testb` (pertinente al corpus CoNLL-2002) para identificar cuatro tipos de entidades:
* **LOC:** Localizaciones.
* **PER:** Personas.
* **ORG:** Organizaciones.
* **MISC:** Entidades misceláneas.

Se evalúa la capacidad de los modelos de **spaCy** para predecir estas etiquetas comparándolas con las anotaciones de referencia (*Gold Standard*) mediante el script de evaluación oficial `conlleval.py`.

---

## 2. Tecnologías y Formato

* **Librería principal:** spaCy (Modelos `es_core_news_sm` y `es_core_news_lg`).
* **Formato de datos:** IOB2 (Inside, Outside, Beginning).
* **Métricas de evaluación:** Precisión, Recall y Medida-F (F1-score).



---

## 3. Estructura del Repositorio

Siguiendo los requisitos de la práctica, los archivos se organizan de la siguiente manera:

* **Documentación:** `Herrerias_Ramirez_Alex_PR1.pdf` (Memoria detallada con análisis de errores).
* **/codigo:**
    * `practica base.py`: Implementación inicial con el modelo base.
    * `practica_mejorada.py`: Implementación que incluye filtros y reglas heurísticas.
    * `parte_opcional.py`: Código para la evaluación del texto anotado manualmente.
    * `conlleval.py`: Script de evaluación de métricas CoNLL.
    * `esp.testb.txt`: Corpus de test original.

---

## 4. Metodología de Mejora

Tras un análisis inicial de errores donde se detectó que el modelo confundía frecuentemente nombres de instituciones con localizaciones o palabras comunes (Stop Words) con entidades, se implementaron las siguientes mejoras:

1.  **Filtro de Organizaciones:** Diccionario de términos clave (`Ministerio`, `Ayuntamiento`, `Comisión`) para forzar la etiqueta `ORG`.
2.  **Filtro de Instituciones Geográficas:** Corrección de entidades que spaCy etiqueta como `LOC` pero que en el contexto del corpus funcionan como `ORG` (ej. `España` o `China` cuando se refieren a gobiernos).
3.  **Eliminación de falsos positivos:** Uso de una lista de `STOP_WORDS` para descartar palabras funcionales que el modelo etiquetaba erróneamente.

---

## 5. Resultados y Comparativa

La evolución de las métricas demuestra la efectividad de las correcciones manuales sobre el modelo de gran tamaño (`lg`):

| Modelo / Configuración | Exactitud (Accuracy) | Precisión | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- |
| **Modelo Base (lg)** | 94.07% | 59.03% | 64.48% | 61.64% |
| **Modelo Mejorado (lg)** | **94.36%** | **60.49%** | **66.09%** | **63.17%** |

### Análisis por categoría (Modelo Mejorado):
* **PER:** Obtuvo los mejores resultados (F1: ~70%), demostrando que los nombres de personas son los más consistentes.
* **ORG:** Se logró una subida significativa en el Recall (del 55.7% al 64.2%) gracias a los filtros aplicados.
* **MISC:** Continúa siendo la categoría más compleja debido a la ambigüedad de los criterios de etiquetado.

---

## 6. Parte Opcional: Anotación Manual

Se realizó un ejercicio de anotación manual sobre un texto contemporáneo relacionado con tecnología y economía (Google, DeepMind, Larry Page).

* **Resultados:** Se alcanzó una precisión global del **71.43%**.
* **Conclusión:** El modelo funciona con una precisión del 100% en entidades claras como personas y localizaciones, pero requiere de mayor contexto para distinguir entre organizaciones y entidades misceláneas en textos técnicos.

---

## 7. Conclusiones

* El uso de **modelos preentrenados** de spaCy proporciona una base sólida, pero el conocimiento del dominio (heurísticas) es clave para elevar el rendimiento en tareas específicas.
* La **mejora del Recall** en organizaciones valida que las reglas basadas en diccionarios son una solución eficaz para mitigar sesgos de modelos generales.
* El análisis de errores permitió comprender que muchas discrepancias no son fallos del modelo, sino diferencias en el criterio de anotación entre el corpus original (2002) y los modelos modernos.