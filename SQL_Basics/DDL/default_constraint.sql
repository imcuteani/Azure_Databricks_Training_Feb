-- Default Constraint 

-- A default constraint is defined to specify a value for a column when a value is not given by the user. 
-- A default value are used when a given value is typically assigned to a column if a 
--column is defined as NOT NULL


-- Default Constraint in SQL Server 

-- A default constraint is defined to specify a value for a column when a value is not given by the user 

-- A default values are used when a given value is typically assigned to a column
-- if a column is defined as NOT NULL

-- Check Constraints allow to restrict the range of values within a column in a table on SQL server
-- TaxAmount and SubTotal, ShippingAmount values should be positive 

use "kpmgsqltraining"
go 

drop table Orders.OrderHeader
GO

create table Orders.OrderHeader
(OrderID INT IDENTITY(1,1),
OrderDate DATE NOT NULL CONSTRAINT df_orderdate DEFAULT GETDATE(),
SubTotal MONEY NOT NULL CONSTRAINT ck_subtotalcheck CHECK (SubTotal > 0),
TaxAmount MONEY NOT NULL CONSTRAINT ck_taxamountvalue CHECK (TaxAmount > 0),
ShippingAmount MONEY NOT NULL CONSTRAINT ck_shippingamountvalue CHECK (ShippingAmount >= 0),
GrandTotal AS (SubTotal + TaxAmount + ShippingAmount),
FinalShipDate DATE NULL,
CONSTRAINT pk_orderheaderid PRIMARY KEY (OrderID))
GO


