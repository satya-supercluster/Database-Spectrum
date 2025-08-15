-- Problem 65: Predictive Analytics for Sales Forecasting
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query implementing time series analysis with trend and seasonality components for sales forecasting.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH DailySales AS (SELECT DATE(s.orderDate) AS saleDate, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS dailySales FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY DATE(s.orderDate)), TimeSeriesData AS (SELECT saleDate, dailySales, ROW_NUMBER() OVER (ORDER BY saleDate) AS timeIndex, DAYOFWEEK(saleDate) AS dayOfWeek, MONTH(saleDate) AS month, QUARTER(saleDate) AS quarter FROM DailySales), MovingAverages AS (SELECT saleDate, dailySales, timeIndex, dayOfWeek, month, quarter, AVG(dailySales) OVER (ORDER BY saleDate ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS ma7, AVG(dailySales) OVER (ORDER BY saleDate ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS ma30 FROM TimeSeriesData), TrendCalculation AS (SELECT saleDate, dailySales, timeIndex, ma7, ma30, (ma7 - LAG(ma7, 7) OVER (ORDER BY saleDate)) / 7 AS weeklyTrend, (ma30 - LAG(ma30, 30) OVER (ORDER BY saleDate)) / 30 AS monthlyTrend FROM MovingAverages), SeasonalDecomposition AS (SELECT t.saleDate, t.dailySales, t.ma30 AS trend, t.dailySales / NULLIF(t.ma30, 0) AS seasonal, AVG(t.dailySales / NULLIF(t.ma30, 0)) OVER (PARTITION BY t.dayOfWeek) AS weeklySeasonality, AVG(t.dailySales / NULLIF(t.ma30, 0)) OVER (PARTITION BY t.month) AS monthlySeasonality FROM TrendCalculation t WHERE t.ma30 IS NOT NULL), ForecastModel AS (SELECT saleDate, dailySales, trend, seasonal, weeklySeasonality, monthlySeasonality, trend * weeklySeasonality * monthlySeasonality AS forecastValue, ABS(dailySales - (trend * weeklySeasonality * monthlySeasonality)) / NULLIF(dailySales, 0) * 100 AS forecastError FROM SeasonalDecomposition WHERE trend IS NOT NULL) SELECT DATE_FORMAT(saleDate, '%Y-%m') AS month, AVG(dailySales) AS actualSales, AVG(forecastValue) AS forecastedSales, AVG(forecastError) AS avgError FROM ForecastModel GROUP BY DATE_FORMAT(saleDate, '%Y-%m') ORDER BY month DESC LIMIT 12;
