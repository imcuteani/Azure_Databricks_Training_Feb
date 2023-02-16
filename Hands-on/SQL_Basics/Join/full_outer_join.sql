-- FULL OUTER JOIN -- 

-- Based on the two tables specified in the join clause 
-- all data is retrieved from both of two tables regardless of the matching data

-- preserves the contents of both the left side and right side tables. 
-- when a match does not exist, a NULL value will appear in the result. 

use AdventureWorksLT2019; 

select a.ProductID, 
a.Name, 
b.SalesOrderID 
FROM SalesLT.Product a 
FULL OUTER JOIN SalesLT.SalesOrderDetail b 
ON a.ProductID = b.ProductID 
ORDER BY 1; 
