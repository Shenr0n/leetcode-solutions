select department, count(worker_id) as num_workers
from worker
where joining_date >= '2014-04-01'
group by department
order by num_workers desc;