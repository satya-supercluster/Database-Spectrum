-- Problem 58: Geographic Sales Distribution Analysis
-- Level: Advanced
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to analyze sales distribution across different geographic regions and identify expansion opportunities.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH GeographicSales AS (SELECT c.country, c.city, COUNT(DISTINCT c.custId) AS customerCount, COUNT(s.orderId) AS orderCount, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.country, c.city), CountrySummary AS (SELECT country, SUM(customerCount) AS totalCustomers, SUM(orderCount) AS totalOrders, SUM(totalRevenue) AS countryRevenue, AVG(totalRevenue) AS avgCityRevenue FROM GeographicSales GROUP BY country) SELECT cs.country, cs.totalCustomers, cs.totalOrders, cs.countryRevenue, cs.avgCityRevenue, RANK() OVER (ORDER BY cs.countryRevenue DESC) AS revenueRank FROM CountrySummary cs ORDER BY cs.countryRevenue DESC;
