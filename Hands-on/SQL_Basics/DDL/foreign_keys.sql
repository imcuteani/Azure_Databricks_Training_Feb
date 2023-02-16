-- Foreign Key -- 

-- Similar to check constraint, Allows for enforcing a range of values which are allowed in a column. 
-- A check constraint derives its data boundaries through the use of a static value or a function. 
-- The Foreign key derives its data boundary through the use of tables. 

-- Foreign key itself enforces a parent-child relationship. 
-- customer (parent) -> order (child), we need to have a primary key being defined for parent key in order to create the foreign key. 

-- Create table then add foreign keys to the existing tables -- 

use kpmgsqltraining
go 

--drop table LookupTables.STATE

create table LookupTables.STATE
(StateID int IDENTITY(1,1),
StateProvince VARCHAR(50) NOT NULL UNIQUE,
CountryID int NOT NULL,
StateProvinceAbbrev CHAR(2) NOT NULL,
CONSTRAINT pk_stateprovince PRIMARY KEY (StateID))
go 

-- drop table LookupTables.Country 

create table LookupTables.Country
(CountryID int IDENTITY(1,1),
CountryName VARCHAR(50) NOT NULL UNIQUE,
CONSTRAINT pk_countryid PRIMARY KEY (CountryID))

-- adding FOREIGN key 

alter table LookupTables.STATE
add CONSTRAINT fk_countrytostate FOREIGN KEY (CountryID)
REFERENCES LookupTables.Country(CountryID)
go 