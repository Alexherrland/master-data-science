# Tarea 2: Agrupamiento (Clustering) de Noticias de Newsgroup

Este proyecto corresponde a la segunda práctica evaluable de la asignatura Minería de Textos. El objetivo es aplicar técnicas de aprendizaje no supervisado para agrupar automáticamente una subcolección de documentos del dataset "20 Newsgroups", evaluando la calidad de los grupos frente a una solución de referencia.

**Nota obtenida:** Pendiente de calificación

---

## 1. Descripción del Problema y Datos

La tarea consiste en organizar una subcolección de noticias en grupos temáticos coherentes sin utilizar etiquetas durante el entrenamiento.

### Información del Dataset:
* **Origen:** Subconjunto de la colección *20 Newsgroups* del CMU Text Learning Group.
* **Estructura:** 7 grupos temáticos reales (categorías de noticias).
* **Directorio de datos:** `Corpus-Clustering` (organizado en subcarpetas por temática).

---

## 2. Tecnologías y Herramientas

* **Procesamiento de Lenguaje Natural:** NLTK y **spaCy** (utilizado en la fase de optimización para mejorar la calidad semántica).
* **Extracción de Características:** Scikit-learn (`TfidfVectorizer` y `CountVectorizer`).
* **Modelado:** `KMeans` y `AgglomerativeClustering` (Clustering Jerárquico).
* **Reducción de Dimensionalidad:** LSA (Latent Semantic Analysis) mediante `TruncatedSVD`.

---

## 3. Estructura del Proyecto

* **Memoria:** `HerreriasRamirezAlexPR2.pdf` (Análisis técnico y justificación de resultados).
* **/codigo:**
    * `HerreriasRamirezAlexPR2.ipynb`: Notebook principal con todo el flujo de preprocesamiento, modelado y validación.
    * Scripts de apoyo para la carga y limpieza de los documentos en la carpeta `Corpus-Clustering`.

---

## 4. Metodología y Preprocesamiento

Se implementó un flujo de trabajo iterativo para maximizar la cohesión de los clusters:

1.  **Limpieza Base:** Eliminación de cabeceras de noticias, stop-words, caracteres no alfanuméricos y conversión a minúsculas.
2.  **Representación Vectorial:** Comparativa entre el modelo de bolsa de palabras (Count) y el modelo de peso estadístico (TF-IDF).
3.  **Optimización con spaCy:** Sustitución de la lematización básica por un procesamiento semántico más robusto, lo que resultó en una mejora crítica de las métricas.
4.  **LSA:** Reducción de la dimensionalidad para mitigar el efecto de la "maldición de la dimensionalidad" y mejorar los tiempos de computación.



---

## 5. Comparativa de Algoritmos y Evaluación

Se evaluó el rendimiento utilizando métricas externas que comparan las etiquetas predichas con las categorías reales de las noticias:

| Algoritmo | Representación | ARI (Adj. Rand Index) | NMI (Norm. Mutual Info) |
| :--- | :--- | :--- | :--- |
| **K-Means** | TF-IDF | **0.2798** | **0.4817** |
| **Jerárquico** | TF-IDF | 0.2315 | 0.4421 |

### Análisis de resultados:
* El modelo **K-Means** superó ligeramente al Jerárquico en términos de separación de categorías.
* Las matrices de confusión revelaron que las categorías más difíciles de distinguir son aquellas con terminología técnica compartida.



---

## 6. Parte Opcional: Determinación del K Óptimo

Se realizó un análisis para encontrar el número ideal de clusters ($K$) sin depender de las 7 categorías conocidas:

* **Método aplicado:** Método del Codo (Elbow Method) analizando la inercia del modelo.
* **Resultado:** El punto de inflexión sugirió un valor de **$K=14$**.
* **Conclusión:** Al doblar el número de clusters, el modelo fue capaz de identificar subtemáticas dentro de las categorías principales, manteniendo una Información Mutua Normalizada (NMI) muy sólida.



---

## 7. Conclusiones Generales

* **Impacto del Preprocesamiento:** La transición de NLTK a **spaCy** tuvo un impacto mucho más significativo en la mejora de las métricas que el cambio de algoritmos de clustering, subrayando la importancia de la calidad de los datos de entrada.
* **Eficacia de LSA:** La reducción de dimensionalidad no solo aceleró el proceso, sino que ayudó a consolidar conceptos semánticos, mejorando el Coeficiente de Silueta de los grupos resultantes.
* **Interpretación:** El clustering demostró ser una herramienta eficaz para el descubrimiento de temas, aunque la ambigüedad inherente al lenguaje natural hace que la separación perfecta sea compleja en categorías muy similares.