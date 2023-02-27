# input dataset read through spark.read in Pyspark
textFile = spark.read.text("README.md")
textFile.count()  # count the number of rows in this dataframe
#show the first row in the dataframe 
textFile.first() 
# apply filter to transform the dataframe to return the a new subset of dataframe to define the number of lines containing the word "Spark"
textFile.filter(textFile.value.contains("Spark")).count()   # filter() is the Spark transformation operator and count() is the action operator


