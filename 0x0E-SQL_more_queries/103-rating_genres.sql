-- all shows will be displayed
SELECT `name`, SUM(`rate`) AS `rating`
-- the shows will be seletced from 
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON s.`genre_id` = g.`id`
-- inner join condition 
       INNER JOIN `tv_show_ratings` AS r
       ON r.`show_id` = s.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;

