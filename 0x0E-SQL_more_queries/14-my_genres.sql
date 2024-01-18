-- Script Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
SELECT g.`name`
  FROM `tv_genres` AS g
       INNER JOIN `tv_show_genres` AS tv
       ON g.`id` = tv.`genre_id`

       INNER JOIN `tv_shows` AS t
       ON t.`id` = tv.`show_id`
       WHERE t.`title` = "Dexter"
 ORDER BY g.`name`;
