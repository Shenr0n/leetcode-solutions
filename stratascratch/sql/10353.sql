with max_salary as
    (select max(salary) as top_salary
    from worker)
select title.worker_title as best_paid_title
from title
inner join worker
    on title.worker_ref_id = worker.worker_id
inner join max_salary on worker.salary = max_salary.top_salary;