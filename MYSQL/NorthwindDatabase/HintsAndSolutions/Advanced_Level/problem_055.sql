-- Problem 55: ABC Analysis for Inventory Management
-- Level: Advanced
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to perform ABC analysis to categorize products based on their revenue contribution.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH ProductRevenue AS (SELECT p.productId, p.productName, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue FROM Product p JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName), RevenueWithPercentage AS (SELECT productId, productName, totalRevenue, totalRevenue / SUM(totalRevenue) OVER () * 100 AS revenuePercentage, SUM(totalRevenue) OVER (ORDER BY totalRevenue DESC) / SUM(totalRevenue) OVER () * 100 AS cumulativePercentage FROM ProductRevenue), ABCClassification AS (SELECT productId, productName, totalRevenue, revenuePercentage, cumulativePercentage, CASE WHEN cumulativePercentage <= 80 THEN 'A' WHEN cumulativePercentage <= 95 THEN 'B' ELSE 'C' END AS abcCategory FROM RevenueWithPercentage) SELECT abcCategory, COUNT(*) AS productCount, SUM(totalRevenue) AS categoryRevenue, AVG(revenuePercentage) AS avgRevenuePercentage FROM ABCClassification GROUP BY abcCategory ORDER BY FIELD(abcCategory, 'A', 'B', 'C');
