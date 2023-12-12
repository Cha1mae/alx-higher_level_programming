-- List all records with dumb score
-- This will help us focus on the top performers
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
