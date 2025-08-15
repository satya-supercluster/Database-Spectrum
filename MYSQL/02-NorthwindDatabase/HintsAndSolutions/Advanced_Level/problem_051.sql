-- Problem 51: Dynamic Pricing Analysis
-- Level: Advanced
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to analyze price changes over time and their impact on sales volume.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH PriceAnalysis AS (SELECT p.productId, p.productName, p.unitPrice AS currentPrice, od.unitPrice AS soldPrice, od.quantity, s.orderDate FROM Product p JOIN OrderDetail od ON p.productId = od.productId JOIN SalesOrder s ON od.orderId = s.orderId), PriceImpact AS (SELECT productName, soldPrice, SUM(quantity) AS totalQuantity, COUNT(*) AS orderCount, (soldPrice - MIN(soldPrice) OVER (PARTITION BY productId)) / MIN(soldPrice) OVER (PARTITION BY productId) * 100 AS priceChangePercent FROM PriceAnalysis GROUP BY productId, productName, soldPrice) SELECT productName, soldPrice, totalQuantity, orderCount, priceChangePercent FROM PriceImpact ORDER BY productName, soldPrice;
