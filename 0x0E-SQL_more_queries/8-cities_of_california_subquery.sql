-- Script Lists all cities of CA in the database hbtn_0d_usa.
SELECT cities.name, cities.id
FROM cities
WHERE cities.state_id = (SELECT states.id
	FROM states
	WHERE states.name = "California")
ORDER BY cities.id ASC;
