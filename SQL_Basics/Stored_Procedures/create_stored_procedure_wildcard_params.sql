-- SQL Server Stored procedure with Parameters using Wildcard 
-- we can use '%' wildcard parameters. 

use AdventureWorks2016
GO 

DROP PROCEDURE dbo.uspGetAddressWildCard
GO

CREATE PROCEDURE dbo.uspGetAddressWildCard @City NVARCHAR(50)
AS 
SELECT * 
FROM Person.Address 
WHERE City LIKE @City + '%'
GO 

-- Invoke the Stored Procedure with Wildcard parameter 

use AdventureWorks2016
GO 

EXEC dbo.uspGetAddressWildCard @City = 'New'
GO  

-- Stored Procedure with Multiple parameters 

DROP PROCEDURE dbo.uspGetMultiParam
GO

CREATE PROCEDURE dbo.uspGetMultipleParam @City NVARCHAR(50) = NULL, 
@AddressLine1 NVARCHAR(60) = NULL
AS 
SELECT * 
FROM Person.Address 
WHERE City = ISNULL(@City, City)
AND AddressLine1 LIKE '%' + ISNULL(@AddressLine1, AddressLine1) +'%'
GO 

-- Invoke/call the stored procedure 

EXEC dbo.uspGetMultipleParam @City = 'Calgary', @AddressLine1 = 'A'
GO 

EXEC dbo.uspGetMultipleParam @City = 'Calgery', @AddressLine1 = 'B'
GO 



