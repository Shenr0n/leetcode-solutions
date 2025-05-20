select
    format(shipment_date, 'yyyy-MM') as year_month,
    count(distinct concat(shipment_id, sub_id)) as count
from amazon_shipment
group by format(shipment_date, 'yyyy-MM')
order by year_month;