-- returns information for the conditions
SELECT t.`title`, g.`name`
  FROM `tv_shows` AS t
-- joins left condition
       LEFT JOIN `tv_show_genres` AS s
       ON t.`id` = s.`show_id`
-- left condition to join
       LEFT JOIN `tv_genres` AS g
       ON s.`genre_id` = g.`id`
 ORDER BY t.`title`, g.`name`;
