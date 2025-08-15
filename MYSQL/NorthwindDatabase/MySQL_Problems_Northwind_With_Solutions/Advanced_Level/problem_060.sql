-- Problem 60: Product Portfolio Optimization
-- Level: Advanced
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to analyze product portfolio performance and identify optimization opportunities.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH ProductPerformance AS (SELECT p.productId, p.productName, c.categoryName, p.unitPrice, p.unitsInStock, SUM(od.quantity) AS totalSold, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue, COUNT(DISTINCT od.orderId) AS orderFrequency FROM Product p JOIN Category c ON p.categoryId = c.categoryId LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName, c.categoryName, p.unitPrice, p.unitsInStock), PortfolioAnalysis AS (SELECT productName, categoryName, unitPrice, unitsInStock, totalSold, totalRevenue, orderFrequency, CASE WHEN totalRevenue > (SELECT AVG(totalRevenue) FROM ProductPerformance) AND orderFrequency > (SELECT AVG(orderFrequency) FROM ProductPerformance) THEN 'Star' WHEN totalRevenue > (SELECT AVG(totalRevenue) FROM ProductPerformance) THEN 'Cash Cow' WHEN orderFrequency > (SELECT AVG(orderFrequency) FROM ProductPerformance) THEN 'Question Mark' ELSE 'Dog' END AS portfolioCategory FROM ProductPerformance) SELECT portfolioCategory, COUNT(*) AS productCount, AVG(totalRevenue) AS avgRevenue, AVG(orderFrequency) AS avgFrequency FROM PortfolioAnalysis GROUP BY portfolioCategory ORDER BY FIELD(portfolioCategory, 'Star', 'Cash Cow', 'Question Mark', 'Dog');
