--ORDER BY clause -- 

use "AdventureWorksLT2019"
GO 

select FirstName, 
MiddleName, 
LastName,
CompanyName,
SalesPerson,
EmailAddress,
Phone 
FROM SalesLT.Customer
ORDER BY FirstName
GO 


-- SQL Server ORDER BY clause allows ordering of columns based on number as specified in the column order 

select FirstName, 
MiddleName, 
LastName,
CompanyName, 
SalesPerson, 
EmailAddress,
Phone 
FROM SalesLT.Customer
ORDER BY 3 DESC 
GO 
