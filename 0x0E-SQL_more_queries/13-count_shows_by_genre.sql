-- Script Lists all genres from the database hbtn_0d_tvshows along with the number of
-- shows links to each.
-- Does not display genres without linked shows.
SELECT g.`name` AS `genre`,
       COUNT(*) AS `number_of_shows`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS s
       ON g.`id` = s.`genre_id`
 GROUP BY g.`name`
 ORDER BY `number_of_shows` DESC;
