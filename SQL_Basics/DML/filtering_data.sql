-- filtering data -- 

use "AdventureWorks2016";

--select * from Production.Product

select ProductID,
Name, 
StandardCost,
ListPrice,
Size
from 
Production.Product 
where 
ListPrice < 10; 

select ProductID, 
Name, 
StandardCost, 
ListPrice,
Size
from 
Production.Product 
where 
ListPrice > 8.99 AND ListPrice <= 35.99; 

select ProductID, 
Name,
StandardCost,
ListPrice,
Size
FROM
Production.Product
where ListPrice > 7.99 OR ListPrice < 34.99;

use "AdventureWorks2016"

select ProductID, 
Name, 
StandardCost, 
ListPrice,
Size
from 
Production.Product
where Name > 'Mu';


select ProductID, 
Name,
ListPrice
from 
Production.Product
where (ListPrice BETWEEN 2 AND 15) 
OR (ListPrice BETWEEN 18 AND 50);

select ProductID, 
Name,
ListPrice
from 
Production.Product
where (ListPrice BETWEEN 2 AND 15) 
AND (ListPrice BETWEEN 18 AND 50);

-- retrieve the product details whose product name contains the character 'tai' in middle

select ProductID,
Name,
ListPrice 
from 
Production.Product
where Name LIKE '%tai%'



