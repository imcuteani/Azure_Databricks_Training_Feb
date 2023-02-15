let 
resource_group_name="cgazrg"
tag="az_sql_db_automation"
location="central india"

# Create Azure Resource Group 

az group create --name $resource_group_name --location $location --tags $tag

# Create Azure SQL server 

az sql server create --name "<name_sql_server>" --resource-group "<resource_group_name>" --location "<location>" --admin-user "<admin_user_login_name>" --admin-password "<admin_password>"

# Create Azure SQL server Firewall rule 

az sql server firewall-rule create --resource-group "<resource_group_name>" --server "<name_sql_server>" -n "<firewall_rule_name>" --start-ip-address "<start_ip>" --end-ip-address "<end_ip_address>"

# Create the Azure SQL db 

az sql db create  \
-- resource-group "<resource_group_name>" \
--server "<name_sql_server>" \
--name "<name_sql_db>" \
--sample-name "<AdventureWorks>" \
--edition GeneralPurpose \
--compute-model Serverless \
--family Gen5 \
--capacity 2 



