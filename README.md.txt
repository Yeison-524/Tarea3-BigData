# Tarea 3 - Procesamiento Batch con PySpark

**Estudiante:** [Escribe tu nombre aquí]
**Curso:** Big Data (202016911) - UNAD

## Descripción del proyecto
Este repositorio contiene el código fuente en PySpark para el análisis exploratorio del conjunto de datos "Netflix Movies and TV Shows". El script realiza limpieza de datos, cuenta la distribución de películas y series, identifica los 10 países con más producción y analiza la evolución del contenido por año.

## Instrucciones para ejecutar
1. Asegurarse de tener Hadoop y PySpark configurados.
2. Subir el archivo `netflix_titles.csv` a HDFS: `hdfs dfs -put netflix_titles.csv /Tarea3`
3. Ejecutar el script: `python3 netflix_batch.py`