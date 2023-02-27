import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('cgpysparklabs').getOrCreate()

data = [("James","Smith","US","CA"),
... ("Michael","Rose","US","NY"),
... ("Robert","William","UK","London"),
... ("Maria","Brown","US","FL")]
columns = ["firstname","lastname","country","state"]
df = spark.createDataFrame(data=data,schema=columns)
df.show(truncate=False)
+---------+--------+-------+------+
|firstname|lastname|country|state |
+---------+--------+-------+------+
|James    |Smith   |US     |CA    |
|Michael  |Rose    |US     |NY    |
|Robert   |William |UK     |London|
|Maria    |Brown   |US     |FL    |
+---------+--------+-------+------+

df.select("firstname","lastname").show()
+---------+--------+
|firstname|lastname|
+---------+--------+
|    James|   Smith|
|  Michael|    Rose|
|   Robert| William|
|    Maria|   Brown|
+---------+--------+

df.select(df.firstname,df.lastname).show()
+---------+--------+
|firstname|lastname|
+---------+--------+
|    James|   Smith|
|  Michael|    Rose|
|   Robert| William|
|    Maria|   Brown|
+---------+--------+

df.select(df["firstname"],df["lastname"]).show()
+---------+--------+
|firstname|lastname|
+---------+--------+
|    James|   Smith|
|  Michael|    Rose|
|   Robert| William|
|    Maria|   Brown|
+---------+--------+

from pyspark.sql.functions import col
df.select(col("firstname"),col("lastname")).show()
+---------+--------+
|firstname|lastname|
+---------+--------+
|    James|   Smith|
|  Michael|    Rose|
|   Robert| William|
|    Maria|   Brown|
+---------+--------+


df.select(*columns).show()
+---------+--------+-------+------+
|firstname|lastname|country| state|
+---------+--------+-------+------+
|    James|   Smith|     US|    CA|
|  Michael|    Rose|     US|    NY|
|   Robert| William|     UK|London|
|    Maria|   Brown|     US|    FL|
+---------+--------+-------+------+

df.select([col for col in df.columns]).show()
+---------+--------+-------+------+
|firstname|lastname|country| state|
+---------+--------+-------+------+
|    James|   Smith|     US|    CA|
|  Michael|    Rose|     US|    NY|
|   Robert| William|     UK|London|
|    Maria|   Brown|     US|    FL|
+---------+--------+-------+------+

df.select("*").show()
+---------+--------+-------+------+
|firstname|lastname|country| state|
+---------+--------+-------+------+
|    James|   Smith|     US|    CA|
|  Michael|    Rose|     US|    NY|
|   Robert| William|     UK|London|
|    Maria|   Brown|     US|    FL|
+---------+--------+-------+------+

df.select(df.columns[:3]).show(3)
+---------+--------+-------+
|firstname|lastname|country|
+---------+--------+-------+
|    James|   Smith|     US|
|  Michael|    Rose|     US|
|   Robert| William|     UK|
+---------+--------+-------+
#only showing top 3 rows

df.select(df.columns[2:4]).show(3)
+-------+------+
|country| state|
+-------+------+
|     US|    CA|
|     US|    NY|
|     UK|London|
+-------+------+
#only showing top 3 rows

