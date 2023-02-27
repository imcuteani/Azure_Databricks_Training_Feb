# PySpark SQL Aggregate functions are grouped as "agg_funcs" in PySpark. 

# avg - returns the average values in the input column
# collect_list - returns all the values from a input column with duplicates
# collect_set - returns all values from an input column with duplicate values being eliminated
# countDistinct - returns the count of distinct items in a group 
# grouping - indicates whether a given input column is aggregated or not. returns 1 for aggregated or 0 for non-aggregated in the result.
# count - returns the total number of elements in the column
# first - returns the first element in a column 
# last - returns the last element in a column
# kurtosis - returns the kurtosis of the values in the group 
# max - returns the maximum value in a column
# min - return the minimum value of the column
# mean - returns the average values in the column
# skewness - return the skewness of the values in a group
# stddev - returns the standard deviatio of values in the column 
# stddev_samp
# stddev_pop - returns the population standard deviation of the values in the column
# sum - sum of all values in a column
# sumDistinct - return the sum of all distinct values in a column
# variance , var_samp, var_pop  - var_samp() would return the unbiased variance of the values in the column
# var_pop - return the population variance of the values in the column 


import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import approx_count_distinct, collect_list
from pyspark.sql.functions import collect_set,sum,avg,max,countDistinct,count
from pyspark.sql.functions import first,last,kurtosis,min,mean,skewness
from pyspark.sql.functions import stddev,stddev_samp,stddev_pop,sumDistinct
from pyspark.sql.functions import variance,var_samp,var_pop
spark = SparkSession.builder.appName('cgpysparksqlfunc').getOrCreate()
#23/02/02 05:14:09 WARN SparkSession: Using an existing Spark session; only runtime SQL configurations will take effect.
 simpleData = [("James","Sales", 3000),
... ("Michael","Sales",4600),
... ("Robert","Sales",4100),
... ("Maria","Finance",3000),
... ("James","Sales",3000),
... ("Scott","Finance",3300),
... ("Jen","Finance",3400),
... ("Jeff","Marketing",2000)]
schema = ["employee_name","department","salary"]
df = spark.createDataFrame(data=simpleData, schema= schema)
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
|Michael      |Sales     |4600  |
|Robert       |Sales     |4100  |
|Maria        |Finance   |3000  |
|James        |Sales     |3000  |
|Scott        |Finance   |3300  |
|Jen          |Finance   |3400  |
|Jeff         |Marketing |2000  |
+-------------+----------+------+

print("approx_count_distinct: " +str(df.select(approx_count_distinct("salary")).collect()[0][0]))
#23/02/02 05:18:17 WARN package: Truncated the string representation of a plan since it was too large. This behavior can be adjusted by setting 'spark.sql.debug.maxToStringFields'.
#approx_count_distinct: 6
print("avg salary of employees: " +str(df.select(avg("salary")).collect()[0][0]))
avg salary of employees: 3300.0
df.select(collect_list("salary")).show(truncate=False)
+------------------------------------------------+
|collect_list(salary)                            |
+------------------------------------------------+
|[3000, 4600, 4100, 3000, 3000, 3300, 3400, 2000]|
+------------------------------------------------+

df.select(collect_set("salary")).show(truncate=False)
+------------------------------------+
|collect_set(salary)                 |
+------------------------------------+
|[4600, 3000, 4100, 3400, 3300, 2000]|
+------------------------------------+

df2 = df.select(countDistinct("department", "salary"))
df2.show(truncate=False)
+----------------------------------+
|count(DISTINCT department, salary)|
+----------------------------------+
|7                                 |
+----------------------------------+

print("Distinct count of department & salary: "+str(df2.collect()[0][0]))
Distinct count of department & salary: 7
print("count of salary of employees: "+str(df.select(count("salary")).collect()[0][0]))
# count of salary of employees: 8
df.select(first("salary")).show(truncate=False)
+-------------+
|first(salary)|
+-------------+
|3000         |
+-------------+

df.select(last("salary")).show(truncate=False)
+------------+
|last(salary)|
+------------+
|2000        |
+------------+

df.select(kurtosis("salary")).show(truncate=False)
+-------------------+
|kurtosis(salary)   |
+-------------------+
|-0.3407463493780418|
+-------------------+

df.select(max("salary")).show(truncate=False)
+-----------+
|max(salary)|
+-----------+
|4600       |
+-----------+

df.select(min("salary")).show(truncate=False)
+-----------+
|min(salary)|
+-----------+
|2000       |
+-----------+

df.select(mean("salary")).show(truncate=False)
+-----------+
|avg(salary)|
+-----------+
|3300.0     |
+-----------+

df.select(skewness("salary")).show(truncate=False)
+-------------------+
|skewness(salary)   |
+-------------------+
|0.13703328123313688|
+-------------------+

df.select(stddev("salary"),stddev_samp("salary"),stddev_pop("salary")).show(truncate=False)
+-------------------+-------------------+------------------+
|stddev_samp(salary)|stddev_samp(salary)|stddev_pop(salary)|
+-------------------+-------------------+------------------+
|783.7638128197259  |783.7638128197259  |733.143914930759  |
+-------------------+-------------------+------------------+

df.select(sum("salary")).show(truncate=False)
+-----------+
|sum(salary)|
+-----------+
|26400      |
+-----------+

df.select(sumDistinct("salary")).show(truncate=False)

+--------------------+
|sum(DISTINCT salary)|
+--------------------+
|20400               |
+--------------------+

df.select(sum_Distinct("salary")).show(truncate=False)

+--------------------+
|sum(DISTINCT salary)|
+--------------------+
|20400               |
+--------------------+

df.select(variance("salary"),var_samp("salary"),var_pop("salary")).show(truncate=False)
+-----------------+-----------------+---------------+
|var_samp(salary) |var_samp(salary) |var_pop(salary)|
+-----------------+-----------------+---------------+
|614285.7142857143|614285.7142857143|537500.0       |
+-----------------+-----------------+---------------+
