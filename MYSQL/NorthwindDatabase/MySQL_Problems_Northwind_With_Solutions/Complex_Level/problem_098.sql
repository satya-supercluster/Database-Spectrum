-- Problem 98: Advanced Predictive Analytics for Strategic Planning
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to implement predictive models for strategic business planning and scenario analysis.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH HistoricalGrowth AS (SELECT YEAR(s.orderDate) AS year, COUNT(s.orderId) AS annual_orders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS annual_revenue, COUNT(DISTINCT s.custId) AS annual_customers FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY YEAR(s.orderDate)), GrowthRates AS (SELECT year, annual_orders, annual_revenue, annual_customers, LAG(annual_revenue) OVER (ORDER BY year) AS prev_year_revenue, (annual_revenue - LAG(annual_revenue) OVER (ORDER BY year)) / LAG(annual_revenue) OVER (ORDER BY year) * 100 AS revenue_growth_rate FROM HistoricalGrowth), PredictiveModeling AS (SELECT AVG(revenue_growth_rate) AS avg_growth_rate, STDDEV(revenue_growth_rate) AS growth_volatility, MAX(annual_revenue) AS peak_revenue FROM GrowthRates WHERE revenue_growth_rate IS NOT NULL), ScenarioAnalysis AS (SELECT pm.avg_growth_rate, pm.growth_volatility, pm.peak_revenue, pm.peak_revenue * (1 + pm.avg_growth_rate/100) AS conservative_forecast, pm.peak_revenue * (1 + (pm.avg_growth_rate + pm.growth_volatility)/100) AS optimistic_forecast, pm.peak_revenue * (1 + (pm.avg_growth_rate - pm.growth_volatility)/100) AS pessimistic_forecast FROM PredictiveModeling pm), StrategicRecommendations AS (SELECT CASE WHEN conservative_forecast > peak_revenue * 1.1 THEN 'Expand Market Presence' WHEN conservative_forecast > peak_revenue * 1.05 THEN 'Optimize Current Operations' ELSE 'Focus on Customer Retention' END AS strategic_direction, CASE WHEN growth_volatility > 20 THEN 'High Risk - Diversify Portfolio' WHEN growth_volatility > 10 THEN 'Medium Risk - Monitor Closely' ELSE 'Low Risk - Continue Current Strategy' END AS risk_strategy FROM ScenarioAnalysis sa) SELECT FORMAT(conservative_forecast, 2) AS conservative_forecast, FORMAT(optimistic_forecast, 2) AS optimistic_forecast, FORMAT(pessimistic_forecast, 2) AS pessimistic_forecast, strategic_direction, risk_strategy FROM ScenarioAnalysis sa CROSS JOIN StrategicRecommendations sr;
