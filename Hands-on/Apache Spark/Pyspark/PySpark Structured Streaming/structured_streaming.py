# In Spark Structured Streaming, the output mode is defined where the processed streamed output data in written out to the external storage. 

# Complete mode - The entire updated Result table will be written to the external storage. It's upto the storage connector to decide how to handle writing of entire table
# Append mode - Only the new rows appended in the Result table since the last trigger will be written to external storage. This is applicable 
# only on the queries where the existing rows in the Result table are not expected to change 
# Update mode - Only the rows which were updated in the Result table since the last trigger will be written to the external storage. In this mode, only the output of the rows
# which have changed since the last trigger exists. If the query doesn't contain aggregations, it'll be equivalent to Append mode. 
# 

# Spark Structured streaming can ensure end to end exactly once semantics under any failure. 
# With Spark Structured streaming, DataFrames and Datasets can represent static, bounded data as well as streaming
# unbounded data. Similar to static datasets/dataframes, we can use common entry point SparkSession to create 
# streaming DataFrames/DataSets from streaming sources and apply the same operations on them as static DataFrames/Datasets. 
# Streaming DataFrames can be created through the DataStreamReader interface which can be returned by SparkSession.readStream() method. 
# The streaming data sources can be file source, Kafka source, socket sources, rate per micro-batch source. 
# Generate the streaming dataframes which are untyped meaning that schema of the DataFrame is not checked at the compile time but only checked at runtime while the query is submitted. 
# To implement it, we can convert the untyped streaming dataframes to typed streaming dataframes using the same methods as static DataFrame. 
# In this following program, we've converted the untyped schema of the dataframe running on PySpark Strucred streaming API to typed schema means the schema of the dataframe running over TCP sockets
# can be checked even at compile time
 
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
spark = SparkSession.builder.appName("cgsparkstreaminglab").getOrCreate()
# 23/02/03 09:38:21 WARN SparkSession: Using an existing Spark session; only runtime SQL configurations will take effect.
socketDF = spark.readStream.format("socket").option("host","localhost").option("port", 9999).load()

from pyspark.sql.functions import StructType
userSchema = StructType().add("name", "string").add("age", "integer")
csvDF = spark.readStream.option("sep",";").schema(userSchema).csv("/home/adminuser")
csvDF = spark.readStream.option("sep",";").schema(userSchema).csv("/home/adminuser/sparkstreaming")
csvDF.printSchema()


