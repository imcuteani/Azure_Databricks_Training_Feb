-- INNER JOIN in SQL Server 

-- allows to combine the data from more than one table at the same time. 
-- It also provides a filtering capability
-- which combines two tables based on joining criteria specified in the ON clause
-- eliminates any of the rows from both tables which dont meet the criteria 


use AdventureWorksLT2019; 

-- retrieve the ProductID, Name and SalesOrderID combining both of the Product and SalesOrderDetail table 
-- through the ProductID in ON clause and where the Product Color is 'Black' 

select a.ProductID, a.Name, b.SalesOrderID
FROM 
SalesLT.Product a 
INNER JOIN 
SalesLT.SalesOrderDetail b 
ON a.ProductID = b.ProductID AND a.Color = 'Black';


select a.ProductID, a.Name, b.SalesOrderID, b.UnitPrice, b.ModifiedDate
FROM 
SalesLT.Product a 
INNER JOIN 
SalesLT.SalesOrderDetail b 
ON a.ProductID = b.ProductID AND a.Color = 'Red';


-- Integrate WHERE and ORDER BY clause 

-- retrieve the ProductID, Name, SalesOrderID, UnitPrice from the Product and SalesOrderDetail table
-- where the information is to be retrieved based on the specified modified date value and sorted by Product Name 

select a.ProductID, a.Name, b.SalesOrderID, b.UnitPrice, b.ModifiedDate 
FROM SalesLT.Product a 
INNER JOIN 
SalesLT.SalesOrderDetail b 
ON a.ProductID = b.ProductID 
WHERE b.ModifiedDate = '2008-06-01'
ORDER BY a.Name; 