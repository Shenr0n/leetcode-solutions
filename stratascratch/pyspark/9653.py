import pyspark
import pyspark.sql.functions as F

playbook_events = playbook_events.filter(F.col('device') == "macbook pro")

playbook_events = playbook_events.groupBy('event_name').agg(F.count('*').alias('event_count')).orderBy(F.desc('event_count'))

playbook_events.toPandas()