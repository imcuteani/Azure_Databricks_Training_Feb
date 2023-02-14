-- Group By Clause in SQL Server 

-- GROUP BY clause allows to arrange the rows for a query of groups. These groups 
-- are determined by the columns specified in the GROUP BY clause

use "AdventureWorksLT2019"
GO 

-- GROUP BY clause is utilized with the SELECT statements 
-- GROUP BY clause aggregates the results on the basis of columns - COUNT, MIN, MAX, SUM and AVG 
-- GROUP BY clause returns only one result per group of data
-- GROUP BY clause always follows the WHERE clause 
-- GROUP BY clause always precedes the ORDER BY clause 

-- The IN operator is a logical operator which allows to test whether a specified value matches with any values in a list 

select 
CustomerID,
SalesPerson,
CompanyName,
Phone, 
ModifiedDate
FROM SalesLT.Customer
WHERE CustomerID IN (12, 29, 30, 40)
GROUP BY 
CustomerID,
SalesPerson,
CompanyName,
Phone,
ModifiedDate
ORDER BY 
CustomerID 