from pyspark.sql.types import StructType,StructField
from pyspark.sql.types import StringType,IntegerType,ArrayType
data = [(("James","","Smith"),["Java","Scala","C++"],"OH","M"),
... (("Anna","Rose",""),["Spark","Java","C++"],"NY","F"),
... (("Maria","A","Jones"),["C++","VB","Python"],"NY","F")]
schema = StructType([
... StructField('name', StructType([
... StructField('firstname',StringType(),True),
... StructFiekd('middlename',StringType(),True),
... StructField('lastname',StringType(),True)])),
...


schema = StructType([
... StructField('name', StructType([
... StructField('firstname', StringType(), True),
... StructField('middlename',StringType(),True),
... StructField('lastname', StringType(), True)])),
... StructField('languages', ArrayType(StringType()), True),
... StructField('state', StringType(), True),
... StructField('gender', StringType(), True)])
df = spark.createDataFrame(data = data, schema = schema)
df.printSchema()
root
 |-- name: struct (nullable = true)
 |    |-- firstname: string (nullable = true)
 |    |-- middlename: string (nullable = true)
 |    |-- lastname: string (nullable = true)
 |-- languages: array (nullable = true)
 |    |-- element: string (containsNull = true)
 |-- state: string (nullable = true)
 |-- gender: string (nullable = true)

df.show(truncate=False)
+-----------------+------------------+-----+------+
|name             |languages         |state|gender|
+-----------------+------------------+-----+------+
|{James, , Smith} |[Java, Scala, C++]|OH   |M     |
|{Anna, Rose, }   |[Spark, Java, C++]|NY   |F     |
|{Maria, A, Jones}|[C++, VB, Python] |NY   |F     |
+-----------------+------------------+-----+------+

df.filter(df.state == "NY").show(truncate=False)
+-----------------+------------------+-----+------+
|name             |languages         |state|gender|
+-----------------+------------------+-----+------+
|{Anna, Rose, }   |[Spark, Java, C++]|NY   |F     |
|{Maria, A, Jones}|[C++, VB, Python] |NY   |F     |
+-----------------+------------------+-----+------+

df.filter(df.state != "NY").show(truncate=False)
+----------------+------------------+-----+------+
|name            |languages         |state|gender|
+----------------+------------------+-----+------+
|{James, , Smith}|[Java, Scala, C++]|OH   |M     |
+----------------+------------------+-----+------+

df.filter(~(df.state == "OH")).show(truncate=False)
+-----------------+------------------+-----+------+
|name             |languages         |state|gender|
+-----------------+------------------+-----+------+
|{Anna, Rose, }   |[Spark, Java, C++]|NY   |F     |
|{Maria, A, Jones}|[C++, VB, Python] |NY   |F     |
+-----------------+------------------+-----+------+
df.filter((df.state == "OH") & (df.gender == "M")).show(truncate=False)
+----------------+------------------+-----+------+
|name            |languages         |state|gender|
+----------------+------------------+-----+------+
|{James, , Smith}|[Java, Scala, C++]|OH   |M     |
+----------------+------------------+-----+------+

df.filter(df.state.startswith("N")).show()
+-----------------+------------------+-----+------+
|             name|         languages|state|gender|
+-----------------+------------------+-----+------+
|   {Anna, Rose, }|[Spark, Java, C++]|   NY|     F|
|{Maria, A, Jones}| [C++, VB, Python]|   NY|     F|
+-----------------+------------------+-----+------+

df.filter(df.state.endswith("H")).show()
+----------------+------------------+-----+------+
|            name|         languages|state|gender|
+----------------+------------------+-----+------+
|{James, , Smith}|[Java, Scala, C++]|   OH|     M|
+----------------+------------------+-----+------+

df.filter(df.state.contains("Y")).show()
+-----------------+------------------+-----+------+
|             name|         languages|state|gender|
+-----------------+------------------+-----+------+
|   {Anna, Rose, }|[Spark, Java, C++]|   NY|     F|
|{Maria, A, Jones}| [C++, VB, Python]|   NY|     F|
+-----------------+------------------+-----+------+

data2 = [(2, "Michael Ross"),(3,"Robert Williams"),(4,"James Cambell"),(5, "Roger Ross")]
df2 = spark.createDataFrame(data = data2, schema = ["id","name"])
df2.filter(df2.name.like("%ross%")).show()
+---+----+
| id|name|
+---+----+
+---+----+

df2.filter(df2.name.rlike("(?i)^*ross$")).show()
+---+------------+
| id|        name|
+---+------------+
|  2|Michael Ross|
+---+------------+
