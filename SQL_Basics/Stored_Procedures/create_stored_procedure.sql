-- Stored Procedure in SQL Server -- 

-- SQL Server Stored Procedure is a batch of statements grouped together as a logical unit and stored in the database. 
-- The Stored procedure in SQL Server accepts the parameters and executes the T-SQL statements in the procedure, returns the result set if any. 

-- Benefits of Stored procedures 

-- 1. It can be modified easily - we can easily modify the code inside the stored procedure without the need to restart or deploying the application. 
-- if the tsql queries are written in the application , if we need to change the logic, we must change the code in the app and deploy it. 

-- 2. Reduced network traffic - when we use stored procedure instead of writing tsql queries at the app level, only the procedure name is passed over the network. 
-- instead of tsql code. 

-- 3. Reusable - stored procedures can be executed by multiple users or multiple clients without the need of writing the code again and again. 

-- 4. Performance - the SQL server stored procedure when executed for the first time, creates a plan and stored it in the buffer pool. 
-- so that, the plan can be reused when it executes the next time. 

-- Variables in Stored procedure provides a way to manipulate, store and pass the data within a stored procedure. 

-- local variable '
-- global variable 

-- local variables are designated by @symbol, create, read, update or delete 
-- global variables are designated by @@symbol, we cant perform create or write to global variables. 

-- @@ERROR -- error code from the last statement executed in the stored procedure 
-- @@IDENTITY -- value of the last identity value inserted in the SQL table within the connection 
-- @@ROWCOUNT -- the number of rows affected by the last executed SQL statement 
-- @@TRANCOUNT -- the number of open SQL transactions with the connection 
-- @@VERSION -- use version of the SQL Server 

use AdventureWorks2016
GO 

DECLARE @City NVARCHAR(50)
SET @City = 'New York'

SELECT * 
FROM Person.Address
WHERE City = @City 
GO 
-- create a stored procedure using a Parameter

use AdventureWorks2016
GO

DROP PROCEDURE dbo.uspGetNewAddress
GO

CREATE PROCEDURE dbo.uspGetNewAddress @City NVARCHAR(50)
AS 
SELECT * 
FROM Person.Address
WHERE City = @City 
GO 


-- Execute/ Call the Stored Procedure (passing the parameter value at runtime)

EXEC dbo.uspGetNewAddress @City = 'New York'
GO 

EXEC dbo.uspGetNewAddress @City = 'Sydney'
GO 

