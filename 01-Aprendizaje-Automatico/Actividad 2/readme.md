# Actividad 2: Predicción de Precios de Airbnb Madrid (Regresión)

Este proyecto desarrolla un flujo de trabajo completo de aprendizaje supervisado para resolver un problema de regresión. El objetivo es predecir la variable continua **price** (precio) de alojamientos vacacionales en la ciudad de Madrid (datos de abril de 2017) basándose en diversas características descriptivas.

**Nota obtenida:** 9,5/10

---

## 1. Descripción del Problema y Datos

La tarea consiste en estimar el precio de una oferta de alojamiento a partir de atributos geográficos, de disponibilidad y de reputación.

### Características del Dataset:
* **Registros:** 13.321 entradas.
* **Variable Objetivo:** `price` (Regresión).
* **Atributos Principales:** * Geográficos: `latitude`, `longitude`, `neighbourhood_group`.
    * Alojamiento: `room_type`, `minimum_nights`.
    * Actividad: `number_of_reviews`, `reviews_per_month`, `availability_365`.
---

## 2. Metodología y Preprocesamiento

Se ha seguido un proceso riguroso de limpieza y transformación de datos utilizando **Pipelines** para asegurar la consistencia en el tratamiento de la información.

### Tratamiento de Datos:
* **Limpieza:** Identificación y tratamiento de datos faltantes mediante imputación simple.
* **Variables Categóricas:** Transformación de datos cualitativos (como `room_type` o barrios) mediante codificación binaria (`OneHotEncoder`).
* **Escalado:** Normalización de los datos numéricos utilizando `StandardScaler` para equilibrar el peso de las variables en los modelos basados en distancia.



---

## 3. Modelos y Entrenamiento

Se han evaluado tres métodos de regresión estudiados en el bloque, comparando su capacidad predictiva mediante validación cruzada ($cv=10$).

### Algoritmos Evaluados:
1.  **Regresión Lineal:** Utilizado como modelo base (*baseline*) de mínimos cuadrados.
2.  **K-Nearest Neighbors (KNN) Regressor:** Basado en la similitud de las características de los alojamientos cercanos.
3.  **Árboles de Decisión (Decision Tree Regressor):** Modelado de relaciones no lineales mediante particiones binarias.

---

## 4. Optimización de Hiperparámetros

Para maximizar el rendimiento, se aplicó **GridSearchCV** sobre los modelos KNN y Árboles de Decisión para encontrar los parámetros óptimos.

* **KNN:** Búsqueda del valor ideal de $K$ (vecinos) entre 1 y 20.
* **Árboles de Decisión:** Ajuste de la profundidad máxima (`max_depth`), nodos hoja máximos (`max_leaf_nodes`) y muestras mínimas para división (`min_samples_split`).

---

## 5. Evaluación de Resultados

El desempeño de los modelos se midió utilizando métricas estándar de regresión: Error Absoluto Medio (MAE), Error Cuadrático Medio (MSE) y el Coeficiente de Determinación ($R^2$).

| Modelo | $R^2$ Promedio (CV=10) |
| :--- | :--- |
| **Árbol de Decisión (Optimizado)** | **~0.50** |
| **KNN (Optimizado)** | **~0.44** |
| **Regresión Lineal** | **~0.17** |



---

## 6. Conclusiones

* **Rendimiento del Modelo:** El **Árbol de Decisión** demostró ser el más eficaz para capturar la variabilidad de los precios en comparación con la Regresión Lineal, que presentó el rendimiento más bajo debido a la naturaleza no lineal de los datos.
* **Importancia del Preprocesamiento:** El uso de Pipelines permitió una gestión eficiente de las variables categóricas de alta cardinalidad (barrios y grupos de vecindad).
* **Análisis Predictivo:** Aunque se logró una mejora significativa mediante la afinación de hiperparámetros, el valor de $R^2$ sugiere que existen factores externos al dataset que influyen fuertemente en la fijación de precios de Airbnb en Madrid.