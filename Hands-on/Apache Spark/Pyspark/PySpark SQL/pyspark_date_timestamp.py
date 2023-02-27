# In PySpark SQL, we have Date and Timestamp functions available on Dataframe and SQL queries and they work 
# similarly with SQL. 
# Date and time functions are very important functions for PySpark SQL to perform the ETL/ELT operations. 
# PySpark SQL provides different kind of Date and time functions like 
# 1. Date function
# 2. Timestamp function
# 3. Date and Timestamp Window function 
# 
# current_date() - to retrieve the current system date 
# date_format() - to retrieve the date and converts from yyyy-mm-dd format to mm-dd-yyyy format
# to_date() - converts a string to date datatype. Date datatype can be converted to any specific type 
# datediff() - return the difference between two dates 
# months_between() - returns the months between two dates 
# trunc() - truncates the date at a specified unit 
# add_months(), date_add(), date_sub() - add or substract date or month of given input 
# year(), month(), next_day(), week_of_year() , dayofweek(), dayofmonth(), dayofyear()
# current_timestamp() - calculate the current timestamp value 
# to_timestamp() - convert to the timestamp value of given input 
# hour(), minute() and second() 
# 
from pyspark.sql import SparkSession
from pyspark.sql.functions import *
spark = SparkSession.builder.appName('cgpysparksqllabs').getOrCreate()
data = [["1","2020-02-01"],["2","2019-03-01"],["3","2021-03-01"]]
df = spark.createDataFrame(data, ["id","input"])
df.show()
+---+----------+
| id|     input|
+---+----------+
|  1|2020-02-01|
|  2|2019-03-01|
|  3|2021-03-01|
+---+----------+

df.select(current_date().alias("current_date")).show(1)
+------------+
|current_date|
+------------+
|  2023-02-02|
+------------+
only showing top 1 row

df.select(col("input"),date_format(col("input"),"MM-dd-yyyy").alias("date_format")).show()
+----------+-----------+
|     input|date_format|
+----------+-----------+
|2020-02-01| 02-01-2020|
|2019-03-01| 03-01-2019|
|2021-03-01| 03-01-2021|
+----------+-----------+

df.select(col("input"),to_date(col("input"),"yyyy-MM-dd").alias("to_date")).show()
+----------+----------+
|     input|   to_date|
+----------+----------+
|2020-02-01|2020-02-01|
|2019-03-01|2019-03-01|
|2021-03-01|2021-03-01|
+----------+----------+

df.select(col("input"),datediff(current_date(),col("input")).alias("datediff")).show()
+----------+--------+
|     input|datediff|
+----------+--------+
|2020-02-01|    1097|
|2019-03-01|    1434|
|2021-03-01|     703|
+----------+--------+

df.select(col("input"),months_between(current_date(),col("input")).alias("months_between")).show()
+----------+--------------+
|     input|months_between|
+----------+--------------+
|2020-02-01|   36.03225806|
|2019-03-01|   47.03225806|
|2021-03-01|   23.03225806|
+----------+--------------+

df.select(col("input"),trunc(col("input"),"Month").alias("Month_Trunc"),
... trunc(col("input"),"Year").alias("Month_Year"),
... trunc(col("input"),Month).alias("Month_Trunc)).show()
  File "<stdin>", line 3
    trunc(col("input"),Month).alias("Month_Trunc)).show()
                                                        ^

df.select(col("input"),
... trunc(col("input"),"Month").alias("Month_Trunc"),
... trunc(col("input"),"Year").alias("Month_Year"),
... trunc(col("input"),"Month").alias("Month_Trunc")).show()
+----------+-----------+----------+-----------+
|     input|Month_Trunc|Month_Year|Month_Trunc|
+----------+-----------+----------+-----------+
|2020-02-01| 2020-02-01|2020-01-01| 2020-02-01|
|2019-03-01| 2019-03-01|2019-01-01| 2019-03-01|
|2021-03-01| 2021-03-01|2021-01-01| 2021-03-01|
+----------+-----------+----------+-----------+

>>> df.select(col("input"),add_months(col("input"),3).alias("add_months"),
... add_months(col("input"),-3).alias("sub_months"),
... date_add(col("input"),4).alias("date_add"),
... date_sub(col("input"),4).alias("date_sub")).show()
+----------+----------+----------+----------+----------+
|     input|add_months|sub_months|  date_add|  date_sub|
+----------+----------+----------+----------+----------+
|2020-02-01|2020-05-01|2019-11-01|2020-02-05|2020-01-28|
|2019-03-01|2019-06-01|2018-12-01|2019-03-05|2019-02-25|
|2021-03-01|2021-06-01|2020-12-01|2021-03-05|2021-02-25|
+----------+----------+----------+----------+----------+

>>> df.select(col("input"),year(col("input")).alias("year"),
... month(col("input")).alias("month"),
... next_day(col("input"),"Sunday").alias("next_day"),
... weekofyear(col("input")).alias("weekofyear")).show()
+----------+----+-----+----------+----------+
|     input|year|month|  next_day|weekofyear|
+----------+----+-----+----------+----------+
|2020-02-01|2020|    2|2020-02-02|         5|
|2019-03-01|2019|    3|2019-03-03|         9|
|2021-03-01|2021|    3|2021-03-07|         9|
+----------+----+-----+----------+----------+

df.select(col("input"),dayofweek(col("input")).alias("dayofweek"),
... dayofmonth(col("input")).alias("dayofmonth"),
... dayofyear(col("input")).alias("dayofyear")).show()
+----------+---------+----------+---------+
|     input|dayofweek|dayofmonth|dayofyear|
+----------+---------+----------+---------+
|2020-02-01|        7|         1|       32|
|2019-03-01|        6|         1|       60|
|2021-03-01|        2|         1|       60|
+----------+---------+----------+---------+
  