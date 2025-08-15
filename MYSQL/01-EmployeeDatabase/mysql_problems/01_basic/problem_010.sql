-- Problem 10: BETWEEN operator
-- Find employees with emp_no between 10001 and 10010
-- Expected: Employees with employee numbers in specified range

select * from employee
where emp_no>=10001 and emp_no<=10010