-- check constraints in SQL Server -- 

-- Allows to restrict the range of values allowed within a column in a table on SQL Server
-- ProductCost and ListPrice should be > 0 
-- OrderDetail table, the tax and shipping amount value should be > 0 

use "cgsqltraining"
GO

drop table Products.Product 
go 

create table Products.Product
(ProductID INT IDENTITY(1,1),
ProductName VARCHAR(50) NOT NULL,
ProductCost MONEY NOT NULL CHECK (ProductCost > 0),
ListPrice MONEY NOT NULL CHECK (ListPrice > 0),
ProductMargin AS (ListPrice - ProductCost),  -- Computed columns
ProductDescription NVARCHAR(100) NULL,
CONSTRAINT pk_product PRIMARY KEY (ProductID))
go 

-- Adding check constraints for existing table 

use "cgsqltraining"
go 

alter table Orders.OrderDetail WITH CHECK
ADD CONSTRAINT ck_quantity CHECK (Quantity > 0)

alter table Orders.OrderHeader WITH CHECK
ADD CONSTRAINT ck_subtotal CHECK (SubTotal > 0)

alter table Orders.OrderHeader WITH CHECK
ADD CONSTRAINT ck_taxamount CHECK (TaxAmount >= 0)

alter table Orders.OrderHeader WITH CHECK
ADD CONSTRAINT ck_shippingamount CHECK (ShippingAmount >= 0)
go 

alter table Orders.OrderDetail WITH CHECK 
ADD CONSTRAINT ck_unitprice CHECK (UnitPrice > 0)
GO






