-- shows all the information necessary for it to work
-- selects distinctly
SELECT DISTINCT `title`
  FROM `tv_shows` AS t
-- join through left join
       LEFT JOIN `tv_show_genres` AS s
       ON s.`show_id` = t.`id`
-- left join in the picture ishuuu
       LEFT JOIN `tv_genres` AS g
       ON g.`id` = s.`genre_id`
-- where it is not in we mize
       WHERE t.`title` NOT IN
             (SELECT `title`
                FROM `tv_shows` AS t
	             INNER JOIN `tv_show_genres` AS s
		     ON s.`show_id` = t.`id`

		     INNER JOIN `tv_genres` AS g
		     ON g.`id` = s.`genre_id`
		     WHERE g.`name` = "Comedy")
 ORDER BY `title`;

