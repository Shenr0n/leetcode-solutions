select 
    e.location,
    avg(cast(h.popularity as float)) as avg_popularity
from facebook_employees e
inner join facebook_hack_survey h
on e.id = h.employee_id
group by e.location
order by e.location;