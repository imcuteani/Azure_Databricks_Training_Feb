
 -- Create external data source for external table 

 CREATE EXTERNAL DATA SOURCE nyctlc 
 WITH ( LOCATION = 'https://azureopendatastorage.blob.core.windows.net/nyctlc');

 -- Create external file format  
 CREATE EXTERNAL FILE FORMAT ParquetFormat WITH ( FORMAT_TYPE = PARQUET);
 GO

 -- we can create the external tables which access data on Azure storage account which allows access to users 
 -- with some Azure AD identity or SAS key. 
 -- So, we can create external tables in the same way as we create regular SQL server external tables. 

 CREATE EXTERNAL TABLE taxi ( 
 vendor_id VARCHAR(100) COLLATE Latin1_General_BIN2,
 pickup_datetime DATETIME2,
 dropoff_datetime DATETIME2,
 passenger_count INT,
 trip_distance FLOAT,
 fare_amount FLOAT,
 tip_amount FLOAT,
 tolls_amount FLOAT,
 total_amount FLOAT 
 ) WITH ( 
  LOCATION = 'yellow/puYear=*/puMonth=*/*.parquet',
  DATA_SOURCE = nyctlc,
  FILE_FORMAT = ParquetFormat
  );

  select top 10 * from dbo.taxi