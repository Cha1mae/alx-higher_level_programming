-- 0-privileges.sql
-- list of priviledge of the users
SELECT CONCAT('\'',user,'\'@\'',host,'\'') AS User, 
       Select_priv, Insert_priv, Update_priv, Delete_priv, Create_priv, Drop_priv 
FROM mysql.user 
WHERE user IN ('user_0d_1', 'user_0d_2');
