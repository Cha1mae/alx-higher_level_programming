-- 9-cities_by_state_join.sql
--sort in order of ascending cities.id.
USE hbtn_0d_usa;

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
