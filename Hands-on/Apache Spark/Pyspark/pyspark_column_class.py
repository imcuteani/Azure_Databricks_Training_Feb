# pyspark.sql.Column class provides several functions to work with DataFrame to manipulate the column values, 
# evaluate the boolean expressions to filter rows, retrieve a value or part of value from a dataframe column 
# to work with list, map and struct columns. 

# Pyspark Column class represents a single column in a dataframe. 
# it provides functions which are used to manipulate Dataframe columns and rows. 
# provides functions to get a value from  a list of column by index, map value by key & index and finally struct nested column. 

from pyspark.sql.functions import lit 
colObj = lit('pysparklabs')

data = [("James", 25), ("Ann", 30)]
df = spark.createDataFrame(data).toDF("name.fname", "age")
df.printSchema()

# retrieve df columns 

df.select(df.age).show()
df.select(df["age"]).show()
df.select(df["`name.fname`"]).show() 