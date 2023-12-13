-- 5-unique_id.sql
-- creates the table id_not_null on my server ig
CREATE TABLE IF NOT EXISTS `id_not_null` 
(
    `id`   INT          DEFAULT 1,
    `name` VARCHAR(256)
);
