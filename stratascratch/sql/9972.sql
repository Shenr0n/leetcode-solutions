select
    employeename,
    basepay
from sf_public_salaries
where jobtitle like '%Police%Captain%'  or jobtitle like '%Captain%Police%';