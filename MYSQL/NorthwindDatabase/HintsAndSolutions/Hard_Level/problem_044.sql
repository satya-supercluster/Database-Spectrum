-- Problem 44: Quarterly Sales Growth
-- Level: Hard
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to calculate quarter-over-quarter growth in order values.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH QuarterlySales AS (SELECT YEAR(s.orderDate) AS year, QUARTER(s.orderDate) AS quarter, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalSales FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY YEAR(s.orderDate), QUARTER(s.orderDate)), SalesWithLag AS (SELECT year, quarter, totalSales, LAG(totalSales) OVER (ORDER BY year, quarter) AS prevQuarterSales FROM QuarterlySales) SELECT year, quarter, totalSales, prevQuarterSales, CASE WHEN prevQuarterSales IS NOT NULL THEN ((totalSales - prevQuarterSales) / prevQuarterSales) * 100 ELSE NULL END AS growthPercent FROM SalesWithLag ORDER BY year, quarter;
