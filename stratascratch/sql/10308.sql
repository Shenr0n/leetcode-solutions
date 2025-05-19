with dept_max_salary as (
select 
    max(e.salary) as max_salary,
    d.department as department_name
from db_employee e
inner join db_dept d
on e.department_id = d.id
group by d.department
),
salary_diff as (
select 
    max(case when department_name = 'marketing' then max_salary end) as mar_salary,
    max(case when department_name = 'engineering' then max_salary end) as eng_salary
from dept_max_salary
)
select abs(mar_salary - eng_salary) as salary_difference from salary_diff;