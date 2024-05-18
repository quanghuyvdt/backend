DROP SCHEMA IF EXISTS midterm ;
CREATE SCHEMA midterm;
USE midterm;

CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    yob INT,
    gender INT,
    university VARCHAR(255),
    major VARCHAR(255)
);