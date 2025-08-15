-- Problem 13: WHERE with multiple conditions (AND)
-- Find male employees hired after '1985-01-01'
-- Expected: Male employees hired after 1985

SELECT * FROM employee
where gender = 'M' and hire_date > '1985-01-01'