-- Problem 9: LIKE operator
-- Find employees whose first name starts with 'A'
-- Expected: All employees with first name beginning with A

select * from employee
where first_name like 'A%'