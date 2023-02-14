use "kpmgsqltraining"
go 


SET IDENTITY_INSERT [Customers].[Customer] ON
INSERT INTO Customers.Customer(CustomerID, CompanyName, FirstName, LastName, ModifiedDate) VALUES (1, 'AdventureWorks', 'James', 'Webb', '2022-01-01')
INSERT INTO Customers.Customer(CustomerID, CompanyName, FirstName, LastName, ModifiedDate) VALUES (2, 'Fabrikum', 'Matt', 'Hardin', '2021-01-01')
GO

-- Set IDENTITY_INSERT OFF 
SET IDENTITY_INSERT [Customers].[Customer] OFF

SET IDENTITY_INSERT [Customers].[CustomerAddress] ON
INSERT INTO Customers.CustomerAddress
(AddressId,
AddressType,
AddressLine1,
AddressLine2,
AddressLine3,
City,
StateProvince,
Country)
VALUES 
(1,
'local'
 ,'seattle'
 ,''
 ,''
 ,'Seattle',
 '',
 'united states')
GO

use "cgsqltraining"
go 

SET IDENTITY_INSERT [Products].[Product] ON 
INSERT INTO Products.Product (ProductID, ProductName, ProductCost, ListPrice, ProductDescription) VALUES (1, 'Samsung', 5.66, 4.55,'Refrigerator')
INSERT INTO Products.Product (ProductID, ProductName, ProductCost, ListPrice, ProductDescription) VALUES (2, 'Sansui', 7.66, 16.55,'Washing Machine')
INSERT INTO Products.Product (ProductID, ProductName, ProductCost, ListPrice, ProductDescription) VALUES (3, 'Samsung', 20.66, 27.55,'Laptop')
INSERT INTO Products.Product (ProductID, ProductName, ProductCost, ListPrice, ProductDescription) VALUES (4, 'HP', 9.66, 15.55,'Smart TV')
INSERT INTO Products.Product (ProductID, ProductName, ProductCost, ListPrice, ProductDescription) VALUES (5, 'Lloyds', 10.66, 24.55,'AC')
INSERT INTO Products.Product (ProductID, ProductName, ProductCost, ListPrice, ProductDescription) VALUES (6, 'Samsung', 17.66, 34.55,'Refrigerator')
INSERT INTO Products.Product (ProductID, ProductName, ProductCost, ListPrice, ProductDescription) VALUES (7, 'Samsung', 8.66, 23.55,'Refrigerator')
INSERT INTO Products.Product (ProductID, ProductName, ProductCost, ListPrice, ProductDescription) VALUES (8, 'Samsung', 4.66, 45.55,'Printer')
INSERT INTO Products.Product (ProductID, ProductName, ProductCost, ListPrice, ProductDescription) VALUES (9, 'Daikin', 6.66, 12.55,'Refrigerator')

select * from Products.Product

SET IDENTITY_INSERT [Products].[Product] OFF 

SET IDENTITY_INSERT [Orders].[OrderDetail] ON
INSERT INTO Orders.OrderDetail (OrderDetailID, SKU, Quantity, UnitPrice, ShipDate) VALUES (1, 'Samsung', 10, 6.55,'2022-03-05')
INSERT INTO Orders.OrderDetail(OrderDetailID, SKU, Quantity, UnitPrice, ShipDate) VALUES (2, 'Sansui', 7, 16.55,'2021-03-06')

SET IDENTITY_INSERT [Orders].[OrderDetail] OFF 