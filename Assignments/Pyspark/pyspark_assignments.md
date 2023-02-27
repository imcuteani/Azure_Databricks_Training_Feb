# Write a program in PySpark dataframe to show the use of OrderBy() and Sort() transformation 

# Hints 

#Create a PySpark dataframe & apply the following transformations

df.sort("column_name1","column_name2").show(truncate=False)
df.sort(("column_name1),col("column_name2)).show(truncate=False)

df.orderBy("column_name1","column_name2").show(truncate=False)

# Write a program in PySpark dataframe to show the fillna() and fill() transformation 