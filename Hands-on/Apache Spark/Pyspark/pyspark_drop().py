import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import expr
spark = SparkSession.builder.appName('cgpysparklabs').getOrCreate()


data = [("James", "Sales", 3000), \
... ("Michael","Sales", 4500),
... ("Robert", "Sales", 4100), \
... ("James", "Sales", 3000) \
... ]
columns = ["employee_name", "department", "salary"]
df2 = spark.createDataFrame(data = data, schema = columns)
df2.printSchema()
root
 |-- employee_name: string (nullable = true)
 |-- department: string (nullable = true)
 |-- salary: long (nullable = true)

 df2.show(truncate=False)
+-------------+----------+------+
|employee_name|department|salary|
+-------------+----------+------+
|James        |Sales     |3000  |
|Michael      |Sales     |4500  |
|Robert       |Sales     |4100  |
|James        |Sales     |3000  |
+-------------+----------+------+

distinctDF2 = df2.distinct()
print("Distinct count:" +str(distinctDF2.count()))

distinctDF2.show(truncate=False)
+-------------+----------+------+
|employee_name|department|salary|
+-------------+----------+------+
|Michael      |Sales     |4500  |
|James        |Sales     |3000  |
|Robert       |Sales     |4100  |
+-------------+----------+------+

df3 = df2.dropDuplicates()
#print("Distinct count: "+str(df2.count())

print("Distinct count: "+str(df3.count()))
Distinct count: 3
df3.show(truncate=False)
+-------------+----------+------+
|employee_name|department|salary|
+-------------+----------+------+
|Michael      |Sales     |4500  |
|James        |Sales     |3000  |
|Robert       |Sales     |4100  |
+-------------+----------+------+

dropDisDF = df2.dropDuplicates(["department","salary"])
print("Distinct count of department salary: "+str(dropDisDF.count()))
#Distinct count of department salary: 3
>>> dropDisDF.show(truncate=False)
+-------------+----------+------+
|employee_name|department|salary|
+-------------+----------+------+
|James        |Sales     |3000  |
|Robert       |Sales     |4100  |
|Michael      |Sales     |4500  |
