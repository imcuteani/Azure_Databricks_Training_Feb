# Installation of Apache Spark 

mkdir spark 

# Download Apache spark 

wget https://dlcdn.apache.org/spark/spark-3.2.3/spark-3.2.3-bin-hadoop2.7.tgz

# Extract the folder 

sudo tar -xvf spark-3.2.3-bin-hadoop2.tgz 

# Move to the $SPARK_HOME folder 

sudo mv spark-3.2.3-bin-hadoop2 /usr/local/spark 

# Add the details to ~/.bashrc 

SPARK_HOME=/usr/local/spark
EXPORT PATH=$SPARK_HOME/bin:$PATH

# Apply the changes 

source ~/.bashrc 

# Open the Spark Shell 

spark-shell 

