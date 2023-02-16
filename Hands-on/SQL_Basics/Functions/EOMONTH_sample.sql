-- SQL Server EOMONTH function -- 

-- built-in function in SQL Server provides the last day of the month based on specified input value 


select EOMONTH('2024-02-15') end_of_month_feb23; 

-- passing a date with month to signify whether its a leap year or not

select EOMONTH('2020-02-15') end_of_month_feb20;


-- to get the total number of days in a specified month 

select DAY(EOMONTH('2023-02-15')) DAYS; 