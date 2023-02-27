## Download the Anaconda distribution of Linux 

https://www.anaconda.com/download/#linux

wget https://repo.anaconda.com/archive/Anaconda3-2022.10-Linux-x86_64.sh

source ~/.bashrc -- Conda base will be activated 


# Install pyspark

# Install PySpark using Conda
conda install pyspark


# Install FindSpark


conda install -c conda-forge findspark


# On Jupyter cell, type the following commands


import findspark
findspark.init()
findspark.find()



# Import PySpark
from pyspark.sql import SparkSession

#Create SparkSession
spark = SparkSession.builder.appName('SparkByExamples.com').getOrCreate()

# Data
data = [("Java", "20000"), ("Python", "100000"), ("Scala", "3000")]

# Columns
columns = ["language","users_count"]

# Create DataFrame
df = spark.createDataFrame(data).toDF(*columns)

# Print DataFrame
df.show()

