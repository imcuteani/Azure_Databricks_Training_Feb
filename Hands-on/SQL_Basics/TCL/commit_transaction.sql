use kpmgsqltraining
GO 

-- COMMIT Transaction -- 

-- COMMIT stands for Transaction Control Language are used to manage 
-- transactions in the database. These are used to manage the changes made by the DML statements. 
-- it also allows statements to be grouped together into logical transactions. 

-- COMMIT statement is used to permanently save any transaction into the database. 

DELETE FROM Customers.Customer WHERE FirstName = 'James'
COMMIT; 


select * from Customers.Customer 
GO
