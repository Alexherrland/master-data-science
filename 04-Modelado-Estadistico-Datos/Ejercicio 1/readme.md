# Práctica 1: Fundamentos de Modelado Estadístico y Regresión Lineal

Este proyecto recoge la resolución de la primera práctica de la asignatura Modelo Estadístico de Datos. El trabajo se centra en la aplicación de simulaciones en R para contrastar conceptos teóricos, la construcción de modelos de regresión robustos y el análisis crítico de procedimientos automáticos de selección de variables.

**Nota obtenida:** 10/10

---

## 1. Contenidos de la Práctica

La práctica se divide en seis bloques fundamentales que cubren desde la bioestadística hasta la modelización multivariante:

1.  **Relevancia Clínica vs. Significancia Estadística:** Simulación del impacto del tamaño muestral en el p-valor.
2.  **Transformaciones de Estabilización de Varianza:** Estudio de la transformación arcoseno raíz para proporciones.
3.  **Análisis de Curvas ROC:** Justificación teórica de la curva ROC en el modelo binormal.
4.  **Modelización Lineal y Análisis de Residuos:** Construcción de un modelo óptimo sobre el dataset `mtcars`.
5.  **Crítica al Procedimiento Stepwise:** Demostración de cómo la selección automática puede incluir variables irrelevantes.
6.  **Ensayos Clínicos Aleatorizados (ECA):** Definición de las características clave (Aleatorización, Control, Enmascaramiento y Prospectividad).

---

## 2. Tecnologías y Metodología

* **Lenguaje:** R.
* **Librerías principales:** `faraway`, `MASS`, `car`.
* **Enfoque:** Uso de simulaciones de Monte Carlo para demostrar que un resultado estadísticamente significativo ($p < 0.05$) no siempre implica una relevancia clínica práctica cuando el tamaño muestral es excesivamente grande.



---

## 3. Aspectos Destacados del Desarrollo

### Modelización y Selección de Variables
Se aplicó una estrategia de modelización completa para predecir el consumo de combustible (`mpg`):
* **Estrategia de eliminación:** Partiendo de un modelo completo, se utilizó el criterio de información de Akaike (AIC) y la significación de los coeficientes.
* **Modelo Final:** Identificación de las variables con mayor poder explicativo, asegurando la parsimonia del modelo.

### Validación del Modelo (Análisis de Residuos)
Para garantizar la validez de las inferencias, se realizó un diagnóstico exhaustivo de los residuos:
* **Linealidad y Homocedasticidad:** Gráficos de residuos frente a valores ajustados.
* **Normalidad:** Uso de diagramas Q-Q y test de Shapiro-Wilk.
* **Puntos de Influencia:** Identificación de valores atípicos mediante la Distancia de Cook.



---

## 4. Conceptos Teóricos Aplicados

### Curvas ROC y Modelo Binormal
Se justifica matemáticamente por qué en un modelo binormal (donde las poblaciones sana y enferma siguen distribuciones normales), la curva ROC siempre se sitúa por encima de la diagonal principal si las medias difieren, dado que la función de distribución acumulada es monótona creciente.



### Transformación Arcoseno
Análisis de la transformación para una proporción $p$ con tamaño muestral $n$:
$$f(p) = 2 \arcsin(\sqrt{p})$$
Se demuestra que su varianza aproximada es $\frac{1}{n}$, lo que independiza la varianza de la media, cumpliendo el objetivo de estabilización.

---

## 5. Conclusiones

* **Riesgos del Stepwise:** Se comprobó mediante código que los métodos automáticos pueden seleccionar variables sin relación causal real, basándose únicamente en correlaciones accidentales en los datos de entrenamiento.
* **Interpretación de Datos:** La significancia estadística es una herramienta de decisión, pero debe ir siempre acompañada del cálculo del tamaño del efecto para determinar la utilidad real de un hallazgo.
* **Rigurosidad en Regresión:** La construcción de un modelo no finaliza con el ajuste; la validación de las hipótesis de Gauss-Markov mediante el análisis de residuos es lo que determina la fiabilidad del modelo estadístico.