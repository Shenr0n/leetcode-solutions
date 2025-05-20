with cte__unique_shipments as (
    select 
    format([shipment_date], 'yyyy-MM') as year_month,
    count(distinct cast(shipment_id as varchar) +'_'+cast(sub_id as varchar)) as count
    from amazon_shipment
    group by format([shipment_date], 'yyyy-MM')
)
select year_month, count
from cte__unique_shipments;