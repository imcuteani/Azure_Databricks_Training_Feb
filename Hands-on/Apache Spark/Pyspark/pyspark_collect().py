#PySpark RDD/Dataframe collect() is an action operation which is used to retrieve all the elements of the dataset
#to the driver node. We should use the collect() on smaller dataset after filter(), group() etc. 

import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('cgpysparkdemo').getOrCreate()
dept = [("Finance",10), \
... ("Marketing",20),\
... ("Sales",30), \
... ("IT",40)]
deptColumns = ["dept_name", "dept_id"]
deptDF = spark.createDataFrame(data=dept, schema=deptColumns)
deptDF.show(truncate=False)

# Apply Collect() pyspark action
dataCollect = deptDF.collect()
print(dataCollect)

#apply pyspark collect() action after select() transformation
dataCollect = deptDF.select("dept_name").collect()
print(dataCollect)


