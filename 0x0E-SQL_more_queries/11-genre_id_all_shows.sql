-- lists all the movies and genres
SELECT s.`title`, g.`genre_id`
-- returns the selected files
-- conditions 
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;

