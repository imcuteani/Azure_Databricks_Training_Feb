# PySpark SQL JSON functions are used to query or extract the elements from JSON string of DataFrame column by path. 
# It can be used to convert it to struct, ,map type. 

# PySpark SQL has the following JSON functions available 

# 1. from_json() - converts JSON string into Struct type or Map type
# 2. to_json() - Converts MapType to StructType to json string
# 3. json_tuple() - Extract data from JSON and create them as a new columns. 
# 4. get_json_object() - Extracts JSON element from a JSON string based on json path specified
# 5. schema_of_json() - Create schema string from JSON string


import pyspark
from pyspark.sql import SparkSession,Row

spark = SparkSession.builder.appName('cgpysparksqllabs').getOrCreate()

jsonString = """{"Zipcode":704, "ZipcodeType":"STANDARD","City":"PARIS","State":"PR"}"""
df = spark.createDataFrame([(1, jsonString)],["id", "value"])
df.show(truncate=False)

# Convert json string column to Map type 
from pyspark.sql.types import MapType,StringType
from pyspark.sql.functions import from_json
df2 = df.withColumn("value", from_json(df.value,MapType(StringType(),StringType())))
df2.printSchema()
df2.show(truncate=False)

# to_json() func 
from pyspark.sql.functions import to_json,col 
df2.withColumn("value",to_json(col("value"))).show(truncate=False)

# json_tuple() func
from pyspark.sql.functions import json_tuple 
df.select(col("id"),json_tuple(col("value"),"Zipcode","ZipCodeType","City")).toDF("id","ZipCode","ZipCodeType","City").show(truncate=False)

# get_json_object() func in PySpark SQL 
from pyspark.sql.functions import get_json_object
df.select(col("id"),get_json_object(col("value"),"$.ZipCodeType").alias("ZipCodeType")).show(truncate=False)

from pyspark.sql.functions import schema_of_json,lit
schemaStr=spark.range(1).select(schema_of_json(lit("""{"Zipcode":704, "ZipCodetype":"STANDARD","City":"PARIS","State":"PR"}"""))).collect()[0][0]
print(schemaStr)