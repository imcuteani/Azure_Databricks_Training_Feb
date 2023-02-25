-- Horizontal Parititioning divides the a table into multiple tables 
-- which contains the same number of columns but fewer rows. 

CREATE DATABASE PartitioningDB
GO 

ALTER DATABASE PartitioningDB 
ADD FILEGROUP January 
GO 

ALTER DATABASE PartitioningDB 
ADD FILEGROUP February 
GO 

ALTER DATABASE PartitioningDB 
ADD FILEGROUP March 
GO 

ALTER DATABASE PartitioningDB 
ADD FILEGROUP April 
GO 


use PartitioningDB;

SELECT name AS AvailableFileGroups 
FROM sys.AvailableFileGroups
WHERE type = 'FG'