select 
    distinct hotel_name,
    total_number_of_reviews
from hotel_reviews
group by hotel_name, total_number_of_reviews
order by total_number_of_reviews desc;