select 
    distinct home_library_code
from library_usage
where ((circulation_active_year = 2016) 
        and (provided_email_address = 0) 
        and (notice_preference_definition = 'email'));