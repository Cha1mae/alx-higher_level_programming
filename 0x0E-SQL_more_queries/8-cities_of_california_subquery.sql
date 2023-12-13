-- 8-cities_of_california_subquery.sql
--  lists all the cities of California <3
SELECT `id`, `name`
  FROM `cities`
 WHERE `state_id` IN
       (SELECT `id`
	  FROM `states`
	 WHERE `name` = "California")
 ORDER BY `id`;
