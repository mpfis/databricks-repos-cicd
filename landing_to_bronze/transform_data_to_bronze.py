# Databricks notebook source
print("initial test")

# COMMAND ----------

aget_data = spark.read.csv(dbutils.fs.ls("/databricks-datasets/online_retail/data-001/")[0].path, inferSchema=True, header=True)

# COMMAND ----------

dbutils.widgets.text("country","","")

# COMMAND ----------

country = dbutils.widgets.get("country")

# COMMAND ----------

print(country)

# COMMAND ----------

get_country_data = get_data.filter(f"Country == '{country}'")

# COMMAND ----------

get_country_data.write.saveAsTable("retail_bronze", format="delta", mode="append")
