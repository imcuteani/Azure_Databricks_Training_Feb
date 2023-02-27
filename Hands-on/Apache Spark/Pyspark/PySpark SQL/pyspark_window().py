# Windowing function in PySpark SQL are used to calculate results such as rank, row_number, dense_rank() etc. 
# over a range of input rows. 

# PySpark Window functions can operate over a group of rows (like fname, partition) and return a single value of every input row. 

# in PySpark SQL, it supports three kinds of window functions 
# ranking functions
# analytic functions 
# aggregate functions 

# ranking functions - row_number(), rank(), dense_rank(), percent_rank(), ntile() etc. 
# analytic functions - cume_dist window function is get cumulative distribution of values within a window partition, lag, lead, 
# aggregate functions - min, max, avg, sum(), first(), last(), stddev() for windowsing operation in PySpark SQL 

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('cgpysparksqllabs').getOrCreate()

sampleData = (("James","Sales",3000), \
... ("Michael","Sales",4500), \
... ("Robert","Sales", 4100), \
... ("Maria","Finance", 4500), \
... ("James","Sales", 3000),\
... ("Scott","Finance",3300),\
... ("Jen","Marketing",3900),\
... ("Jeff","Marketing",2000))
columns = ["employee_name","department","salary"]
df = spark.createDataFrame(data = sampleData, schema = columns)
df.printSchema()
root
 |-- employee_name: string (nullable = true)
 |-- department: string (nullable = true)
 |-- salary: long (nullable = true)

df.show(truncate=False)
+-------------+----------+------+
|employee_name|department|salary|
+-------------+----------+------+
|James        |Sales     |3000  |
|Michael      |Sales     |4500  |
|Robert       |Sales     |4100  |
|Maria        |Finance   |4500  |
|James        |Sales     |3000  |
|Scott        |Finance   |3300  |
|Jen          |Marketing |3900  |
|Jeff         |Marketing |2000  |
+-------------+----------+------+

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number
windowSpec = Window.partitionBy("department").orderBy("salary")
df.withColumn("row_number", row_number().over(windowSpec)).show(truncate=False)
+-------------+----------+------+----------+
|employee_name|department|salary|row_number|
+-------------+----------+------+----------+
|Scott        |Finance   |3300  |1         |
|Maria        |Finance   |4500  |2         |
|Jeff         |Marketing |2000  |1         |
|Jen          |Marketing |3900  |2         |
|James        |Sales     |3000  |1         |
|James        |Sales     |3000  |2         |
|Robert       |Sales     |4100  |3         |
|Michael      |Sales     |4500  |4         |
+-------------+----------+------+----------+

from pyspark.sql.functions import rank
df.withColumn("rank",rank().over(windowSpec)).show()
+-------------+----------+------+----+
|employee_name|department|salary|rank|
+-------------+----------+------+----+
|        Scott|   Finance|  3300|   1|
|        Maria|   Finance|  4500|   2|
|         Jeff| Marketing|  2000|   1|
|          Jen| Marketing|  3900|   2|
|        James|     Sales|  3000|   1|
|        James|     Sales|  3000|   1|
|       Robert|     Sales|  4100|   3|
|      Michael|     Sales|  4500|   4|
+-------------+----------+------+----+

from pyspark.sql.functions import dense_rank
df.withColumn("dense_rank",dense_rank().over(windowSpec)).show()
+-------------+----------+------+----------+
|employee_name|department|salary|dense_rank|
+-------------+----------+------+----------+
|        Scott|   Finance|  3300|         1|
|        Maria|   Finance|  4500|         2|
|         Jeff| Marketing|  2000|         1|
|          Jen| Marketing|  3900|         2|
|        James|     Sales|  3000|         1|
|        James|     Sales|  3000|         1|
|       Robert|     Sales|  4100|         2|
|      Michael|     Sales|  4500|         3|
+-------------+----------+------+----------+

from pyspark.sql.functions import percent_rank
df.withColumn("percent_rank",percent_rank().over(windowSpec)).show()
+-------------+----------+------+------------------+
|employee_name|department|salary|      percent_rank|
+-------------+----------+------+------------------+
|        Scott|   Finance|  3300|               0.0|
|        Maria|   Finance|  4500|               1.0|
|         Jeff| Marketing|  2000|               0.0|
|          Jen| Marketing|  3900|               1.0|
|        James|     Sales|  3000|               0.0|
|        James|     Sales|  3000|               0.0|
|       Robert|     Sales|  4100|0.6666666666666666|
|      Michael|     Sales|  4500|               1.0|
+-------------+----------+------+------------------+


from pyspark.sql.functions import ntile
df.withColumn("ntile",ntile(2).over(windowSpec)).show()
+-------------+----------+------+-----+
|employee_name|department|salary|ntile|
+-------------+----------+------+-----+
|        Scott|   Finance|  3300|    1|
|        Maria|   Finance|  4500|    2|
|         Jeff| Marketing|  2000|    1|
|          Jen| Marketing|  3900|    2|
|        James|     Sales|  3000|    1|
|        James|     Sales|  3000|    1|
|       Robert|     Sales|  4100|    2|
|      Michael|     Sales|  4500|    2|
+-------------+----------+------+-----+

from pyspark.sql.functions import cume_dist
df.withColumn("cume_dist",cume_dist().over(windowSpec)).show()
+-------------+----------+------+---------+
|employee_name|department|salary|cume_dist|
+-------------+----------+------+---------+
|        Scott|   Finance|  3300|      0.5|
|        Maria|   Finance|  4500|      1.0|
|         Jeff| Marketing|  2000|      0.5|
|          Jen| Marketing|  3900|      1.0|
|        James|     Sales|  3000|      0.5|
|        James|     Sales|  3000|      0.5|
|       Robert|     Sales|  4100|     0.75|
|      Michael|     Sales|  4500|      1.0|
+-------------+----------+------+---------+

from pyspark.sql.functions import lag
df.withColumn("lag",lag("salary",2).over(windowSpec)).show()
+-------------+----------+------+----+
|employee_name|department|salary| lag|
+-------------+----------+------+----+
|        Scott|   Finance|  3300|null|
|        Maria|   Finance|  4500|null|
|         Jeff| Marketing|  2000|null|
|          Jen| Marketing|  3900|null|
|        James|     Sales|  3000|null|
|        James|     Sales|  3000|null|
|       Robert|     Sales|  4100|3000|
|      Michael|     Sales|  4500|3000|
+-------------+----------+------+----+

from pyspark.sql.functions import lead
df.withColumn("lead",lead("salary",2).over(windowSpec)).show()
+-------------+----------+------+----+
|employee_name|department|salary|lead|
+-------------+----------+------+----+
|        Scott|   Finance|  3300|null|
|        Maria|   Finance|  4500|null|
|         Jeff| Marketing|  2000|null|
|          Jen| Marketing|  3900|null|
|        James|     Sales|  3000|4100|
|        James|     Sales|  3000|4500|
|       Robert|     Sales|  4100|null|
|      Michael|     Sales|  4500|null|
+-------------+----------+------+----+

windowSpecAgg = Window.partitionBy("department")
from pyspark.sql.functions import col, avg, sum, min, max, row_number
df.withColumn("row",row_number().over(windowSpec)) \
... .withColumn("avg",avg(col("salary")).over(windowSpecAgg)) \
... .withColumn("sum",sum(col("salary")).over(windowSpecAgg)) \
... .withColumn("min",min(col("salary")).over(windowSpecAgg)) \
... .withColumn("max",max(col("salary")).over(windowSpecAgg)) \
... .where(col("row")==1).select("department","avg","sum","min","max").show()
