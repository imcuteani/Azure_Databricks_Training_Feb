-- Vertical partitioning in SQL Server -- 

-- Vertical table partitioning is mostly used to increase the SQL query performance & optimization purpose. 
-- It's used especially in cases where a query retrieves all columns from a table which contains a number of very wide text or BLOB columns. 

CREATE TABLE EmployeeReports
( 
    ReportID int IDENTITY(1,1) NOT NULL,
    ReportName VARCHAR(100), 
    ReportNumber VARCHAR(20),
    ReportDescription VARCHAR(MAX)
    CONSTRAINT EReport_PK PRIMARY KEY CLUSTERED (ReportID)
)

DECLARE @i int 
SET @i = 1

BEGIN TRAN 
WHILE @i&lt;100000
BEGIN 
INSERT INTO EmployeeReports
(
    ReportName,
    ReportNumber,
    ReportDescription
)
VALUES
(
    'ReportName',
    CONVERT(varchar (20), @i),
    REPLICATE('Report', 1000)
)
SET @i=@i+1
END 
COMMIT TRAN 
GO 

SET STATISTICS IO ON 
SET STATISTICS TIME ON 
SELECT er.ReportID, er.ReportName, er.ReportNumber 
FROM dbo.EmployeeReports er 
WHERE er.ReportNumber LIKE '%33%'
SET STATISTICS IO OFF 
SET STATISTICS TIME OFF 


CREATE TABLE ReportsDesc
(
    ReportID int FOREIGN KEY REFERENCES EmployeeReports (ReportID),
    ReportDescription VARCHAR(max)
    CONSTRAINT PK_ReportDesc PRIMARY KEY CLUSTERED(ReportID)
)

CREATE TABLE ReportsData 
( 
    ReportID int NOT NULL,
    ReportName VARCHAR (100), 
    ReportNumber VARCHAR(20)
    CONSTRAINT DReport_PK PRIMARY KEY CLUSTERED (ReportID)
)
INSERT INTO dbo.ReportsData
(
    ReportID,
    ReportName, 
    ReportNumber
)
SELECT er.ReportID,
er.ReportName,
er.ReportNumber 
FROM dbo.EmployeeReports er 

SET STATISTICS IO ON 
SET STATISTICS TIME ON 
SELECT er.ReportID, er.ReportName, er.ReportNumber 
FROM dbo.EmployeeReports er 
WHERE er.ReportNumber LIKE '%33%'
SET STATISTICS IO OFF 
SET STATISTICS TIME OFF 