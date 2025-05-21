import pyspark
import pyspark.sql.functions as F

ms_employee_salary = ms_employee_salary.groupby('id', 'first_name', 'last_name', 'department_id').agg(F.max('salary').alias('salary')).sort('id')

ms_employee_salary.toPandas()