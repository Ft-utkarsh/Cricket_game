-- MySQL Database Setup for Cricket Game
-- Run this script in MySQL Workbench or MySQL Command Line

-- Create database
CREATE DATABASE IF NOT EXISTS cricket_db;

-- Use the database
USE cricket_db;

-- Create cricket table to store game records
CREATE TABLE IF NOT EXISTS cricket(
    sno INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    name VARCHAR(25) NOT NULL,
    run INT NOT NULL,
    status VARCHAR(10) NOT NULL
);

-- Create login table for user authentication
CREATE TABLE IF NOT EXISTS login(
    username VARCHAR(25) NOT NULL PRIMARY KEY,
    password VARCHAR(25) NOT NULL
);

-- Create sno table to track the last serial number
CREATE TABLE IF NOT EXISTS sno(
    id INT NOT NULL
);

-- Insert default login credentials (admin/ng)
INSERT INTO login (username, password) VALUES ('admin', 'ng');

-- Initialize sno table with starting value
INSERT INTO sno (id) VALUES (0);

-- Display all tables
SHOW TABLES;

-- Display structure of each table
DESCRIBE cricket;
DESCRIBE login;
DESCRIBE sno;

-- Display initial data
SELECT * FROM login;
SELECT * FROM sno;
