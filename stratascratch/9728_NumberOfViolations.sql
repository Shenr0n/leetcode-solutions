select 
    YEAR(inspection_date) as inspection_year,
    count(violation_id) as n_violations
from sf_restaurant_health_violations
where business_name = 'Roxanne Cafe'
group by YEAR(inspection_date)
order by inspection_year;