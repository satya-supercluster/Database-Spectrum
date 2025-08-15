#!/usr/bin/env python3
"""
MySQL Problems Generator Script
Creates a structured directory with 100 MySQL problems based on employee database schema
"""

import os
import json

def create_directory_structure():
    """Create the main directory structure for MySQL problems"""
    base_dir = "mysql_problems"
    levels = {
        "01_basic": (1, 20),
        "02_intermediate": (21, 40), 
        "03_hard": (41, 60),
        "04_advanced": (61, 80),
        "05_complex": (81, 100)
    }
    
    # Create base directory
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Create level directories
    for level, (start, end) in levels.items():
        level_path = os.path.join(base_dir, level)
        if not os.path.exists(level_path):
            os.makedirs(level_path)
    
    return base_dir, levels

def get_problems():
    """Return dictionary of all 100 problems organized by difficulty"""
    return {
        "01_basic": [
            # Problems 1-20: Basic SELECT, WHERE, ORDER BY
            {
                "num": 1,
                "problem": "-- Problem 1: Basic SELECT\n-- Write a query to select all columns from the employee table\n-- Expected: Display all employee records\n\n"
            },
            {
                "num": 2,
                "problem": "-- Problem 2: SELECT specific columns\n-- Select only first_name and last_name from employee table\n-- Expected: Display employee names only\n\n"
            },
            {
                "num": 3,
                "problem": "-- Problem 3: WHERE clause with condition\n-- Find all employees with gender 'F'\n-- Expected: All female employees\n\n"
            },
            {
                "num": 4,
                "problem": "-- Problem 4: ORDER BY clause\n-- Select all employees ordered by hire_date in ascending order\n-- Expected: Employees sorted by hire date (oldest first)\n\n"
            },
            {
                "num": 5,
                "problem": "-- Problem 5: LIMIT clause\n-- Select first 10 employees from the employee table\n-- Expected: First 10 employee records\n\n"
            },
            {
                "num": 6,
                "problem": "-- Problem 6: COUNT function\n-- Count total number of employees in the database\n-- Expected: Single number representing total employee count\n\n"
            },
            {
                "num": 7,
                "problem": "-- Problem 7: DISTINCT keyword\n-- Find all unique department numbers from dept_emp table\n-- Expected: List of unique department numbers\n\n"
            },
            {
                "num": 8,
                "problem": "-- Problem 8: WHERE with date condition\n-- Find employees hired after '1990-01-01'\n-- Expected: Employees hired after 1990\n\n"
            },
            {
                "num": 9,
                "problem": "-- Problem 9: LIKE operator\n-- Find employees whose first name starts with 'A'\n-- Expected: All employees with first name beginning with A\n\n"
            },
            {
                "num": 10,
                "problem": "-- Problem 10: BETWEEN operator\n-- Find employees with emp_no between 10001 and 10010\n-- Expected: Employees with employee numbers in specified range\n\n"
            },
            {
                "num": 11,
                "problem": "-- Problem 11: IN operator\n-- Find employees with emp_no in (10001, 10005, 10009)\n-- Expected: Three specific employees\n\n"
            },
            {
                "num": 12,
                "problem": "-- Problem 12: ORDER BY DESC\n-- List all employees ordered by birth_date in descending order\n-- Expected: Employees sorted by birth date (youngest first)\n\n"
            },
            {
                "num": 13,
                "problem": "-- Problem 13: WHERE with multiple conditions (AND)\n-- Find male employees hired after '1985-01-01'\n-- Expected: Male employees hired after 1985\n\n"
            },
            {
                "num": 14,
                "problem": "-- Problem 14: WHERE with multiple conditions (OR)\n-- Find employees with first_name 'Mary' OR last_name 'Smith'\n-- Expected: Employees matching either condition\n\n"
            },
            {
                "num": 15,
                "problem": "-- Problem 15: IS NULL check\n-- Find all titles where to_date is NULL\n-- Expected: Current/active titles\n\n"
            },
            {
                "num": 16,
                "problem": "-- Problem 16: Basic GROUP BY\n-- Count employees by gender\n-- Expected: Count of male and female employees\n\n"
            },
            {
                "num": 17,
                "problem": "-- Problem 17: MIN and MAX functions\n-- Find the earliest and latest hire dates\n-- Expected: Two dates showing employment span\n\n"
            },
            {
                "num": 18,
                "problem": "-- Problem 18: AVG function\n-- Calculate average salary amount from salary table\n-- Expected: Single average salary value\n\n"
            },
            {
                "num": 19,
                "problem": "-- Problem 19: String functions - CONCAT\n-- Create full name by concatenating first_name and last_name\n-- Expected: Employee full names\n\n"
            },
            {
                "num": 20,
                "problem": "-- Problem 20: Date functions - YEAR\n-- Find employees hired in the year 1985\n-- Expected: All employees hired specifically in 1985\n\n"
            }
        ],
        
        "02_intermediate": [
            # Problems 21-40: JOINs, GROUP BY, HAVING, Subqueries
            {
                "num": 21,
                "problem": "-- Problem 21: INNER JOIN\n-- Join employee and dept_emp tables to show employee names with their department numbers\n-- Expected: Employee names with their department assignments\n\n"
            },
            {
                "num": 22,
                "problem": "-- Problem 22: Multiple JOINs\n-- Join employee, dept_emp, and department tables to show employee names with department names\n-- Expected: Employee names with readable department names\n\n"
            },
            {
                "num": 23,
                "problem": "-- Problem 23: LEFT JOIN\n-- Show all employees and their titles (including employees without titles)\n-- Expected: All employees with titles where available\n\n"
            },
            {
                "num": 24,
                "problem": "-- Problem 24: GROUP BY with HAVING\n-- Find departments with more than 50000 employees\n-- Expected: Department numbers with high employee count\n\n"
            },
            {
                "num": 25,
                "problem": "-- Problem 25: Subquery in WHERE\n-- Find employees who earn more than the average salary\n-- Expected: High-earning employees\n\n"
            },
            {
                "num": 26,
                "problem": "-- Problem 26: Correlated subquery\n-- Find employees who earn the maximum salary in their department\n-- Expected: Top earners per department\n\n"
            },
            {
                "num": 27,
                "problem": "-- Problem 27: EXISTS operator\n-- Find employees who have been managers\n-- Expected: Employees who appear in dept_manager table\n\n"
            },
            {
                "num": 28,
                "problem": "-- Problem 28: UNION operator\n-- Combine employee first names and last names into a single list of names\n-- Expected: Single column with all first and last names\n\n"
            },
            {
                "num": 29,
                "problem": "-- Problem 29: CASE statement\n-- Categorize employees as 'Senior' (hired before 1990) or 'Junior' (hired 1990 or after)\n-- Expected: Employee names with seniority category\n\n"
            },
            {
                "num": 30,
                "problem": "-- Problem 30: Self JOIN\n-- Find pairs of employees with the same birth date\n-- Expected: Employee pairs sharing birth dates\n\n"
            },
            {
                "num": 31,
                "problem": "-- Problem 31: Window functions - ROW_NUMBER\n-- Rank employees by salary within each department\n-- Expected: Employees with ranking numbers\n\n"
            },
            {
                "num": 32,
                "problem": "-- Problem 32: Date arithmetic\n-- Calculate age of employees at time of hire\n-- Expected: Employee names with hire age\n\n"
            },
            {
                "num": 33,
                "problem": "-- Problem 33: Multiple GROUP BY\n-- Count employees by department and gender\n-- Expected: Employee count breakdown by dept and gender\n\n"
            },
            {
                "num": 34,
                "problem": "-- Problem 34: Subquery in SELECT\n-- For each employee, show their salary and the average salary of their department\n-- Expected: Employee salary vs department average\n\n"
            },
            {
                "num": 35,
                "problem": "-- Problem 35: NOT EXISTS\n-- Find employees who have never been managers\n-- Expected: Non-management employees\n\n"
            },
            {
                "num": 36,
                "problem": "-- Problem 36: HAVING with aggregate functions\n-- Find departments where average salary is greater than 60000\n-- Expected: High-paying departments\n\n"
            },
            {
                "num": 37,
                "problem": "-- Problem 37: Complex WHERE with subquery\n-- Find employees hired in the same year as employee number 10001\n-- Expected: Employees with matching hire year\n\n"
            },
            {
                "num": 38,
                "problem": "-- Problem 38: JOIN with date conditions\n-- Find employees and their current titles (where title to_date is NULL or future)\n-- Expected: Employees with active titles\n\n"
            },
            {
                "num": 39,
                "problem": "-- Problem 39: String manipulation\n-- Find employees whose last name contains 'son' or 'sen'\n-- Expected: Employees with Nordic-style surnames\n\n"
            },
            {
                "num": 40,
                "problem": "-- Problem 40: Multiple CTEs (Common Table Expressions)\n-- Use CTEs to find the department with highest average salary\n-- Expected: Department name and average salary\n\n"
            }
        ],
        
        "03_hard": [
            # Problems 41-60: Complex JOINs, Advanced Analytics, Performance
            {
                "num": 41,
                "problem": "-- Problem 41: Complex aggregation\n-- Find the top 3 departments by total salary expenditure\n-- Expected: Department names with total salary costs\n\n"
            },
            {
                "num": 42,
                "problem": "-- Problem 42: Window functions - RANK\n-- Rank departments by average salary, handling ties appropriately\n-- Expected: Departments with proper ranking\n\n"
            },
            {
                "num": 43,
                "problem": "-- Problem 43: Recursive CTE simulation\n-- Find all employees and their management chain (using multiple self-joins)\n-- Expected: Employee hierarchy structure\n\n"
            },
            {
                "num": 44,
                "problem": "-- Problem 44: Pivoting data\n-- Create a report showing employee count by department and gender in pivot format\n-- Expected: Departments as rows, gender as columns\n\n"
            },
            {
                "num": 45,
                "problem": "-- Problem 45: Gap analysis\n-- Find periods where employees had no salary records\n-- Expected: Employee gaps in salary history\n\n"
            },
            {
                "num": 46,
                "problem": "-- Problem 46: Running totals\n-- Calculate running total of salary costs by hire date\n-- Expected: Cumulative salary costs over time\n\n"
            },
            {
                "num": 47,
                "problem": "-- Problem 47: Percentile calculation\n-- Find employees whose salary is in the top 10% of their department\n-- Expected: High-performing employees by department\n\n"
            },
            {
                "num": 48,
                "problem": "-- Problem 48: Complex date logic\n-- Find employees who changed departments more than twice\n-- Expected: Frequently transferred employees\n\n"
            },
            {
                "num": 49,
                "problem": "-- Problem 49: Advanced subqueries\n-- Find departments where no employee has ever earned more than 80000\n-- Expected: Lower-paying departments\n\n"
            },
            {
                "num": 50,
                "problem": "-- Problem 50: Lead/Lag simulation\n-- For each employee, show their current and previous salary\n-- Expected: Salary progression tracking\n\n"
            },
            {
                "num": 51,
                "problem": "-- Problem 51: Dynamic grouping\n-- Group employees into salary bands (0-40k, 40k-60k, 60k-80k, 80k+)\n-- Expected: Employee distribution across salary ranges\n\n"
            },
            {
                "num": 52,
                "problem": "-- Problem 52: Complex filtering\n-- Find employees who have held at least 3 different titles\n-- Expected: Career-diverse employees\n\n"
            },
            {
                "num": 53,
                "problem": "-- Problem 53: Time-series analysis\n-- Calculate month-over-month salary growth for each employee\n-- Expected: Salary progression rates\n\n"
            },
            {
                "num": 54,
                "problem": "-- Problem 54: Multiple window functions\n-- For each employee, show salary rank within department and overall\n-- Expected: Dual ranking system\n\n"
            },
            {
                "num": 55,
                "problem": "-- Problem 55: Complex joins with conditions\n-- Find employees who were promoted (title change) within 2 years of hiring\n-- Expected: Fast-tracked employees\n\n"
            },
            {
                "num": 56,
                "problem": "-- Problem 56: Statistical analysis\n-- Calculate salary standard deviation by department\n-- Expected: Salary variability metrics\n\n"
            },
            {
                "num": 57,
                "problem": "-- Problem 57: Seasonal analysis\n-- Analyze hiring patterns by month and year\n-- Expected: Seasonal hiring trends\n\n"
            },
            {
                "num": 58,
                "problem": "-- Problem 58: Cohort analysis\n-- Group employees by hire year and analyze retention patterns\n-- Expected: Hiring cohort analysis\n\n"
            },
            {
                "num": 59,
                "problem": "-- Problem 59: Advanced string processing\n-- Find employees with palindromic employee numbers when converted to string\n-- Expected: Employees with special ID patterns\n\n"
            },
            {
                "num": 60,
                "problem": "-- Problem 60: Multi-level aggregation\n-- Create a hierarchical report: Company > Department > Gender > Count\n-- Expected: Nested aggregation results\n\n"
            }
        ],
        
        "04_advanced": [
            # Problems 61-80: Performance Optimization, Complex Business Logic
            {
                "num": 61,
                "problem": "-- Problem 61: Performance optimization\n-- Write an optimized query to find top 10 highest paid employees using proper indexing strategy\n-- Expected: Efficient high-salary employee query\n-- Hint: Consider index on (amount DESC)\n\n"
            },
            {
                "num": 62,
                "problem": "-- Problem 62: Complex business logic\n-- Calculate employee tenure and categorize as: Intern (<1yr), Junior (1-3yr), Mid (3-7yr), Senior (7-15yr), Executive (15+yr)\n-- Expected: Employee tenure categorization\n\n"
            },
            {
                "num": 63,
                "problem": "-- Problem 63: Advanced window functions\n-- For each department, find employees whose salary is within 1 standard deviation of department mean\n-- Expected: Statistically normal salary employees\n\n"
            },
            {
                "num": 64,
                "problem": "-- Problem 64: Complex temporal logic\n-- Find overlapping employment periods for employees who worked in multiple departments simultaneously\n-- Expected: Employees with concurrent department roles\n\n"
            },
            {
                "num": 65,
                "problem": "-- Problem 65: Advanced analytics\n-- Calculate employee churn rate by department and year\n-- Expected: Departmental retention analytics\n\n"
            },
            {
                "num": 66,
                "problem": "-- Problem 66: Performance comparison\n-- Compare query performance between correlated subquery vs window function for ranking employees by salary\n-- Expected: Two equivalent queries with performance notes\n\n"
            },
            {
                "num": 67,
                "problem": "-- Problem 67: Data quality analysis\n-- Identify potential data inconsistencies in employee records (impossible ages, future dates, etc.)\n-- Expected: Data validation report\n\n"
            },
            {
                "num": 68,
                "problem": "-- Problem 68: Complex aggregation patterns\n-- Create a salary distribution histogram with 10 equal-width bins\n-- Expected: Salary frequency distribution\n\n"
            },
            {
                "num": 69,
                "problem": "-- Problem 69: Advanced date calculations\n-- Find employees who have worked continuously (no gaps) for more than 10 years\n-- Expected: Long-tenure continuous employees\n\n"
            },
            {
                "num": 70,
                "problem": "-- Problem 70: Simulation of advanced functions\n-- Implement a dense_rank() equivalent using basic SQL functions\n-- Expected: Manual ranking implementation\n\n"
            },
            {
                "num": 71,
                "problem": "-- Problem 71: Complex reporting\n-- Generate a management dashboard showing: total employees, avg salary, top department, newest hire\n-- Expected: Executive summary metrics\n\n"
            },
            {
                "num": 72,
                "problem": "-- Problem 72: Advanced pattern matching\n-- Find employees with consecutive employee numbers who share the same last name\n-- Expected: Potentially related employees\n\n"
            },
            {
                "num": 73,
                "problem": "-- Problem 73: Efficiency optimization\n-- Optimize a query that finds departments with salary growth > 20% year-over-year\n-- Expected: Optimized departmental growth analysis\n\n"
            },
            {
                "num": 74,
                "problem": "-- Problem 74: Complex mathematical operations\n-- Calculate the Gini coefficient for salary distribution by department\n-- Expected: Salary inequality measurement\n\n"
            },
            {
                "num": 75,
                "problem": "-- Problem 75: Advanced time-series\n-- Detect salary anomalies (outliers) using statistical methods\n-- Expected: Unusual salary changes identification\n\n"
            },
            {
                "num": 76,
                "problem": "-- Problem 76: Multi-dimensional analysis\n-- Create a cube-like analysis: Department x Gender x Title Level with salary metrics\n-- Expected: Multi-dimensional salary analysis\n\n"
            },
            {
                "num": 77,
                "problem": "-- Problem 77: Performance tuning\n-- Write queries to identify missing indexes by analyzing query patterns\n-- Expected: Index optimization recommendations\n\n"
            },
            {
                "num": 78,
                "problem": "-- Problem 78: Advanced business metrics\n-- Calculate employee productivity score based on salary progression and tenure\n-- Expected: Performance scoring algorithm\n\n"
            },
            {
                "num": 79,
                "problem": "-- Problem 79: Complex data transformation\n-- Normalize salary data to account for inflation using year-based multipliers\n-- Expected: Inflation-adjusted salary comparison\n\n"
            },
            {
                "num": 80,
                "problem": "-- Problem 80: Advanced optimization\n-- Create a single query that combines multiple CTEs to analyze employee lifecycle comprehensively\n-- Expected: Comprehensive employee analytics\n\n"
            }
        ],
        
        "05_complex": [
            # Problems 81-100: Enterprise-level Complex Queries
            {
                "num": 81,
                "problem": "-- Problem 81: Enterprise reporting system\n-- Build a comprehensive employee analytics dashboard with 15+ KPIs including:\n-- Total headcount, gender distribution, avg tenure, salary quartiles, department sizes,\n-- promotion rates, retention rates, hiring trends, age demographics, title distribution\n-- Expected: Executive-level analytics dashboard\n\n"
            },
            {
                "num": 82,
                "problem": "-- Problem 82: Advanced workforce analytics\n-- Create a query to predict employee flight risk based on:\n-- Below-average salary progression, long tenure without promotion, department turnover rates\n-- Expected: Employee retention risk assessment\n\n"
            },
            {
                "num": 83,
                "problem": "-- Problem 83: Complex organizational analysis\n-- Map the complete organizational hierarchy and calculate span of control metrics\n-- Include direct reports, indirect reports, and management layers\n-- Expected: Organizational structure analysis\n\n"
            },
            {
                "num": 84,
                "problem": "-- Problem 84: Advanced performance benchmarking\n-- Create a comprehensive salary benchmarking system comparing:\n-- Internal equity, market positioning, pay compression analysis, and career progression patterns\n-- Expected: Compensation analytics framework\n\n"
            },
            {
                "num": 85,
                "problem": "-- Problem 85: Sophisticated time-series forecasting\n-- Analyze historical hiring patterns and project future headcount needs by department\n-- Include seasonal adjustments and trend analysis\n-- Expected: Workforce planning analytics\n\n"
            },
            {
                "num": 86,
                "problem": "-- Problem 86: Advanced data mining query\n-- Identify hidden patterns in employee data such as:\n-- Correlation between hire date and performance, geographic clustering, career path similarities\n-- Expected: Pattern discovery analysis\n\n"
            },
            {
                "num": 87,
                "problem": "-- Problem 87: Complex financial modeling\n-- Calculate total cost of ownership per employee including:\n-- Salary costs, benefit allocation, training investments, and turnover costs\n-- Expected: Employee ROI analysis\n\n"
            },
            {
                "num": 88,
                "problem": "-- Problem 88: Enterprise data quality framework\n-- Create a comprehensive data quality assessment covering:\n-- Completeness, accuracy, consistency, timeliness, and validity across all tables\n-- Expected: Data governance metrics\n\n"
            },
            {
                "num": 89,
                "problem": "-- Problem 89: Advanced segmentation analysis\n-- Perform employee segmentation using multiple criteria:\n-- Performance clusters, career stage groupings, compensation bands, and engagement levels\n-- Expected: Employee persona analysis\n\n"
            },
            {
                "num": 90,
                "problem": "-- Problem 90: Sophisticated audit and compliance\n-- Create audit trails and compliance reports for:\n-- Salary changes, position changes, equal pay analysis, and regulatory reporting\n-- Expected: Compliance monitoring system\n\n"
            },
            {
                "num": 91,
                "problem": "-- Problem 91: Machine learning preparation\n-- Prepare feature engineering for ML models predicting:\n-- Employee success, promotion likelihood, and retention probability\n-- Expected: ML-ready dataset generation\n\n"
            },
            {
                "num": 92,
                "problem": "-- Problem 92: Advanced optimization challenge\n-- Optimize a complex query involving all tables with multiple window functions,\n-- subqueries, and CTEs while maintaining sub-second performance\n-- Expected: Performance-optimized complex analytics\n\n"
            },
            {
                "num": 93,
                "problem": "-- Problem 93: Real-time analytics simulation\n-- Design queries for real-time dashboard updates including:\n-- Live headcount changes, salary adjustments, and departmental metrics\n-- Expected: Real-time monitoring queries\n\n"
            },
            {
                "num": 94,
                "problem": "-- Problem 94: Advanced statistical modeling\n-- Implement statistical functions for employee analytics:\n-- Regression analysis, correlation coefficients, and predictive scoring\n-- Expected: Statistical analysis framework\n\n"
            },
            {
                "num": 95,
                "problem": "-- Problem 95: Complex scenario modeling\n-- Create what-if scenarios for workforce planning:\n-- Budget constraint modeling, headcount optimization, and cost-benefit analysis\n-- Expected: Strategic planning analytics\n\n"
            },
            {
                "num": 96,
                "problem": "-- Problem 96: Enterprise integration queries\n-- Design queries that would integrate with external systems:\n-- HRIS synchronization, payroll system integration, and external benchmarking data\n-- Expected: Integration-ready query framework\n\n"
            },
            {
                "num": 97,
                "problem": "-- Problem 97: Advanced security and privacy\n-- Implement data privacy and security measures in queries:\n-- Role-based data access, PII masking, and audit logging\n-- Expected: Security-compliant query patterns\n\n"
            },
            {
                "num": 98,
                "problem": "-- Problem 98: Comprehensive business intelligence\n-- Create a master query combining all business intelligence requirements:\n-- Operational metrics, strategic KPIs, predictive insights, and actionable recommendations\n-- Expected: Complete BI solution\n\n"
            },
            {
                "num": 99,
                "problem": "-- Problem 99: Performance stress testing\n-- Design queries to test database performance under various loads:\n-- Concurrent user simulation, large dataset processing, and memory optimization\n-- Expected: Performance testing framework\n\n"
            },
            {
                "num": 100,
                "problem": "-- Problem 100: Ultimate challenge - Complete HR Analytics Platform\n-- Design a complete query-based HR analytics platform including:\n-- Data warehouse design, ETL processes, real-time analytics, predictive modeling,\n-- compliance reporting, executive dashboards, and automated insights\n-- This should demonstrate mastery of all MySQL concepts and real-world application\n-- Expected: Enterprise-grade HR analytics solution\n\n"
            }
        ]
    }

