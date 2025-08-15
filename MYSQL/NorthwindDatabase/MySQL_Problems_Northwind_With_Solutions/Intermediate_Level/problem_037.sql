-- Problem 37: Employee Hierarchy
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display employees with their manager names.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT e1.firstname + ' ' + e1.lastname AS employee, e2.firstname + ' ' + e2.lastname AS manager FROM Employee e1 LEFT JOIN Employee e2 ON e1.mgrId = e2.employeeId;
