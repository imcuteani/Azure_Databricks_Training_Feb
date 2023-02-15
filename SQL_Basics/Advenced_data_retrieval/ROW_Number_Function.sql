-- Row_Number() in SQL Server 

-- ROW_NUMBER() actually it helps to provide the numbers in a result set sequentially. 
-- from 1 to n based on the user-specified ordering 
-- break the result set into GROUPS and NUMBERS based on the rows to be displayed within 
-- the groups by applying a PARTITION BY clause 

-- PARTITION BY() clause divides the result set into partitions (another term for group of rows)

-- The ROW_NUMBER() function is applied to each partition seperately and reinitialized the row number for each partition 

-- Partition BY() claise is option, if skipped, then ROW_NUMBER() function will treat the whole result set as a single partition 

-- ORDER BY() clause which defines the logical order of the rows within each partition of the result set. The ORDER BY() clause 
-- mandatory because the ROW_NUMBER() function is order sensitive. 

-- OVER() is a method which determines the partitioning and ordering of a rowset before the ROW_NUMBER() function is applied 

use AdventureWorks2016
GO 

select 
ROW_NUMBER() OVER(ORDER BY FirstName) row_num,
FirstName,
LastName,
ModifiedDate 
FROM Person.Person;  

-- Partition BY() clause along with the ORDER BY clause applied with ROW_NUMBER() function. 

-- We used the PARTITION BY clause to divide the Persons table into the partitions by ModifiedDate. 
-- The ROW_NUMBER() was reinitialized when the Modified_Date has changed. 

select FirstName, 
LastName,
ModifiedDate,
ROW_NUMBER() OVER(
    PARTITION BY ModifiedDate
    ORDER BY FirstName
) row_num
FROM Person.Person 
ORDER BY ModifiedDate; 



select FirstName, 
LastName,
ModifiedDate,
ROW_NUMBER() OVER(
    PARTITION BY PersonType
    ORDER BY FirstName
) row_num
FROM Person.Person 
ORDER BY PersonType; 