def create_problem_files(base_dir, levels, problems):
    """Create individual SQL files for each problem"""
    
    for level, (start, end) in levels.items():
        level_path = os.path.join(base_dir, level)
        level_problems = problems[level]
        
        for problem_data in level_problems:
            problem_num = problem_data["num"]
            problem_content = problem_data["problem"]
            
            filename = f"problem_{problem_num:03d}.sql"
            filepath = os.path.join(level_path, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(problem_content)
    
    print(f"Created 100 problem files in {base_dir}/")

def create_readme(base_dir):
    """Create README file with overview"""
    readme_content = """# MySQL Problems - Employee Database

This collection contains 100 MySQL problems based on the employee database schema, organized by difficulty level.

## Database Schema
The problems are based on an employee database with the following tables:
- `employee`: Employee basic information
- `department`: Department information  
- `dept_emp`: Employee-department relationships
- `dept_manager`: Department managers
- `title`: Employee titles/positions
- `salary`: Employee salary history

## Problem Structure
- **01_basic** (Problems 1-20): Basic SELECT, WHERE, ORDER BY, simple functions
- **02_intermediate** (Problems 21-40): JOINs, GROUP BY, HAVING, subqueries
- **03_hard** (Problems 41-60): Complex JOINs, window functions, advanced analytics
- **04_advanced** (Problems 61-80): Performance optimization, complex business logic
- **05_complex** (Problems 81-100): Enterprise-level complex queries

## How to Use
1. Set up the employee database using the provided schema
2. Start with basic problems and progress through difficulty levels
3. Each SQL file contains the problem statement as comments
4. Try to solve each problem before looking up solutions
5. Focus on query optimization for advanced problems

## Learning Objectives
- Master MySQL query writing from basic to advanced levels
- Understand database performance optimization
- Learn real-world business analytics patterns
- Practice complex data analysis scenarios
- Develop enterprise-level SQL skills

Good luck with your MySQL journey! 🚀
"""
    
    readme_path = os.path.join(base_dir, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"Created README.md in {base_dir}/")

def create_schema_file(base_dir):
    """Create the database schema file"""
    schema_content = """-- Employee Database Schema
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
"""
    
    schema_path = os.path.join(base_dir, "schema.sql")
    with open(schema_path, 'w', encoding='utf-8') as f:
        f.write(schema_content)
    
    print(f"Created schema.sql in {base_dir}/")

def main():
    """Main function to generate all MySQL problems"""
    print("🚀 Starting MySQL Problems Generator...")
    
    # Create directory structure
    base_dir, levels = create_directory_structure()
    print(f"✅ Created directory structure in {base_dir}/")
    
    # Get all problems
    problems = get_problems()
    
    # Create problem files
    create_problem_files(base_dir, levels, problems)
    
    # Create additional files
    create_readme(base_dir)
    create_schema_file(base_dir)
    
    # Create summary
    create_summary_file(base_dir, levels)
    
    print("\n🎉 Successfully generated 100 MySQL problems!")
    print(f"📁 Location: {os.path.abspath(base_dir)}")
    print("\n📊 Summary:")
    print("- 01_basic: 20 problems (Basic SELECT, WHERE, ORDER BY)")
    print("- 02_intermediate: 20 problems (JOINs, GROUP BY, Subqueries)")  
    print("- 03_hard: 20 problems (Complex JOINs, Window Functions)")
    print("- 04_advanced: 20 problems (Performance Optimization)")
    print("- 05_complex: 20 problems (Enterprise-level Queries)")
    print(f"\n📖 Check {base_dir}/README.md for detailed instructions")
    print(f"🗃️  Run {base_dir}/schema.sql to set up the database")

def create_summary_file(base_dir, levels):
    """Create a summary file with problem categories"""
    summary_content = """# MySQL Problems Summary

## Quick Reference Guide

### Basic Level (Problems 1-20)
Focus: Fundamental SQL operations
- SELECT statements and column selection
- WHERE clauses and filtering
- ORDER BY and LIMIT
- Basic aggregate functions (COUNT, AVG, MIN, MAX)
- String operations and date functions

### Intermediate Level (Problems 21-40)  
Focus: Multi-table operations and analysis
- INNER, LEFT, RIGHT JOINs
- GROUP BY with HAVING clauses
- Subqueries and correlated subqueries
- UNION operations
- CASE statements and conditional logic

### Hard Level (Problems 41-60)
Focus: Advanced analytics and complex operations
- Window functions (ROW_NUMBER, RANK, DENSE_RANK)
- Complex aggregations and pivoting
- Advanced date calculations
- Statistical analysis queries
- Performance considerations

### Advanced Level (Problems 61-80)
Focus: Optimization and complex business logic
- Query optimization techniques
- Index usage strategies  
- Advanced window functions
- Complex temporal logic
- Data quality and validation

### Complex Level (Problems 81-100)
Focus: Enterprise-level solutions
- Comprehensive analytics dashboards
- Predictive analytics preparation
- Performance stress testing
- Business intelligence frameworks
- Real-world enterprise scenarios

## Problem Categories by Topic

### JOIN Operations: 21, 22, 23, 30, 38, 43, 55, 64
### Window Functions: 31, 42, 47, 50, 54, 63
### Date/Time Analysis: 20, 32, 45, 48, 53, 57, 58, 69
### Performance Optimization: 61, 66, 73, 77, 92
### Statistical Analysis: 47, 56, 63, 68, 74, 75, 94
### Business Intelligence: 71, 81, 89, 98
### Data Quality: 67, 88, 97

## Tips for Success
1. Start with basic problems and build your skills progressively
2. Focus on understanding the business logic behind each query
3. Practice writing efficient, readable queries
4. Test your queries with sample data
5. Pay attention to performance implications in advanced problems
"""
    
    summary_path = os.path.join(base_dir, "SUMMARY.md")
    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(summary_content)
    
    print(f"Created SUMMARY.md in {base_dir}/")

if __name__ == "__main__":
    main()