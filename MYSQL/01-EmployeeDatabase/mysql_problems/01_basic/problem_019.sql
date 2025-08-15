-- Problem 19: String functions - CONCAT
-- Create full name by concatenating first_name and last_name
-- Expected: Employee full names

SELECT CONCAT(first_name ,' ', last_name) as "full name"
from employee