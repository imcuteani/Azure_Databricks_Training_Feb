-- Right Outer Join in SQL Server 

-- using two tables Product table and SalesOrderDetail table 

-- A Right Outer join will include all of the records from the right table in the join clause. 
-- regardless of the matching records in the left table. 
-- using the SQL right outer join, it includes all the rows from the table on the right. 
-- the SQL right outer join includes all of the matching and non-matching rows from the right side table 
-- only the matching records from the left side table 
-- whereas the non-matching records from the left side table will be shown as NULL values 

use AdventureWorksLT2019; 

select a.ProductID, a.Name, b.SalesOrderID 
FROM 
SalesLT.SalesOrderDetail b 
RIGHT OUTER JOIN 
SalesLT.Product a 
ON a.ProductID = b.ProductID 
WHERE a.Color = 'Red'
ORDER BY 1; 

use AdventureWorks2016; 

select a.ProductID, a.Name, b.SalesOrderID 
FROM Sales.SalesOrderDetail b RIGHT OUTER JOIN Production.Product a 
ON a.ProductID = b.ProductID 
WHERE a.Color = 'Red'
ORDER BY 1; 
