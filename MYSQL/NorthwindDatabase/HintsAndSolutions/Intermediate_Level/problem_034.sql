-- Problem 34: Region-wise Territory Count
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to count the number of territories in each region.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT r.regiondescription, COUNT(t.territoryId) AS territoryCount FROM Region r LEFT JOIN Territory t ON r.regionId = t.regionId GROUP BY r.regionId, r.regiondescription;
