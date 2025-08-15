-- Problem 11: IN operator
-- Find employees with emp_no in (10001, 10005, 10009)
-- Expected: Three specific employees

select *
from employee
where emp_no IN (10001,10005,10009)