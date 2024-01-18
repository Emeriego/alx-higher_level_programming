-- Script Lists all cities of CA in the database hbtn_0d_usa.
SELECT `c.id`, `name`
  FROM `cities` AS c
 WHERE `state_id` IN
       (SELECT `id`
	FROM `states
	WHERE `name` = "California")
 ORDER BY `c.id`;
