-- Problem 42: Top 3 Products in Each Category by Sales
-- Level: Hard
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to find the top 3 best-selling products in each category by quantity sold.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH ProductSales AS (SELECT p.categoryId, p.productName, SUM(od.quantity) AS totalSold FROM Product p JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.categoryId, p.productId, p.productName), RankedProducts AS (SELECT categoryId, productName, totalSold, ROW_NUMBER() OVER (PARTITION BY categoryId ORDER BY totalSold DESC) AS rank FROM ProductSales) SELECT c.categoryName, rp.productName, rp.totalSold FROM RankedProducts rp JOIN Category c ON rp.categoryId = c.categoryId WHERE rp.rank <= 3;
