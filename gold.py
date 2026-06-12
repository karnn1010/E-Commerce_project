source_df = spark.read.jdbc(
    url=jdbc_url,
    table="customers",
    properties=connection_properties
)

source_df.write.mode("overwrite").saveAsTable(
    "bronze.customers"
)

query = f"""
(
SELECT *
FROM customers
WHERE updated_at > '{last_watermark}'
) temp
"""

incremental_df = spark.read.jdbc(
    url=jdbc_url,
    table=query,
    properties=connection_properties
)