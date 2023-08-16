-- displays all the information
SELECT name FROM tv_genres
-- join the tables together
JOIN tv_show_genres ON id=tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id=tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter'
-- order by the name 
ORDER BY name;
