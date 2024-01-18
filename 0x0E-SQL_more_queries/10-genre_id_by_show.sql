-- Script Lists all shows in hbtn_0d_tvshows that have at least one genre
SELECT t.`title`, gr.`genre_id`
  FROM `tv_shows`
	AS t
        INNER JOIN `tv_show_genres` AS gr
	ON t.`id` = gr.`show_id`
 ORDER BY t.`title`, gr.`genre_id`;
