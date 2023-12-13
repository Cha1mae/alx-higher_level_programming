-- 5-unique_id.sql
-- creates the table id_not_null on my server ig
CREATE TABLE IF NOT EXISTS unique_id (
    id INT UNIQUE DEFAULT 1,
    name VARCHAR(256)
);
