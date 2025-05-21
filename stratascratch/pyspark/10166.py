import pyspark
import pyspark.sql.functions as F

df_hotel_arena = hotel_reviews.filter(F.col('hotel_name') == "Hotel Arena")
result = df_hotel_arena.groupBy('hotel_name','reviewer_score').agg(F.count('*').alias('count'))

result.toPandas()