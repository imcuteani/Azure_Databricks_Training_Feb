import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('cgpysparklabs').getOrCreate()
data = [('James','Smith','M', 30),
... ('Anna','Rose','F',31),
... ('Robert','Williams','M',52)]
columns = [("firstname","lastname","gender","salary")]


columns = ["firstname","lastname","gender","salary"]
df = spark.createDataFrame(data=data, schema=columns)
df.show()
+---------+--------+------+------+
|firstname|lastname|gender|salary|
+---------+--------+------+------+
|    James|   Smith|     M|    30|
|     Anna|    Rose|     F|    31|
|   Robert|Williams|     M|    52|
+---------+--------+------+------+

rdd2 = df.rdd.map(lambda x:
... (x[0]+","+x[1],x[2],x[3]*2))
df2 = rdd2.toDF(["name","gender","new_salary"])
df2.show()
+---------------+------+----------+
|           name|gender|new_salary|
+---------------+------+----------+
|    James,Smith|     M|        60|
|      Anna,Rose|     F|        62|
|Robert,Williams|     M|       104|
+---------------+------+----------+


def func1(x):
...     firstName=x.firstname
...     lastName=x.lastname
...     name=firstName+","+lastName
...     gender=x.gender.lower()
...     salary=x.salary*2
...     return (name,gender,salary)
rdd2=df.rdd.map(lambda x: func1(x))


