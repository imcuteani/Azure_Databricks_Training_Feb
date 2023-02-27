 import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col,sum,avg,max
spark = SparkSession.builder.appName('cgpysparklabs').getOrCreate()

sampleData=[("James","Sales","NY",90000,23,10000),
... ("Michael","Sales","CA",86000,25,10000),
... ("Robert","Finance","CA",78000,29,96000),
... ("Maria","Marketing","CA",66000,30,80000)]
schema = ["employee_name","department","state","salary","age","bonus"]
df = spark.createDataFrame(data=sampleData, schema=schema)
df.printSchema()
root
 |-- employee_name: string (nullable = true)
 |-- department: string (nullable = true)
 |-- state: string (nullable = true)
 |-- salary: long (nullable = true)
 |-- age: long (nullable = true)
 |-- bonus: long (nullable = true)

df.show(truncate=False)
+-------------+----------+-----+------+---+-----+
|employee_name|department|state|salary|age|bonus|
+-------------+----------+-----+------+---+-----+
|James        |Sales     |NY   |90000 |23 |10000|
|Michael      |Sales     |CA   |86000 |25 |10000|
|Robert       |Finance   |CA   |78000 |29 |96000|
|Maria        |Marketing |CA   |66000 |30 |80000|
+-------------+----------+-----+------+---+-----+

df.groupBy("department").sum("salary").show(truncate=False)
+----------+-----------+
|department|sum(salary)|
+----------+-----------+
|Sales     |176000     |
|Finance   |78000      |
|Marketing |66000      |
+----------+-----------+

df.groupBy("department").count().show(truncate=False)
+----------+-----+
|department|count|
+----------+-----+
|Sales     |2    |
|Finance   |1    |
|Marketing |1    |
+----------+-----+

df.groupBy("department", "state").sum("salary", "bonus").show(truncate=False)
+----------+-----+-----------+----------+
|department|state|sum(salary)|sum(bonus)|
+----------+-----+-----------+----------+
|Sales     |CA   |86000      |10000     |
|Sales     |NY   |90000      |10000     |
|Marketing |CA   |66000      |80000     |
|Finance   |CA   |78000      |96000     |
+----------+-----+-----------+----------+

df.groupBy("department").agg(sum("salary").alias("sum_salary"),\
... avg("salary").alias("avg_salary"),\
... sum("bonus").alias("sum_bonus"),\
... max("bonus").alias("max_bonus")).show(truncate=False)
+----------+----------+----------+---------+---------+
|department|sum_salary|avg_salary|sum_bonus|max_bonus|
+----------+----------+----------+---------+---------+
|Sales     |176000    |88000.0   |20000    |10000    |
|Finance   |78000     |78000.0   |96000    |96000    |
|Marketing |66000     |66000.0   |80000    |80000    |
+----------+----------+----------+---------+---------+

df.groupBy("department")\
... .agg(sum("salary").alias("sum_salary"),\
... avg("salary").alias("avg_salary"),\
... sum("bonus").alias("sum_bonus"),\
... max("bonus").alias("max_bonus"))\
... .where(col("sum_bonus") >-50000).show(truncate=False)
