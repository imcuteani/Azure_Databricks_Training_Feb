-- CREATE Serverless SQL Pool 

DROP DATABASE IF EXISTS uspopulationdemo
GO 

-- Create new database 

CREATE DATABASE uspopulationdemo
GO 

-- CREATE External Data Source 

CREATE EXTERNAL DATA SOURCE AzureOpenData
WITH ( LOCATION = 'https://azureopendatastorage.blob.core.windows.net/')


-- Prepare the SQL View 

DROP VIEW IF EXISTS usPopulationView;
GO 

CREATE VIEW usPopulationView AS 
SELECT 
* 
FROM 
 OPENROWSET(
 BULK 'censusdatacontainer/release/us_population_county/year=20*/*.parquet',
 DATA_SOURCE = 'AzureOpenData', 
 FORMAT = 'PARQUET'
) AS uspv;
