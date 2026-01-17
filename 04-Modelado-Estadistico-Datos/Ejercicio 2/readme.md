# Práctica 2: Modelado Estadístico Avanzado y Análisis de Confusión

Este repositorio contiene la resolución de la segunda práctica de la asignatura Modelo Estadístico de Datos. El proyecto profundiza en modelos de regresión no lineal, técnicas de clasificación supervisada (LDA/QDA) y la identificación de variables de confusión mediante el uso del lenguaje R.

**Nota obtenida:** 8,5/10

---

## 1. Contenidos de la Práctica

La práctica aborda problemas estadísticos complejos divididos en las siguientes áreas:

1.  **Regresión Lineal Múltiple y Diagnóstico:** Modelado de la concentración de alcohol en el dataset `wine` y validación de supuestos.
2.  **Teoría de Verosimilitud:** Justificación de la equivalencia asintótica entre el estadístico Chi-cuadrado de Pearson y el de razón de verosimilitudes.
3.  **Modelos de Poisson:** Análisis de la multicolinealidad en modelos de conteo.
4.  **Regresión Logística:** Interpretación de Odds Ratios y probabilidades de supervivencia según el sexo.
5.  **Análisis Discriminante:** Comparativa práctica entre LDA (Lineal) y QDA (Cuadrático).
6.  **Estudio de la Confusión (Confounding):** Demostración del sesgo en la relación Clase-Supervivencia en el Titanic.

---

## 2. Tecnologías y Librerías

* **Lenguaje:** R.
* **Librerías principales:** `rattle` (dataset wine), `MASS` (LDA/QDA/Stepwise), `car` (diagnóstico de modelos).
* **Metodología:** Uso de IA para la síntesis de conceptos teóricos y optimización de la estructura del código.

---

## 3. Aspectos Destacados del Desarrollo

### Modelización del Dataset 'Wine'
Se desarrolló un modelo para predecir el grado alcohólico basado en análisis químicos:
* **Selección de Variables:** Implementación de un algoritmo Stepwise basado en el AIC para reducir la multicolinealidad.
* **Análisis de Residuos:** Verificación de normalidad, homocedasticidad y detección de puntos de influencia mediante la Distancia de Cook.



### Regresión Logística y Probabilidad
A través de un análisis de regresión logística sobre frecuencias de supervivencia, se cuantificó el impacto del sexo en la probabilidad de sobrevivir, interpretando los coeficientes en términos de log-odds y Odds Ratios.



### Clasificación: LDA vs QDA
Se generó un ejemplo sintético en R donde el Análisis Discriminante Cuadrático (QDA) supera al Lineal (LDA) al trabajar con grupos que presentan matrices de varianza-covarianza claramente distintas, rompiendo el supuesto de homocedasticidad del LDA.



---

## 4. Análisis de la Confusión (The Titanic Case)

Uno de los puntos clave de la práctica es el análisis de la variable de confusión. Se demostró estadísticamente cómo el **Sexo** actúa como un confusor en la relación entre la **Clase** (específicamente la tripulación) y la **Supervivencia**:

* **Efecto Crudo:** El Odds Ratio inicial sugería que la tripulación tenía una supervivencia ínfima.
* **Efecto Ajustado:** Al introducir el sexo en el modelo, el coeficiente cambió en un **88.96%**, revelando que el riesgo real no era pertenecer a la tripulación, sino el elevado porcentaje de hombres en ese grupo.

---

## 5. Conclusiones

* **Multicolinealidad:** Se determinó que la multicolinealidad perfecta es una limitación estructural (rango de la matriz) que afecta a cualquier modelo de regresión, incluido el de Poisson, impidiendo la estimación única de parámetros.
* **Interpretación de Modelos:** El estudio del Titanic subraya la importancia de no realizar inferencias basadas únicamente en modelos crudos, ya que variables omitidas pueden sesgar drásticamente las conclusiones de negocio o investigación.
* **Robustez:** La elección entre modelos lineales y cuadráticos debe basarse en la exploración previa de las varianzas de los grupos para asegurar la capacidad de generalización del clasificador.