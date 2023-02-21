-- read csv file in serverless sql pool database of Azure synapse analytics DW tables

select top 10 * 
from openrowset(
bulk 'https://pandemicdatalake.blob.core.windows.net/public/curated/covid-19/ecdc_cases/latest/ecdc_cases.csv',
format = 'csv',
parser_version = '2.0',
firstrow = 2 ) as rows


-- External data source 

create external data source covid 
with  ( location = 'https://pandemicdatalake.blob.core.windows.net/public/curated/covid-19/ecdc_cases/latest/ecdc_cases.csv');


-- once we created the data source, we can use that data source and the relative path to the file in OPENROWSET function

select top 10 * 
from openrowset(
 bulk 'latest/ecdc_cases.csv',
 data_source = 'covid',
 format = 'csv',
 parser_version = '2.0',
 firstrow = 2
 ) as rows

 -- read the data from parquet file format using openrowset function in Serverless sql pool dw db

 select top 10 * 
 from openrowset(
 bulk 'https://pandemicdatalake.blob.core.windows.net/public/curated/covid-19/ecdc_cases/latest/ecdc_cases.parquet',
 format = 'parquet') as rows

 -- create external data source for serverless sql pool db

 CREATE EXTERNAL DATA SOURCE nyctlc 
 WITH ( LOCATION = 'https://azureopendatastorage.blob.core.windows.net/nyctlc');

 -- create external file format for serverless sql pool db

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

  select  top 15 * from dbo.taxi;
