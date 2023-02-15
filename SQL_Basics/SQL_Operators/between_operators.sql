-- between operators in SQL server -- 

-- between operator is a logical operator allows to specify a range of values to test 

-- purpose 

-- 1. use column or sql expression to test the between operator 
-- 2. start_expresson and end_expression between the BETWEEN and AND keywords
-- 3. between operator returns true if the expression is to test is >= to the value of 
-- start_expression and <= to the value of end_expression

use "AdventureWorksLT2019"
GO 

select ProductID, 
Name, 
ListPrice
FROM 
SalesLT.Product 
WHERE 
ListPrice BETWEEN 150.55 AND 255.55 
ORDER BY 
ListPrice 


-- NOT BETWEEN operator in SQL Server -- 

select 
ProductID, 
Name, 
ListPrice 
FROM 
SalesLT.Product 
WHERE 
ListPrice NOT BETWEEN 150.55 AND 255.55 
ORDER BY 
ListPrice; 
