-- CROSS JOIN in SQL Server -- 

-- A CROSS JOIN returns all rows for all possible combinations of two tables. 
-- It generates all the rows from the left table which is then combined with all the rows from the right table. 
-- This type of join (cross-join) is also called a Cartesian Product. (A*B)

use AdventureWorks2016; 

select a.BusinessEntityID, b.Name AS Department 
FROM 
HumanResources.Employee as a 
CROSS JOIN 
HumanResources.Department as b; 
