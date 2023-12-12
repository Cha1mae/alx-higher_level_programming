-- List all records of the table second_table with a name value
-- Results are displayed by descending score to identify the Alphas
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
