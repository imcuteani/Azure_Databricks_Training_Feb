-- A primary key defines the column or columns within a table that uniquely
-- identifies each row within the table. During INSERT operation
-- without a primary key, impossible to modify to delete a single row
-- unless it can be uniquely defined. 
-- a table in a db should have a primary key
-- it cant contain a NULL 

use kpmgsqltraining
go 

drop table Customers.Customer
go 

-- create tables with primary key --

create table Customers.Customer
(CustomerID INT IDENTITY(1,1),
CompanyName VARCHAR(50) NULL,
FirstName VARCHAR(50) NULL,
LastName VARCHAR(50) NULL,
ModifiedDate DATE NOT NULL,
CONSTRAINT pk_customer PRIMARY KEY (CustomerID))
go 

drop table Customers.CustomerAddress
go 

create table Customers.CustomerAddress
(AddressID INT IDENTITY(1,1),
AddressType VARCHAR(20) NOT NULL,
AddressLine1 VARCHAR(50) NOT NULL,
AddressLine2 VARCHAR(50) NULL,
AddressLine3 VARCHAR(50) NULL,
City VARCHAR(50) NOT NULL,
StateProvince VARCHAR(70) NULL,
Country VARCHAR(70) NULL,
CONSTRAINT pk_customeraddress PRIMARY KEY (AddressID))
go 

drop table Orders.OrderHeader
go 

create table Orders.OrderHeader
(OrderID INT IDENTITY(1,1),
OrderDate DATE NOT NULL,
SubTotal MONEY NOT NULL,
TaxAmount MONEY NOT NULL,
ShippingAmount MONEY NOT NULL,
GrandTotal AS (SubTotal + TaxAmount + ShippingAmount),
FinalShipDate DATE NULL,
CONSTRAINT pk_orderheader PRIMARY KEY (OrderID))
go 


drop table Orders.OrderDetail
go 

create table Orders.OrderDetail
(OrderDetailID INT IDENTITY(1,1),
SKU CHAR(10) NOT NULL,
Quantity INT NOT NULL,
UnitPrice MONEY NOT NULL,
ShipDate DATE NULL,
CONSTRAINT pk_orderdetail PRIMARY KEY (OrderDetailID))
go 

drop table Products.Product 
go 

create table Products.Product
(ProductID INT IDENTITY(1,1),
ProductName VARCHAR(50) NOT NULL,
ProductCost MONEY NOT NULL,
ListPrice MONEY NOT NULL,
ProductDescription NVARCHAR(100) NULL,
CONSTRAINT pk_product PRIMARY KEY (ProductID))
go 

drop table HumanResources.Employee
go 

create table HumanResources.Employee
(EmployeeID INT IDENTITY(1,1),
FirstName VARCHAR(50) NOT NULL,
LastName VARCHAR(50) NOT NULL,
JobTitle VARCHAR(50) NOT NULL,
BirthDate DATE NOT NULL,
HireDate DATE NOT NULL,
CONSTRAINT pk_employee PRIMARY KEY (EmployeeID))
go 

drop table HumanResources.EmployeeAddress
go 

create table HumanResources.EmployeeAddress
(AddressID INT IDENTITY(1,1),
AddressType VARCHAR(20) NOT NULL,
AddressLine1 VARCHAR(50) NOT NULL,
AddressLine3 VARCHAR(50) NULL,
City VARCHAR(50) NOT NULL,
StateProvince VARCHAR(50) NULL,
Country VARCHAR(70) NULL,
CONSTRAINT pk_employeeaddress PRIMARY KEY (AddressID))
go 