with top_revenue as (
select 
    product_id,
    sum(cost_in_dollars * units_sold) as revenue
from online_orders
where month(date_sold) between 1 and 6
group by product_id
)
select top 5
    product_id,
    revenue
from top_revenue
order by revenue desc;