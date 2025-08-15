-- Problem 20: Date functions - YEAR
-- Find employees hired in the year 1985
-- Expected: All employees hired specifically in 1985

SELECT * from employee
where hire_date >= '1985-01-01' and hire_date <= '1985-12-31'