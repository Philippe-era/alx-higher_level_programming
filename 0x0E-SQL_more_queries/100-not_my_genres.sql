-- returns the information from the tbale
SELECT DISTINCT `name`
  FROM `tv_genres` AS g
-- innner joins the conditions
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`
-- innner joins the tv shows
       INNER JOIN `tv_shows` AS t
       ON s.`show_id` = t.`id`
       WHERE g.`name` NOT IN
             (SELECT `name`
                FROM `tv_genres` AS g
	             INNER JOIN `tv_show_genres` AS s
		     ON g.`id` = s.`genre_id`

		     INNER JOIN `tv_shows` AS t
		     ON s.`show_id` = t.`id`
		     WHERE t.`title` = "Dexter")
	-- the order in which it should be executed
 ORDER BY g.`name`;
