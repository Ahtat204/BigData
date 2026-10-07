import os
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col

ES_NODES=os.getenv("ES_NODES") # for a cluster of nodes, this a comma-seperated list of hosts only (
ES_PORT=os.getenv("ES_PORT") ## this the REST API port
spark: SparkSession = SparkSession.builder.appName("SparkESJob").config("es.nodes", ES_NODES).config("es.port",ES_PORT).getOrCreate()
es_ef=spark.read.format("org.elasticsearch.spark.sql").load("customers")
es_ef.show()
