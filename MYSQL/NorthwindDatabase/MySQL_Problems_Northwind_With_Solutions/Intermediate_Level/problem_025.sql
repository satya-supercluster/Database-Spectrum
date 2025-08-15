-- Problem 25: Employees and Their Territories
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display employee names and their territory descriptions.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT CONCAT(e.firstname, ' ', e.lastname) AS employeeName, t.territorydescription FROM Employee e JOIN EmployeeTerritory et ON e.employeeId = et.employeeId JOIN Territory t ON et.territoryId = t.territoryId;
