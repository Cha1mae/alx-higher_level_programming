-- 0-privileges.sql
-- list of priviledge of the users
SELECT CONCAT('SHOW GRANTS FOR ''', user, '''@''', host, ''';') 
FROM mysql.user 
WHERE user IN ('user_0d_1', 'user_0d_2');
