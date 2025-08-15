-- Problem 15: Employee First and Last Names
-- Level: Basic
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display employee first names and last names concatenated.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT CONCAT(firstname, ' ', lastname) AS fullName FROM Employee;
