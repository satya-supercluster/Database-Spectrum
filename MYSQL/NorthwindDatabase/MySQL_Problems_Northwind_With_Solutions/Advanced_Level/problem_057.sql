-- Problem 57: Sales Forecasting Using Moving Averages
-- Level: Advanced
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to calculate 3-month and 6-month moving averages for sales forecasting.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH MonthlySales AS (SELECT DATE_FORMAT(s.orderDate, '%Y-%m') AS month, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS monthlySales FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY DATE_FORMAT(s.orderDate, '%Y-%m')), MovingAverages AS (SELECT month, monthlySales, AVG(monthlySales) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS ma3, AVG(monthlySales) OVER (ORDER BY month ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) AS ma6, LAG(monthlySales, 1) OVER (ORDER BY month) AS prevMonthSales FROM MonthlySales) SELECT month, monthlySales, ma3, ma6, CASE WHEN prevMonthSales IS NOT NULL THEN ((monthlySales - prevMonthSales) / prevMonthSales) * 100 ELSE NULL END AS monthOverMonthGrowth FROM MovingAverages ORDER BY month;
