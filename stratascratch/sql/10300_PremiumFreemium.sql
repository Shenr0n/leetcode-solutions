with cte_downloads as 
(
    select 
        d.date,
        sum(case when a.paying_customer = 'no' then d.downloads end) as non_paying,
        sum(case when a.paying_customer = 'yes' then d.downloads end) as paying
    from ms_user_dimension u
    join ms_acc_dimension a
        on u.acc_id = a.acc_id
    join ms_download_facts d
        on u.user_id = d.user_id
    group by d.date)
select date, non_paying, paying
from cte_downloads
where non_paying > paying
order by date;