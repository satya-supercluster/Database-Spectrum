-- Problem 49: Seasonal Sales Pattern Analysis
-- Level: Hard
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to analyze seasonal sales patterns by comparing monthly sales across years.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT MONTH(s.orderDate) AS month, MONTHNAME(s.orderDate) AS monthName, YEAR(s.orderDate) AS year, COUNT(s.orderId) AS orderCount, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalSales, AVG(SUM(od.quantity * od.unitPrice * (1 - od.discount))) OVER (PARTITION BY MONTH(s.orderDate)) AS avgMonthlySales FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY YEAR(s.orderDate), MONTH(s.orderDate), MONTHNAME(s.orderDate) ORDER BY month, year;
