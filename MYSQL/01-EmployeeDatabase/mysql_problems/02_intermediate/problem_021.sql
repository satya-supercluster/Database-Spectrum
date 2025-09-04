-- Problem 21: INNER JOIN
-- Join employee and dept_emp tables to show employee names with their department numbers
-- Expected: Employee names with their department assignments

SELECT CONCAT(e.first_name, ' ', e.last_name) AS employee_name, de.dept_no
FROM employee as e
INNER JOIN dept_emp as de ON e.emp_no = de.emp_no;