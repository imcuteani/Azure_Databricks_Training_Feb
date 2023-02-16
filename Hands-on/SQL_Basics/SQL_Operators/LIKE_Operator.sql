-- LIKE Operator -- 

-- The SQL Server LIKE operator determines that if a character string matches a specified pattern
-- the pattern can be regular characteristics and wildcard characters. 

-- Patterns - % wildcard %: any string of zero or more characters. 

-- _wildcard: any single character 
-- The {list_of_chars} wildcard -- any single character within the set can be considered 

-- The{^}: any single character not within the specified range. 

use AdventureWorksLT2019 

-- Get all customers last name starts with 'M' 

select CustomerID, 
FirstName, 
LastName 
FROM 
SalesLT.Customer 
WHERE LastName LIKE 'm%'
ORDER BY FirstName; 

-- retrieve the lastname of customer with specific last name pattern 

select CustomerID, 
FirstName, 
LastName
FROM 
SalesLT.Customer 
WHERE 
LastName LIKE 'm%n'
ORDER BY FirstName;  

-- Retrieve the lastname with second character as 'p' -- 

select CustomerID, 
FirstName, 
LastName 
FROM 
SalesLT.Customer 
WHERE 
LastName LIKE '_p%'
ORDER BY 
FirstName; 

-- NOT LIKE Operator -- 

select CustomerID, 
FirstName, 
LastName 
FROM SalesLT.Customer 
WHERE 
LastName NOT LIKE 'A%'
ORDER BY 
FirstName; 

-- The [^ character list of ranges] wildcard 

select CustomerID,
FirstName, 
LastName 
FROM SalesLT.Customer 
WHERE 
LastName LIKE '[^A-H]%'
ORDER BY 
FirstName; 