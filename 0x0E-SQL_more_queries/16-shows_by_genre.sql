-- Script Lists all shows and genres linked to the show from the
SELECT ti.`title`, g.`name`
  FROM `tv_shows` AS ti
       LEFT JOIN `tv_show_genres` AS s
       ON ti.`id` = s.`show_id`
       LEFT JOIN `tv_genres` AS g
       ON s.`genre_id` = g.`id`
 ORDER BY ti.`title`, g.`name`;
