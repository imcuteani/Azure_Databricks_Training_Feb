-- Indentity property creates an identity column in a table. 
--This property is used to with the
-- CREATE TABLE and ALTER TABLE tsql statements. 


-- The identity property allows you to specify a counter of values for a specific column of a table. 

-- Columns with numeric data types -- TinyINT, smallINT, INT or BigINT can have this property. 

-- IDENTITY((seed, increment))

--productID INT NOT NULL IDENTITY(10, 5)

-- seed is the value of first row in the table
-- increment is the incremental value being added to the identity value of the previous row. 

-- it means the first row of the productID column would contain the value of 10 
-- wheras the second row would contain the value of 15 .. 
-- third row would contain the value of 20.. 

