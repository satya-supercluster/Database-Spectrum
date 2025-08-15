-- Problem 52: Customer Lifetime Value Prediction
-- Level: Advanced
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to calculate customer lifetime value based on historical data and predict future value.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH CustomerHistory AS (SELECT c.custId, c.companyName, MIN(s.orderDate) AS firstOrder, MAX(s.orderDate) AS lastOrder, COUNT(s.orderId) AS totalOrders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalSpent, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avgOrderValue FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId, c.companyName), CustomerLTV AS (SELECT custId, companyName, totalOrders, totalSpent, avgOrderValue, DATEDIFF(lastOrder, firstOrder) + 1 AS customerLifespanDays, CASE WHEN DATEDIFF(lastOrder, firstOrder) > 0 THEN totalOrders / (DATEDIFF(lastOrder, firstOrder) / 365.25) ELSE totalOrders END AS ordersPerYear FROM CustomerHistory) SELECT companyName, totalSpent AS historicalValue, avgOrderValue, ordersPerYear, avgOrderValue * ordersPerYear AS predictedAnnualValue FROM CustomerLTV ORDER BY predictedAnnualValue DESC;
