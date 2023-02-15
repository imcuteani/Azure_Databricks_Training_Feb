-- CAST and CONVERT Function in TSQL 

-- use cast() to convert an expression from one datatype to another datatype 

-- use cast() function to convert a decimal to another different length 

select CAST(59.1 as DEC(1,0)) result; 

select CAST(5.95 as int) result; 

-- CONVERT() function converts an expression from one datatype to another datatype
-- if the conversion fails, the function will return an error, otherwise, it'll return the converted value. 
-- CONVERT() function is used to do the converting and formatting of the data type at the same time
-- CAST() function is used to convert a data type without a specific format  


use AdventureWorksLT2019
GO 

select CONVERT(varchar(30),AddressID),
AddressLine1,
AddressLine2,
City,
StateProvince
FROM 
SalesLT.Address

