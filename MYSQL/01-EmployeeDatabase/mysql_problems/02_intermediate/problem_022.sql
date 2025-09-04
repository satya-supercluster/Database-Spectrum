-- Problem 22: Multiple JOINs
-- Join employee, dept_emp, and department tables to show employee names with department names
-- Expected: Employee names with readable department names

SELECT CONCAT(e.first_name, ' ', e.last_name) AS employee_name, d.dept_name
FROM employee as e
INNER JOIN dept_emp as de ON e.emp_no = de.emp_no
INNER JOIN department as d ON de.dept_no = d.dept_no;