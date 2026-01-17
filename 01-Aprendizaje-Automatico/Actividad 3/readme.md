# Actividad 3: Segmentación de Alojamientos mediante Aprendizaje No Supervisado (Clustering)

Este proyecto desarrolla la tercera actividad evaluable de la asignatura Aprendizaje Automático I. El objetivo es aplicar técnicas de clustering para segmentar los alojamientos de Airbnb en Madrid, identificando grupos con características similares sin depender de una variable objetivo predefinida.

**Nota obtenida:** 8,5/10

---

## 1. Descripción del Problema y Datos

La tarea consiste en agrupar los registros del dataset de Airbnb Madrid basándose en sus atributos físicos, económicos y de actividad. A diferencia de las actividades anteriores, aquí se busca descubrir la estructura intrínseca de los datos.

### Atributos Utilizados:
* **Numéricos:** `latitude`, `longitude`, `price`, `minimum_nights`, `number_of_reviews`, `reviews_per_month`, `calculated_host_listings_count` y `availability_365`.
* **Categóricos:** `neighbourhood_group` y `room_type`, transformados para ser procesados por los algoritmos de distancia.

---

## 2. Preprocesamiento y Reducción de Dimensionalidad

Se implementó un preprocesamiento avanzado para preparar los datos para algoritmos basados en distancias:

* **Tratamiento de Datos:** Imputación de valores faltantes y codificación de variables categóricas mediante `OneHotEncoder`.
* **Escalado:** Uso de `StandardScaler` para normalizar las magnitudes, evitando que variables como el precio dominen sobre la latitud o longitud.
* **PCA (Análisis de Componentes Principales):** Se aplicó reducción de dimensionalidad para facilitar la visualización de los clusters en un plano bidimensional, manteniendo la mayor varianza posible de los datos originales.

---

## 3. Algoritmos de Clustering Aplicados

Se exploraron tres aproximaciones distintas para la segmentación:

### K-Means (Particional)
* Determinación del número óptimo de clusters ($K$) mediante el **Método del Codo (Elbow Method)** y el análisis del **Coeficiente de Silueta**.
* Se identificó que $K=3$ ofrece una segmentación equilibrada entre cohesión y separación.



### Clustering Jerárquico (Aglomerativo)
* Uso de la distancia euclídea y el método de enlace de Ward para construir una jerarquía de grupos.
* Visualización mediante un **Dendrograma** para decidir el nivel de corte óptimo para la creación de clusters.



### DBSCAN (Basado en Densidad)
* Aplicación de un enfoque basado en densidad para identificar grupos de forma arbitraria y detectar puntos de ruido (outliers).
* Ajuste de los parámetros `eps` (radio de vecindad) y `min_samples` para definir la densidad crítica.

---

## 4. Evaluación de Resultados

La calidad de los clusters se evaluó utilizando métricas internas, dado que no se dispone de etiquetas reales:

1.  **Coeficiente de Silueta:** Mide qué tan similar es un objeto a su propio cluster en comparación con otros grupos.
2.  **Índice Calinski-Harabasz:** Evalúa la dispersión interna y la separación entre clusters.

### Comparativa de Modelos:
| Algoritmo | Observaciones |
| :--- | :--- |
| **K-Means** | Ofreció la estructura más clara y fácil de interpretar para la gestión de negocio. |
| **Jerárquico** | Útil para entender la relación de proximidad entre barrios y tipos de alojamiento. |
| **DBSCAN** | Excelente para filtrar ofertas con precios o características atípicas (ruido). |

---

## 5. Conclusiones

* La segmentación reveló patrones geográficos y de precio claros, diferenciando principalmente entre zonas céntricas de alta demanda y zonas periféricas.
* El **aprendizaje no supervisado** permitió validar que la variable `room_type` es uno de los principales diferenciadores en la estructura de los datos, incluso cuando no se usa como etiqueta de entrenamiento.
* La combinación de **PCA** con técnicas de clustering facilitó la interpretación visual de un dataset complejo y multidimensional.