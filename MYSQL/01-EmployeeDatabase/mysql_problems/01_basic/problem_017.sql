-- Problem 17: MIN and MAX functions
-- Find the earliest and latest hire dates
-- Expected: Two dates showing employment span

SELECT min(hire_date), max(hire_date)
from employee 