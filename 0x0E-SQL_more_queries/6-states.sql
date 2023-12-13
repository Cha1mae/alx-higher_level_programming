-- 6-states.sql
-- with the state table this create the table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas");
