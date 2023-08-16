-- shows all titles and tv shows in action
SELECT `title`, SUM(`rate`) AS `rating`
-- where the information is taken from
  FROM `tv_shows` AS t
-- inner join the table to check if it works 
       INNER JOIN `tv_show_ratings` AS r
       ON t.`id` = r.`show_id`
-- group by size 
 GROUP BY `title`
 ORDER BY `rating` DESC;
