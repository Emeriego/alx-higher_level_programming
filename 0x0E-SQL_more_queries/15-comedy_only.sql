-- Script Lists all comedy shows in the database hbtn_0d_tvshows.
SELECT ti.`title`
  FROM `tv_shows` AS ti
       INNER JOIN `tv_show_genres` AS s
       ON ti.`id` = s.`show_id`

       INNER JOIN `tv_genres` AS g
       ON g.`id` = s.`genre_id`
       WHERE g.`name` = "Comedy"
 ORDER BY ti.`title`;
