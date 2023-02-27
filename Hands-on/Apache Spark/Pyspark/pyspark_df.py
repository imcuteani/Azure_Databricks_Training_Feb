import pyspark 
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[1]").appName('CGSparkDemo').getOrCreate()
# Create Dataframe in PySpark 
df = spark.createDataFrame([("Scala", 20000), ("Spark", 30000), ("PHP", 25000)])
df.show()  # display the dataframe
#Spark SQL 
df.createOrReplaceTempView("sample_table")
df2 = spark.sql("SELECT _1, _2 FROM sample_table")
df2.show()