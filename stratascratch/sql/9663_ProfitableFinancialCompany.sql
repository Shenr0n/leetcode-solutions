select top 1 company, continent
from forbes_global_2010_2014
where sector = 'Financials'
order by profits desc;