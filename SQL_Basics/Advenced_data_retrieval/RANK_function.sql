-- Limitation in ROW_NUMBER() function 

-- The ROW_NUMBER() function does not always return the same results if there're duplicate 

-- values within the ORDER BY clause specified. 

-- The column which is defined with the ORDER BY clause if having duplicate values
-- then the ROW_NUMBER() function doesn't return the expected sequential records in the result set. 

-- RANK() function provides sequential ordering of rows
-- duplicate values will receive the same rank value 
-- will provide gaps in the sequence of returned rows when ties exist 
-- leave the gaps in the bunch of sequence of row groups 


use AdventureWorks2016;

select 
RANK() OVER(ORDER BY FirstName) rank_value,
FirstName, 
LastName,
ModifiedDate
FROM Person.Person;

-- Difference between RANK() and DENSE_RANK() function. 

-- 1. RANK(), DENSE_RANK() are similar to ROW_NUMBER() function but when there are ties exist. They will give the same to the value to the tied values. 
-- RANK() function will perform the ranking. So that the numbering will go 1, 2, 2, 4 based on Ranks.
-- RANK() function is used to calculate a rank for each row within a partition of a result set.
-- Dense_RANK() function will not leave any gaps between the rank groups 

select 
DENSE_RANK() OVER(ORDER BY FirstName) dense_rank_value,
FirstName,
LastName,
ModifiedDate
FROM Person.Person; 




