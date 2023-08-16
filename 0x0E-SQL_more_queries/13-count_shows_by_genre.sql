-- selects information from table
SELECT name AS genre, COUNT(*) AS number_of_shows FROM tv_genres
-- joins the genres and tv shows together
JOIN tv_show_genres ON id=tv_show_genres.genre_id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
