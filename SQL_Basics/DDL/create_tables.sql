 USE kpmgsqltraining
 GO
 
-- Schemas to be created before the table creation in SQL server 
-- create schemas -- 
CREATE SCHEMA Customers AUTHORIZATION dbo 
GO

CREATE SCHEMA Orders AUTHORIZATION dbo 
GO 

CREATE SCHEMA Products AUTHORIZATION dbo 
GO 

CREATE SCHEMA LookupTables AUTHORIZATION dbo 
GO 

CREATE SCHEMA HumanResources AUTHORIZATION dbo 
GO 

-- Create Table --

-- create Customer table -- 

CREATE TABLE Customers.Customer
(CustomerID INT IDENTITY(1,1),
CompanyName VARCHAR(50) NULL,
FirstName VARCHAR(50) NULL,
LastName VARCHAR(50) NULL,
ModifiedDate DATE NOT NULL)
GO 

-- create CustomerAddress table 

CREATE TABLE Customers.CustomerAddress
(AddressID INT IDENTITY(1,1),
AddressType VARCHAR(20) NOT NULL,
AddressLine1 VARCHAR(50) NOT NULL,
AddressLine2 VARCHAR(50)  NULL,
AddressLine3 VARCHAR(50) NULL,
City VARCHAR(50) NOT NULL,
StateProvince VARCHAR(50) NULL,
Country VARCHAR(70) NULL)
GO 

-- create OrderHeader table -- 

CREATE TABLE Orders.OrderHeader
(OrderID INT IDENTITY(1,1),
OrderDate DATE NOT NULL,
SubTotal MONEY NOT NULL,
TaxAmount MONEY NOT NULL,
ShippingAmount MONEY NOT NULL,
FinalShipDate DATE NULL)
GO 

-- Create OrderDetail table -- 

CREATE TABLE Orders.OrderDetail
(OrderDetailID INT IDENTITY(1,1),
SKU CHAR(10) NOT NULL,
Quantity INT NOT NULL,
UnitPrice MONEY NOT NULL,
ShipDate DATE NULL)
GO 

-- Create Product table -- 

CREATE TABLE Products.Product
(ProductID INT IDENTITY(1,1),
ProductName VARCHAR(50)NOT NULL,
ProductCost MONEY NOT NULL,
ListPrice MONEY NOT NULL,
ProductDescription NVARCHAR(100) NULL)
GO 


-- create Employee table -- 

CREATE TABLE HumanResources.Employee
(EmployeeID INT IDENTITY(1,1),
FirstName VARCHAR(50) NOT NULL,
LastName VARCHAR(50) NOT NULL,
JobTitle VARCHAR(50) NOT NULL,
BirthDate DATE NOT NULL,
HireDate DATE NOT NULL)
GO 

-- create EmployeeAddress table -- 

CREATE TABLE HumanResources.EmployeeAddress
(AddressID INT IDENTITY(1,1),
AddressType VARCHAR(20) NOT NULL,
AddressLine1 VARCHAR(50) NOT NULL,
AddressLine2 VARCHAR(50) NULL,
AddressLine3 VARCHAR(50) NULL,
City VARCHAR(50) NOT NULL,
StateProvince VARCHAR(50) NULL,
Country VARCHAR(50) NULL)
GO


