from pyspark.sql import SparkSession
from pyspark.sql.functions import col, desc

# 1. Iniciar sesión de Spark
spark = SparkSession.builder.appName("NetflixBatchAnalysis").getOrCreate()
spark.sparkContext.setLogLevel("WARN")

# 2. Leer el CSV desde HDFS
file_path = "hdfs://localhost:9000/Tarea3/netflix_titles.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True, escape="\"")

print("\n--- ESQUEMA DEL DATASET ---")
df.printSchema()

print("\n--- TOTAL DE REGISTROS ---")
print(f"Total de títulos: {df.count()}")

# 3. LIMPIEZA DE DATOS
df_clean = df.dropna(subset=["type", "title", "release_year"])

# 4. ANÁLISIS 1: ¿Películas vs Series?
print("\n--- DISTRIBUCIÓN POR TIPO ---")
df_clean.groupBy("type").count().orderBy(desc("count")).show()

# 5. ANÁLISIS 2: Top 10 países
print("\n--- TOP 10 PAÍSES ---")
df_clean.filter(col("country").isNotNull()).groupBy("country").count().orderBy(desc("count")).show(10, truncate=False)

# 6. ANÁLISIS 3: Evolución por año
print("\n--- CONTENIDO POR AÑO (2015+) ---")
df_clean.filter(col("release_year") >= 2015).groupBy("release_year").count().orderBy(desc("release_year")).show()

spark.stop()
