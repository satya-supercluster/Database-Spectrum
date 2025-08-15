-- Problem 16: Basic GROUP BY
-- Count employees by gender
-- Expected: Count of male and female employees

SELECT count(*)
from employee
GROUP BY gender