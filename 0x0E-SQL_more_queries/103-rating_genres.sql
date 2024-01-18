-- Script Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT `name`, SUM(`rate`) AS `ratn`
  FROM `tv_genres` AS g
  INNER JOIN `tv_show_genres` AS tg
       ON tg.`genre_id` = g.`id`
       INNER JOIN `tv_show_ratings` AS r
       ON r.`show_id` = tg.`show_id`
 GROUP BY `name`
 ORDER BY `ratn` DESC;
