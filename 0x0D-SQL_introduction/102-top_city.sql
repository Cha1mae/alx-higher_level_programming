-- Display the top 3 of cities temperature during July and August
-- will know wich city is hot 
SELECT city, AVG(temperature) AS avg_temp FROM temperatures WHERE MONTH(date) IN (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
