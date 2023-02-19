source(output(
		ProductID as short,
		Name as string,
		ProductNumber as string,
		Color as string,
		StandardCost as double,
		ListPrice as double,
		Size as string,
		Weight as double,
		ProductCategoryID as short,
		ProductModelID as short,
		SellStartDate as string,
		SellEndDate as string,
		DiscontinuedDate as string,
		ThumbNailPhoto as string,
		ThumbnailPhotoFileName as string,
		rowguid as string,
		ModifiedDate as string
	),
	allowSchemaDrift: true,
	validateSchema: false,
	ignoreNoFilesFound: false) ~> Product
source(output(
		ProductCategoryID as short,
		ParentProductCategoryID as short,
		Name as string,
		rowguid as string,
		ModifiedDate as string
	),
	allowSchemaDrift: true,
	validateSchema: false,
	ignoreNoFilesFound: false) ~> ProductCategory
source(output(
		ProductModelID as short,
		Name as string,
		CatalogDescription as string,
		rowguid as string,
		ModifiedDate as string
	),
	allowSchemaDrift: true,
	validateSchema: false,
	ignoreNoFilesFound: false) ~> ProductModel
Product select(mapColumn(
		ProductID,
		Product = Name,
		ProductCategoryID,
		ProductModelID
	),
	skipDuplicateMapInputs: true,
	skipDuplicateMapOutputs: true) ~> SelectProductColumns
ProductCategory select(mapColumn(
		ProductCategoryID,
		ProductCategory = Name
	),
	skipDuplicateMapInputs: true,
	skipDuplicateMapOutputs: true) ~> SelectProductCategoryColumns
ProductModel select(mapColumn(
		ProductModelID,
		ProductModel = Name
	),
	skipDuplicateMapInputs: true,
	skipDuplicateMapOutputs: true) ~> SelectProductModelColumns
SelectProductColumns, SelectProductCategoryColumns lookup(SelectProductColumns@ProductCategoryID == SelectProductCategoryColumns@ProductCategoryID,
	multiple: false,
	pickup: 'any',
	broadcast: 'auto')~> LookupProductCategory
LookupProductCategory, SelectProductModelColumns lookup(SelectProductColumns@ProductModelID == SelectProductModelColumns@ProductModelID,
	multiple: false,
	pickup: 'any',
	broadcast: 'auto')~> LookupProductModel
LookupProductModel select(mapColumn(
		ProductID,
		Product,
		ProductCategoryID = SelectProductColumns@ProductCategoryID,
		ProductModelID = SelectProductColumns@ProductModelID,
		ProductCategory,
		ProductModel
	),
	skipDuplicateMapInputs: true,
	skipDuplicateMapOutputs: true) ~> RemoveDuplicateColumns
RemoveDuplicateColumns sink(allowSchemaDrift: true,
	validateSchema: false,
	format: 'parquet',
	umask: 0022,
	preCommands: [],
	postCommands: [],
	skipDuplicateMapInputs: true,
	skipDuplicateMapOutputs: true) ~> WriteDataToADLS