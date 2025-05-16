select 
    city,
    property_type,
    avg(cast(bathrooms as float)) as n_bathrooms_avg,
    avg(cast(bedrooms as float)) as n_bedrooms_avg
from airbnb_search_details
group by city, property_type
order by city, property_type;