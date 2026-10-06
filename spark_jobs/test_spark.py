import sys
import os
from pyspark.sql import SparkSession

# Ensure worker processes use the active virtual environment Python
os.environ["PYSPARK_PYTHON"] = sys.executable
os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable

spark = SparkSession.builder \
    .appName("HelloSpark") \
    .master("local[*]") \
    .config("spark.driver.bindAddress", "127.0.0.1") \
    .config("spark.driver.host", "127.0.0.1") \
    .config("spark.network.timeout", "600s") \
    .config("spark.executor.heartbeatInterval", "60s") \
    .getOrCreate()

data = [("Addis Ababa", 1), ("Bahir Dar", 2), ("Adama", 3)]
df = spark.createDataFrame(data, ["city", "id"])

df.show()
print("Row count:", df.count())

spark.stop()