# Import your libraries
import pyspark.sql.functions as F

result = customers.join(orders, customers.id == orders.cust_id, "left")
result = (
    result
    .select("first_name", "last_name", "city", "order_details")
    .orderBy(F.asc("first_name"),F.asc("order_details"))
)
# To validate your solution, convert your final pySpark df to a pandas df
result.toPandas()