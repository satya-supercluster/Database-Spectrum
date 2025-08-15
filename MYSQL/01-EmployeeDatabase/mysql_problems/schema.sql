-- Employee Database Schema
-- Run this script to set up the database structure

DROP DATABASE IF EXISTS employee; 
CREATE DATABASE IF NOT EXISTS employee; 
USE employee;

SELECT 'CREATING DATABASE STRUCTURE' as 'INFO';

DROP TABLE IF EXISTS dept_emp, dept_manager, title, salary, employee, department;

CREATE TABLE employee (
    emp_no INT NOT NULL,
    birth_date DATE NOT NULL,
    first_name VARCHAR(14) NOT NULL,
    last_name VARCHAR(16) NOT NULL,
    gender ENUM ('M','F') NOT NULL,
    hire_date DATE NOT NULL,
    PRIMARY KEY (emp_no)
);

CREATE TABLE department (
    dept_no CHAR(4) NOT NULL,
    dept_name VARCHAR(40) NOT NULL,
    PRIMARY KEY (dept_no),
    UNIQUE KEY (dept_name)
);

CREATE TABLE dept_manager (
    emp_no INT NOT NULL,
    dept_no CHAR(4) NOT NULL,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    FOREIGN KEY (emp_no) REFERENCES employee (emp_no) ON DELETE CASCADE,
    FOREIGN KEY (dept_no) REFERENCES department (dept_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no,dept_no)
);

CREATE TABLE dept_emp (
    emp_no INT NOT NULL,
    dept_no CHAR(4) NOT NULL,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    FOREIGN KEY (emp_no) REFERENCES employee (emp_no) ON DELETE CASCADE,
    FOREIGN KEY (dept_no) REFERENCES department (dept_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no,dept_no)
);

CREATE TABLE title (
    emp_no INT NOT NULL,
    title VARCHAR(50) NOT NULL,
    from_date DATE NOT NULL,
    to_date DATE,
    FOREIGN KEY (emp_no) REFERENCES employee (emp_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no,title, from_date)
);

CREATE TABLE salary (
    emp_no INT NOT NULL,
    amount INT NOT NULL,
    from_date DATE NOT NULL,
    to_date DATE NOT NULL,
    FOREIGN KEY (emp_no) REFERENCES employee (emp_no) ON DELETE CASCADE,
    PRIMARY KEY (emp_no, from_date)
);

-- Views for convenience
CREATE OR REPLACE VIEW dept_emp_latest_date AS 
SELECT emp_no, MAX(from_date) AS from_date, MAX(to_date) AS to_date 
FROM dept_emp 
GROUP BY emp_no;

-- Shows only the current department for each employee
CREATE OR REPLACE VIEW current_dept_emp AS 
SELECT l.emp_no, dept_no, l.from_date, l.to_date 
FROM dept_emp d 
INNER JOIN dept_emp_latest_date l ON d.emp_no=l.emp_no AND d.from_date=l.from_date AND l.to_date = d.to_date;

SELECT 'DATABASE SCHEMA CREATED SUCCESSFULLY' as 'INFO';
