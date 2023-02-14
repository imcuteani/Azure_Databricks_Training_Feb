-- SQL Server Top Command with Ties option -- 

-- WITH Ties allows you to return more rows with values that match the last row in the 
--limited result set. WITH TIES may cause more rows to be returned than you specified in the 
-- expression

-- for e.g. if you want to return the most expensive products, then you can use 
-- top 1. However, if two or more products have the same prices as the most expensive product, 
-- then you miss the other most expensive products in the result set. 

use "AdventureWorks2016"
go

-- Using TOP command in tSQL with a constant value 

SELECT TOP 10 
Name,
ListPrice
FROM
Production.Product
ORDER BY 
ListPrice DESC;

select * from Production.Product

-- using TOP to return a % of rows 

SELECT TOP 1 PERCENT 
Name, 
ListPrice
FROM 
Production.Product
ORDER BY 
ListPrice DESC; 

-- using TOP command WITH TIES to include the rows that match the values in the last row 

SELECT TOP 3 WITH TIES 
Name, 
ListPrice
FROM 
Production.Product 
ORDER BY
ListPrice DESC; 

