-- SQL Server UNION operator -- 

-- Combines the result set from two or multiple tables together while eliminating any duplicates 

-- Both of the select statement must have the same number of columns 
-- columns in both the select statement must have the compatible data types
-- we can define GROUP BY and HAVING clause with each SELECT statement. It's not possible 
-- to use them with the result set. 

-- we can't use ORDER BY clause with individual SELECT statement. We can use it
-- with result set generated from the UNION of both SELECT statements. 


use AdventureWorks2016; 

-- joining both the Person and Employee table based on specific BusinessEntityID and apply UNION operator 

select p.LastName, 
p.FirstName 
FROM Person.Person p 
JOIN HumanResources.Employee e 
ON p.BusinessEntityID = e.BusinessEntityID 
WHERE e.BusinessEntityID = 2 
UNION  
select p.LastName, p.FirstName
FROM Person.Person p JOIN HumanResources.Employee e 
ON p.BusinessEntityID = e.BusinessEntityID 
WHERE e.BusinessEntityID = 2 
UNION 
select p.LastName,
p.FirstName
FROM Person.Person p JOIN HumanResources.Employee e 
ON p.BusinessEntityID = e.BusinessEntityID 
WHERE e.BusinessEntityID = 2 


-- UNION ALL operator will combine the result sets together while preserving any duplicate values 


select p.LastName, 
p.FirstName 
FROM Person.Person p 
JOIN HumanResources.Employee e 
ON p.BusinessEntityID = e.BusinessEntityID 
WHERE e.BusinessEntityID = 2 
UNION ALL  
select p.LastName, p.FirstName
FROM Person.Person p JOIN HumanResources.Employee e 
ON p.BusinessEntityID = e.BusinessEntityID 
WHERE e.BusinessEntityID = 2 
UNION ALL
select p.LastName,
p.FirstName
FROM Person.Person p JOIN HumanResources.Employee e 
ON p.BusinessEntityID = e.BusinessEntityID 
WHERE e.BusinessEntityID = 2 


-- EXCEPT operator 

-- will return the rows from the left-side table which doesn't exist in the right side table 

select ProductID
FROM Production.Product 
EXCEPT 
select ProductID 
FROM Production.ProductDocument 

-- alternative way 

select a.ProductID
FROM Production.Product a 
INNER JOIN Production.ProductDocument b 
ON a.ProductID != b.ProductID 

-- INTERSECT operator 

-- INTERSECT operator will return the rows/records where the rows on the left side or 
-- right side can match 

select ProductID 
FROM Production.Product 
INTERSECT 
select ProductID 
FROM Production.ProductDocument

-- alternative way 

select a.ProductID 
FROM Production.Product a INNER JOIN 
Production.ProductDocument b 
ON a.ProductID = b.ProductID 