# Import your libraries
import pyspark.sql.functions as F

worker = worker.withColumn("joining_date",F.to_date(worker["joining_date"]))
worker = worker.withColumn("year", F.year(worker["joining_date"]))
worker = worker.withColumn("month", F.month(worker["joining_date"]))

april_df = worker.filter((F.col("year") > 2014) | ((F.col("month") >= 4) & (F.col("year") == 2014)))

dept_df = (
    april_df
    .groupBy("department")
    .agg(F.count("*").alias("num_workers"))
    .orderBy(F.desc("num_workers"))
    .select("department","num_workers")
)
# To validate your solution, convert your final pySpark df to a pandas df
dept_df.toPandas()