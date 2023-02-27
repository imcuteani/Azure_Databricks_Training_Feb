# in PySpark, DF the show() can be used to display the contents of the dataframe in a table row and column format. 
# By default, it shows only 20 rows and column values are truncated with 20 chars. 
# pyspark printSchema() can be used to print the schema of the dataframe. 
# 
from pyspark.sql import SparkSession
spark = SparkSession.builder().appName('cgpysparkdemo').getOrCreate()
columns = ["Seqno", "Quote"]
data = [("1", "Be the change that you wish to see the world"), 
        ("2", "Python is the most widely used programming language"),
        ("3", "Spark is the core data transformation engine for data processing"),
        ("4", "Spark works in-memory")]

df = spark.createDataFrame(data, columns)
df.show()