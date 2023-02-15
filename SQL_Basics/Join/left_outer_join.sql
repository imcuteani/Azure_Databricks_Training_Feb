-- Left Outer Join in SQL Server -- 

-- A left outer join will return all the records from the left side of the table in the join clause. 
-- regardless of the matching records in the right table
-- the left SQL outer join includes the rows where the condition is met including 
-- all of the rows from the table on the left where the condition is not met are defined. 
-- Fields from the right table with no match will be displayed as NULL values 

use AdventureWorksLT2019; 

select a.ProductID, a.Name, b.SalesOrderID 
FROM 
SalesLT.Product a 
LEFT OUTER JOIN 
SalesLT.SalesOrderDetail b 
ON a.ProductID = b.ProductID 
WHERE a.Color = 'Red'
ORDER BY 1; 



