-- Problem 23: LEFT JOIN
-- Show all employees and their titles (including employees without titles)
-- Expected: All employees with titles where available

-- SELECT * FROM employee AS e
-- LEFT JOIN title AS t ON e.emp_no = t.emp_no;

SELECT e.*, t.title
FROM employee AS e
LEFT JOIN title AS t ON e.emp_no = t.emp_no;