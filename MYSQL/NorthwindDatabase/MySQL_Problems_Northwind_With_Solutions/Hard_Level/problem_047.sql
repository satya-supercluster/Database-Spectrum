-- Problem 47: Inventory Turnover Analysis
-- Level: Hard
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to calculate inventory turnover ratio for each product.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH ProductSales AS (SELECT p.productId, p.productName, p.unitsInStock, SUM(od.quantity) AS totalSold FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName, p.unitsInStock) SELECT productName, unitsInStock, totalSold, CASE WHEN unitsInStock > 0 THEN totalSold / unitsInStock ELSE NULL END AS turnoverRatio FROM ProductSales ORDER BY turnoverRatio DESC;
