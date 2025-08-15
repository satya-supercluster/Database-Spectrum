-- Problem 14: WHERE with multiple conditions (OR)
-- Find employees with first_name 'Mary' OR last_name 'Smith'
-- Expected: Employees matching either condition

SELECT * from employee
where first_name = "Mary" or last_name = "Smith"