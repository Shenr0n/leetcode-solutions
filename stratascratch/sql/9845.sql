select 
    count(worker_id) as n_admins
from worker
where department = 'Admin' and month(joining_date) >= 4;