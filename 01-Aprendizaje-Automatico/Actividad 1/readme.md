# Actividad 1: Clasificación de Alojamientos de Airbnb Madrid

Este proyecto corresponde a la primera actividad evaluable de la asignatura Aprendizaje Automático I. El objetivo principal es realizar un ejercicio completo de clasificación utilizando diferentes algoritmos y técnicas de preprocesamiento de datos sobre un dataset real de Airbnb Madrid (abril de 2017).

**Nota obtenida:** 9/10

---

## 1. Descripción del Problema e Información de los Datos

La tarea consiste en clasificar las ofertas de alojamiento según su tipo, definido en el campo **room_type**, utilizando el resto de las características disponibles en el dataset.

### Detalles del Dataset:
* **Registros:** 13.321.
* **Atributos:** 11 campos (incluyendo ubicación, precio, disponibilidad, número de reseñas, etc.).
* **Variable Objetivo:** `room_type` (Clases: Entire home/apt, Private room, Shared room).

---

## 2. Tecnologías y Metodología Aplicada

El desarrollo se ha realizado en un entorno de **Jupyter Notebook** utilizando la librería **Scikit-Learn**. Se han aplicado las siguientes técnicas:

### Estudio Estadístico y Limpieza
* Análisis de distribución de clases, identificando un fuerte desbalanceo (predominio de casas enteras frente a habitaciones compartidas).
* Tratamiento de datos faltantes mediante imputación simple.
* Codificación de variables categóricas (`OneHotEncoder` para vecindarios y `LabelEncoder` para la etiqueta objetivo).
* Escalado de datos numéricos mediante `StandardScaler` y `MinMaxScaler`.

### Implementación de Pipelines
Se utilizaron **Pipelines** y **ColumnTransformer** para asegurar la reproducibilidad del preprocesamiento y evitar la fuga de datos (*data leakage*) durante la validación.

---

## 3. Algoritmos de Clasificación Utilizados

Se evaluaron y compararon tres métodos fundamentales:

1.  **K-Nearest Neighbors (KNN):** Ajuste del valor óptimo de $K$.
2.  **Árboles de Decisión:** Optimización de la estructura del árbol para prevenir sobreajuste.
3.  **Naive Bayes:** Evaluación exhaustiva de variantes (`GaussianNB`, `BernoulliNB`, `MultinomialNB`, `ComplementNB`) para determinar cuál se adapta mejor a datos mixtos.

---

## 4. Afinación de Hiperparámetros

Se empleó **GridSearchCV** con validación cruzada ($cv=5$ y $cv=10$) para encontrar la mejor configuración de los modelos:

| Modelo | Hiperparámetros Buscados |
| :--- | :--- |
| **KNN** | `n_neighbors` (rango 1-20) |
| **Árbol de Decisión** | `max_leaf_nodes`, `min_samples_split`, `max_depth` |

---

## 5. Resultados y Conclusiones

Tras la evaluación final en el conjunto de test (20% del total de datos), los resultados obtenidos fueron los siguientes:

| Modelo | Exactitud (Accuracy) en Test |
| :--- | :--- |
| **Árbol de Decisión (Afinado)** | **82.85%** |
| **KNN (Afinado)** | **77.67%** |
| **Naive Bayes (Bernoulli)** | **71.89%** |

### Observaciones clave:
* El **Árbol de Decisión** resultó ser el modelo más eficaz, no solo en precisión general sino también en su capacidad para identificar la clase minoritaria gracias al parámetro de balanceo de pesos.
* La fase de **preprocesamiento** fue crítica; el uso de `BernoulliNB` demostró ser superior a otras variantes de Naive Bayes debido a la gran cantidad de columnas binarias generadas por el proceso de One-Hot Encoding.
* Se logró mitigar el impacto del desbalanceo de clases mediante el uso de la métrica de **estratificación** en la división del dataset.