select 
    c.first_name, 
    o.order_date, 
    o.order_details,
    o.total_order_cost
from customers c
right join orders o
on c.id = o.cust_id
where c.first_name in ('Jill', 'Eva')
order by o.cust_id;