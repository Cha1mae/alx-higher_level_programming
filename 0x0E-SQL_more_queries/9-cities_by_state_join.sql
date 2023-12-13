-- 9-cities_by_state_join.sql
--sort in order of < cities.id.
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
