# Import your libraries
import pyspark.sql.functions as F

review_result = (
    hotel_reviews
    .groupBy("hotel_name","total_number_of_reviews")
    .count()
    .drop("count")
    .sort(F.desc("total_number_of_reviews"))
    .select("hotel_name","total_number_of_reviews")
    )

# To validate your solution, convert your final pySpark df to a pandas df
review_result.toPandas()