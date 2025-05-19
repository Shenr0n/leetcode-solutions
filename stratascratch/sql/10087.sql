select 
    distinct p.post_id,
    p.poster,
    p.post_text,
    p.post_keywords,
    p.post_date
from facebook_posts p
inner join facebook_reactions r
on p.post_id = r.post_id
where r.reaction = 'heart';