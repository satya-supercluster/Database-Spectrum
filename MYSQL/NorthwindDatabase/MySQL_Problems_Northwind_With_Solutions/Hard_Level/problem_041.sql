-- Problem 41: Running Total of Orders by Month
-- Level: Hard
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to calculate running total of orders by month for each year.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT YEAR(orderDate) AS year, MONTH(orderDate) AS month, COUNT(*) AS monthlyOrders, SUM(COUNT(*)) OVER (PARTITION BY YEAR(orderDate) ORDER BY MONTH(orderDate)) AS runningTotal FROM SalesOrder GROUP BY YEAR(orderDate), MONTH(orderDate) ORDER BY year, month;
