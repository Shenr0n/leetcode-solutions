import pyspark
import pyspark.sql.functions as F

airbnb_search_details = airbnb_search_details.groupBy('city','property_type') \
    .agg(F.avg('bathrooms').alias('n_bathrooms_avg'), F.avg('bedrooms').alias('n_bedrooms_avg'))

airbnb_search_details.toPandas()