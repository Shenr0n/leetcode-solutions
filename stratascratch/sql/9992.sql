select 
    artist,
    count (stream_date) as n_occurences
from spotify_worldwide_daily_song_ranking
group by artist
order by n_occurences desc;