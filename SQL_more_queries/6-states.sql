-- Create the database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Select the database
USE hbtn_0d_usa;

-- Create the table states
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
