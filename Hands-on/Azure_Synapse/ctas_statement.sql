-- CTAS statement 

CREATE TABLE [dbo].[FactInternetSales_new] 
WITH 
( 
 DISTRIBUTION = ROUND_ROBIN,
 CLUSTERED COLUMNSTORE INDEX
)
AS 
SELECT * FROM [dbo].[FactInternalSales];


-- using CTAS to copy a table 

-- CTAS can help to change to copy data from one table to another while also maintaining / changing the partitioning, indexing and column 
-- types

-- Create a table as heap with Distribution with ROUND_ROBIN 


CREATE TABLE FactInternetSales
( 
 ProductKey int NOT NULL,
 OrderDateKey int NOT NULL,
 DueDateKey int NOT NULL,
 ShipDateKey int NOT NULL,
 CustomerKey int NOT NULL,
 PromotionKey int NOT NULL,
 CurrencyKey int NOT NULL,
 SalesTerritoryKey int NOT NULL,
 SalesOrderNumber nvarchar(20) NOT NULL,
 SalesOrderLineNumber tinyint NOT NULL,
 RevisionNumber tinyint NOT NULL,
 OrderQuantity smallint NOT NULL,
 UnitPrice money NOT NULL,
 ExtendedAmount money NOT NULL,
 UnitPriceDiscountPct float NOT NULL,
 DiscountAmount float NOT NULL,
 ProductStandardCost money NOT NULL,
 TotalProductCost money NOT NULL,
 SalesAmount money NOT NULL,
 TaxAmt money NOT NULL,
 Frieght money NOT NULL,
 CarrierTrackingNumber nvarchar(25),
 CustomerPONumber nvarchar(25)
 ) 
 WITH (
 HEAP,
 DISTRIBUTION = ROUND_ROBIN
 );


 CREATE TABLE FactInternetSales_new
 WITH 
 (
  CLUSTERED COLUMNSTORE INDEX,
  DISTRIBUTION = HASH(ProductKey),
  PARTITION 
  (
   OrderDateKey RANGE RIGHT FOR VALUES 
   ( 
   20000101, 20010101, 20020101, 20030101, 20040101, 20050101, 20060101, 20070101, 20080101, 20090101,
   20100101, 20110101, 20120101, 20130101, 20140101, 20150101, 20160101, 20170101, 20180101, 20190101,
   20200101, 20210101, 20220101, 20230101, 20240101, 20250101, 20260101, 20270101, 20280101, 20290101
   ) 
  )
)
AS SELECT * FROM FactInternetSales;

-- rename the tables, swap in the new table and then drop the old table

RENAME OBJECT FactInternetSales TO FactInternetSales_old;
RENAME OBJECT FactInternetSales_new TO FactInternetSales;

DROP TABLE FactInternetSales_old;

select top 10 * from dbo.FactInternetSales;