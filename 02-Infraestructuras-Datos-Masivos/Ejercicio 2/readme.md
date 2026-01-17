# Trabajo Práctico 2: Procesamiento de Flujos de Datos con Kafka y Spark Streaming

Este proyecto corresponde a la segunda entrega de la asignatura **Infraestructuras Computacionales para Procesamiento de Datos Masivos**. El trabajo se centra en el diseño e implementación de un sistema de procesamiento de datos en tiempo real (*Stream Processing*) utilizando información de movilidad de la ciudad de Madrid.

**Nota obtenida:** Pendiente de calificación

---

## 1. Descripción y Objetivos

El objetivo principal es construir una arquitectura distribuida que permita la ingesta y el análisis continuo de datos provenientes de la API de Open Data de la EMT (Empresa Municipal de Transportes de Madrid).



### Objetivos clave:
* Implementar un productor de eventos utilizando la librería `kafka-python` para la ingesta de datos desde una API externa.
* Configurar y gestionar un clúster de **Apache Kafka** para la mensajería distribuida.
* Desarrollar un consumidor de datos utilizando **Spark Structured Streaming** para el procesamiento de flujos.
* Realizar transformaciones y agregaciones en tiempo real sobre los datos de los autobuses de Madrid.

---

## 2. Arquitectura del Sistema

La solución se divide en dos componentes tecnológicos fundamentales que interactúan de forma asíncrona:

### Parte 1: Productor de Kafka (Ingesta)
Se encarga de la obtención de datos y su publicación en el sistema de mensajería:
* **Conexión API EMT:** Autenticación y petición de datos a los servicios de movilidad de Madrid.
* **Publicación de Mensajes:** Envío de información en formato JSON hacia un tópico específico de Kafka (`emt-bus-topic`).
* **Control de Flujo:** Implementación de pausas para simular la actualización real de los datos de las paradas y líneas.

### Parte 2: Consumidor Spark Streaming (Procesamiento)
Utiliza el motor de Spark para analizar los datos recibidos desde Kafka de manera ininterrumpida:
* **Lectura de Stream:** Conexión de Spark a Kafka para suscribirse al flujo de datos.
* **Tratamiento de Datos:** Definición de un esquema (`Schema`) para parsear los mensajes JSON y convertirlos en columnas de un DataFrame de streaming.
* **Agregaciones en Tiempo Real:** Cálculo de métricas como el tiempo de espera estimado en las paradas o la densidad de autobuses por línea.
* **Salida de Datos:** Escritura de los resultados procesados en la consola o en memoria para su visualización.



---

## 3. Tecnologías y Herramientas

* **Apache Kafka:** Plataforma de transmisión de eventos distribuida para la ingesta de datos a escala.
* **Apache Spark (Structured Streaming):** Motor de procesamiento de flujo escalable y tolerante a fallos.
* **Python (PySpark):** Lenguaje de programación utilizado para implementar tanto el productor como el consumidor.
* **API EMT Madrid:** Fuente de datos externa que proporciona información en tiempo real sobre el transporte público.

---

## 4. Ejecución del Proyecto

Para el correcto funcionamiento del sistema, se requiere seguir el siguiente flujo de ejecución:
1.  **Arranque de Infraestructura:** Iniciar los servicios de Zookeeper y el servidor de Kafka.
2.  **Lanzamiento del Productor:** Ejecutar el script que consulta la API de la EMT y envía los mensajes al tópico de Kafka.
3.  **Lanzamiento del Consumidor:** Ejecutar la aplicación de Spark Streaming para comenzar a procesar y mostrar los resultados de las agregaciones en pantalla.

---

## 5. Conclusiones Técnicas

* **Desacoplamiento:** El uso de Kafka permite que la ingesta de datos y el procesamiento sean independientes, mejorando la robustez del sistema.
* **Procesamiento Incremental:** Spark Structured Streaming permite tratar los flujos de datos con la misma facilidad que si fueran datos estáticos, aplicando optimizaciones de rendimiento automáticas.
* **Escalabilidad:** La arquitectura diseñada permite añadir más productores o consumidores para manejar incrementos masivos en el volumen de datos de movilidad.