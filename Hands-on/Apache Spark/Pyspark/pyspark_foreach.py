# in PySpark, the foreach() is an action operation which is available in RDD. DataFrame can iterate or loop over each element
# in the dataframe, which is similar to for loop with advanced features. 

# when foreach() is applied on pyspark dataframe, it executes a function specified in for each element in the dataframe. 

from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('cgpysparkdemo').getOrCreate()

columns = ["Seqno","Name"]
data = [("1","John Jones"),
...         ("2","Tracy Smith"),
...         ("3","Amy Sander")]
df = spark.createDataFrame(data=data,schema=columns)
df.show()
+-----+-----------+
|Seqno|       Name|
+-----+-----------+
|    1| John Jones|
|    2|Tracy Smith|
|    3| Amy Sander|
+-----+-----------+


# apply foreach transformation as actions on the pyspark dataframe 


accum=spark.sparkContext.accumulator(0)
df.foreach(lambda x:accum.add(int(x.Seqno)))
print(accum.value)

# syntax to apply foreach action on pyspark dataframe 
def f(df):
...     print(df.Seqno)
df.foreach(f)

df.foreach(f)