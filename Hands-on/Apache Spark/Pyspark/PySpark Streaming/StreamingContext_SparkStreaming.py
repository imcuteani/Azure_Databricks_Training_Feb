# StreamingContext class is the main entry point for all streaming functionality. We can create a local StreamingContext with 
# two execution threads and batch interval of 1 second. 

# In PySpark Streaming or Spark Streaming, A StreamingContext class represents the connection to a Spark cluster, 
# can be used to create DStream of various input sources. 
# It can be from any existing SparkContext. 
# After creating and transforming DStreams, the streaming computation can be started and stopped using context.start() and context.stop() respectively. 
# context.awaitTermination() allows the current thread to wait for the termination of the context by stop() or by an exception. 

# sparkContext: SparkContext 
# SparkContext object. 
# batchDuration: int, optional 
# The time interval (in seconds) at which streaming data will be divided into batches. 
# sparkContext is the object initialized with SparkContext class associated with StreamingContext class. 
# checkpoint() - sets the context to periodically checkpoint the DStream operations for master fault-tolerance
# getActiveOrCreate(checkpointPath, setupfunc) -  either return the active StreamingContext. 
# start() - start the execution of streams
# stop(stopSparkContext, stopGracefully) - stop the execution of streams
# textFileStream(directory) - Create an input stream which monitors a hadoop compatible file system for new files and reads them as text files. 
# transform(dstreams, transformfunc) - create a new DStream in which each RDD is generated applying a function on RDDs of the DStreams. 
# union(*dstreams) - Create a unified DStream from multiple DStreams of same type and same slide duration. 


from pyspark import SparkContext 
from pyspark.streaming import StreamingContext 

# create a local streamingContext with two working thread and batch interval of 1 sec 

sc = SparkContext("local[*]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

# Create a DStream which will connect to hostname, port, like localhost 9999 

lines = ssc.socketTextstream("localhost", 9999)

# split the lines into words 
words = lines.flatMap(lambda line: line.split(" "))

# flatMap is one to many DStream operation which creates a new DStream by genrating multiple records from each record in the source DStream. 

# count each word in each batch 
pairs = words.map(lambda word: (word, 1))
wordcounts = pairs.reduceByKey(lambda x, y: x + y)

# print the first ten elements of each RDD generated in this DStream 
wordcounts.pprint()  # which will print a few of the counts of words generated every second 

ssc.start()  # start the computation 
ssc.awaitTermination()  # wait for the computation to terminate 

# Execute PySpark streaming job 

# ./bin/spark-submit examples/src/main/python/streaming/network_wordcount.py localhost 9999
