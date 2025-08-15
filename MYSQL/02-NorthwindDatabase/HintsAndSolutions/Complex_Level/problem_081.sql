-- Problem 81: Advanced Seasonal Decomposition Analysis
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to decompose sales data into trend, seasonal, and residual components.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH MonthlySales AS (SELECT DATE_FORMAT(s.orderDate, '%Y-%m') AS month, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS monthly_sales FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY DATE_FORMAT(s.orderDate, '%Y-%m')), TrendAnalysis AS (SELECT month, monthly_sales, AVG(monthly_sales) OVER (ORDER BY month ROWS BETWEEN 5 PRECEDING AND 5 FOLLOWING) AS trend FROM MonthlySales), SeasonalDecomposition AS (SELECT month, monthly_sales, trend, monthly_sales / NULLIF(trend, 0) AS seasonal_factor, monthly_sales - trend AS residual FROM TrendAnalysis) SELECT SUBSTRING(month, 6, 2) AS month_num, AVG(seasonal_factor) AS avg_seasonal_factor, STDDEV(residual) AS residual_variance FROM SeasonalDecomposition GROUP BY SUBSTRING(month, 6, 2) ORDER BY month_num;
