with total_ct as (
    select count(*) as total_count
    from fb_active_users
),
open_us as (
    select count(*) as us_open_count
    from fb_active_users
    where country = 'USA' and status = 'open'
)
select 
    ((cast(open_us.us_open_count as float)/cast(total_ct.total_count as float))*100) as us_active_share
    from total_ct, open_us;