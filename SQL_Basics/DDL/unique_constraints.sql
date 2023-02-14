-- Unique Key Constraint 

-- A unique key can accept null value 
-- A table in SQL server can have more than one unique key constraint

use "cgsqltraining"
go 

-- Create Unique Key constraint 
create table Products.TransactionHistory
(
    TransactionID int not NULL, 
    CONSTRAINT AK_transactionID UNIQUE (TransactionID)

); 

-- Adding Unique Key constraint to an existing table

ALTER TABLE Products.Product
ADD CONSTRAINT ak_listpricecost UNIQUE (ListPrice, ProductCost)
