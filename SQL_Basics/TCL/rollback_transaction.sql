-- Rollback statement restores the database to last committed state. 

-- It's also used with savepoint command to jump to a savepoint. 

use kpmgsqltraining
GO 

BEGIN TRANSACTION;
DELETE FROM Customers.Customer WHERE FirstName = 'Matt'
ROLLBACK TRANSACTION;

