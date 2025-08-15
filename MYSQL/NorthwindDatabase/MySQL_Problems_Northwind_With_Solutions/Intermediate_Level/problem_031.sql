-- Problem 31: Employees Hired in Same Year
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to find employees hired in the same year, grouped by hire year.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT YEAR(hireDate) AS hireYear, COUNT(*) AS employeeCount, GROUP_CONCAT(CONCAT(firstname, ' ', lastname)) AS employees FROM Employee GROUP BY YEAR(hireDate) HAVING COUNT(*) > 1;
