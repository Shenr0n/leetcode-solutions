import pyspark
import pyspark.sql.functions as F

fact_events = fact_events.withColumn('month', F.month('time_id'))
fact_events = fact_events.groupby('client_id', 'month').agg(F.countDistinct('user_id').alias('users_num'))

result = fact_events.select('client_id','month','users_num')
result.toPandas()