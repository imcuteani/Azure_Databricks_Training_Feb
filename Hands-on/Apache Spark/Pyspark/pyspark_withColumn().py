#PySpark withColumn() is a transformation function in DataFrame which is used to change the value, 
# convert the datatype 
# of an existing column, create a new column, and change the datatype of an existing column. 

#PySpark withColumnRenamed() function is used to rename the column of a dataframe. 

import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
from pyspark.sql.types import StructType,StructField,StringType,IntegerType
spark = SparkSession.builder.appName('cgpysparkdemo').getOrCreate()
data = [('James','','Smith','1992-03-02','M',3000),
... ('Michael','Rose','','2000-05-19','M',4000),
... ('Robert','','Williams','1978-09-04','M',4500),
... ('Maria','A','Jones','1967-07-04','F',7900)]
columns = ["firstname","middlename","lastname","dob","gender","salary"]
df = spark.createDataFrame(data=data, schema=columns)
df.printSchema()
root
 |-- firstname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- dob: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- salary: long (nullable = true)

df.show(truncate=False)
+---------+----------+--------+----------+------+------+
|firstname|middlename|lastname|dob       |gender|salary|
+---------+----------+--------+----------+------+------+
|James    |          |Smith   |1992-03-02|M     |3000  |
|Michael  |Rose      |        |2000-05-19|M     |4000  |
|Robert   |          |Williams|1978-09-04|M     |4500  |
|Maria    |A         |Jones   |1967-07-04|F     |7900  |
+---------+----------+--------+----------+------+------+

# change the datatype of salary col
df2 = df.withColumn("salary",col("salary").cast("Integer"))
df2.printSchema()
root
 |-- firstname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- dob: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- salary: integer (nullable = true)

df2.show(truncate=False)
+---------+----------+--------+----------+------+------+
|firstname|middlename|lastname|dob       |gender|salary|
+---------+----------+--------+----------+------+------+
|James    |          |Smith   |1992-03-02|M     |3000  |
|Michael  |Rose      |        |2000-05-19|M     |4000  |
|Robert   |          |Williams|1978-09-04|M     |4500  |
|Maria    |A         |Jones   |1967-07-04|F     |7900  |
+---------+----------+--------+----------+------+------+

#update the value of existing column in pyspark df
df3 = df.withColumn("salary",col("salary")*100)
df3.printSchema()
root
 |-- firstname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- dob: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- salary: long (nullable = true)

df3.show(truncate=False)
+---------+----------+--------+----------+------+------+
|firstname|middlename|lastname|dob       |gender|salary|
+---------+----------+--------+----------+------+------+
|James    |          |Smith   |1992-03-02|M     |300000|
|Michael  |Rose      |        |2000-05-19|M     |400000|
|Robert   |          |Williams|1978-09-04|M     |450000|
|Maria    |A         |Jones   |1967-07-04|F     |790000|
+---------+----------+--------+----------+------+------+

# create a new column from an existing col
df4 = df.withColumn("CopiedColumn",col("salary")* -1)
df4.printSchema()
root
 |-- firstname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- dob: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- salary: long (nullable = true)
 |-- CopiedColumn: long (nullable = true)

df5 = df.withColumn("Country", lit("USA"))
df5.printSchema()
root
 |-- firstname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- dob: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- salary: long (nullable = true)
 |-- Country: string (nullable = false)

# create a new column and new value 
df6 = df.withColumn("Country", lit("USA")) \
... .withColumn("anotherColumn",lit("anotherValue"))
df6.printSchema()
root
 |-- firstname: string (nullable = true)
 |-- middlename: string (nullable = true)
 |-- lastname: string (nullable = true)
 |-- dob: string (nullable = true)
 |-- gender: string (nullable = true)
 |-- salary: long (nullable = true)
 |-- Country: string (nullable = false)
 |-- anotherColumn: string (nullable = false)

# rename a col name withColumnRenamed() method
df.withColumnRenamed("dob","DateOfBirth").show(truncate=False)
+---------+----------+--------+-----------+------+------+
|firstname|middlename|lastname|DateOfBirth|gender|salary|
+---------+----------+--------+-----------+------+------+
|James    |          |Smith   |1992-03-02 |M     |3000  |
|Michael  |Rose      |        |2000-05-19 |M     |4000  |
|Robert   |          |Williams|1978-09-04 |M     |4500  |
|Maria    |A         |Jones   |1967-07-04 |F     |7900  |
+---------+----------+--------+-----------+------+------+

#drop column with drop()
df4.drop("CopiedColumn").show(truncate=False)
+---------+----------+--------+----------+------+------+
|firstname|middlename|lastname|dob       |gender|salary|
+---------+----------+--------+----------+------+------+
|James    |          |Smith   |1992-03-02|M     |3000  |
|Michael  |Rose      |        |2000-05-19|M     |4000  |
|Robert   |          |Williams|1978-09-04|M     |4500  |
|Maria    |A         |Jones   |1967-07-04|F     |7900  |
+---------+----------+--------+----------+------+------+
