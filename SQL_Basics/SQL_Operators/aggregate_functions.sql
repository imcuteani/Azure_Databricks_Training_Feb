-- Aggregate Functions -- 

-- These functions are being used to perform the calculation on one or more 
-- values and return a single value. The aggregate function often is used 
-- with the GROUP BY , HAVING clause for the select statement 

-- AVG - calculate the average of the non-null values in the dataset 

-- COUNT - returns the no of rows in a group, including the rows with NULL values

-- MIN - returns the minimum value (lowest) in a set of non-null values 

-- MAX - returns the maximum value (highest) in a set of non-null values 

-- SUM - summation of all non-null values in a set 


use "AdventureWorksLT2019"
GO 

select AVG(UnitPrice) avg_order_price 
FROM 
SalesLT.SalesOrderDetail 


-- COUNT() function 

select COUNT(*) productNumber 
FROM SalesLT.Product 
WHERE ListPrice > 500; 

-- max() function 

select MAX(ListPrice) max_list_price 
FROM SalesLT.Product; 

-- min() function 

select MIN(ListPrice) min_list_price 
FROM SalesLT.Product 

-- SUM() function 

select ProductNumber, 
SUM(ProductID) as total_products 
FROM 
SalesLT.Product 
GROUP BY ProductNumber 
ORDER BY total_products 

-- Distinct() function 

SELECT DISTINCT 
AddressLine1, 
City 
FROM 
SalesLT.Address 
ORDER BY City; 