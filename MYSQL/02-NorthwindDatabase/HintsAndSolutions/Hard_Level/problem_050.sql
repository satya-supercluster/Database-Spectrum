-- Problem 50: Territory Performance Comparison
-- Level: Hard
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to compare territory performance including sales, employee count, and customer coverage.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH TerritoryStats AS (SELECT t.territoryId, t.territorydescription, r.regiondescription, COUNT(DISTINCT et.employeeId) AS employeeCount FROM Territory t JOIN Region r ON t.regionId = r.regionId LEFT JOIN EmployeeTerritory et ON t.territoryId = et.territoryId GROUP BY t.territoryId, t.territorydescription, r.regiondescription) SELECT ts.territorydescription, ts.regiondescription, ts.employeeCount FROM TerritoryStats ts ORDER BY ts.employeeCount DESC;
