-- Display the max temperature of each state
-- by name i guess
SELECT state, MAX(temperature) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
