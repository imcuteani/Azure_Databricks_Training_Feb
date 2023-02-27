# PySpark Structured streaming provides end to end guaranteed low latency framework for structured streams of data processing. 
# In PySpark, the Structured streaming can be implemented by creating a streaming DataFrame which represents text data received from the server listening on port 9999. 
# transform the dataframe to calcuate the wordcounts. 
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode
from pyspark.sql.functions import split
spark = SparkSession.builder.appName("cgpysparkstreaminglab").getOrCreate()
# 23/02/03 07:29:57 WARN SparkSession: Using an existing Spark session; only runtime SQL configurations will take effect.
lines = spark.readStream.format("socket").option("host", "localhost").option("port",9999).load()
# 23/02/03 07:31:49 WARN TextSocketSourceProvider: The socket source should not be used for production applications! It does not support recovery.
words = lines.select(explode(split(lines.value, " ")).alias("word"))
#wordCounts = word.groupBy("word").count()
wordCounts = words.groupBy("word").count()
query = wordCounts.writeStream.outputMode("Complete").format("console").start()


# You need to type the following command in another terminal 

# cd $SPARK_HOME

# ./bin/spark-submit examples/src/main/python/sql/streaming/structured_network_wordcount.py localhost 9999 

# open a new terminal window & run the netcat utility 

# nc -lk 9999 

"Apache Spark"
"Apache Hadoop"

