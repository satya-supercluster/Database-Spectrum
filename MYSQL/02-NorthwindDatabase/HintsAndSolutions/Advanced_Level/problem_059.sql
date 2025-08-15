-- Problem 59: Customer Churn Risk Analysis
-- Level: Advanced
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to identify customers at risk of churning based on their ordering patterns.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH CustomerLastOrder AS (SELECT c.custId, c.companyName, MAX(s.orderDate) AS lastOrderDate, COUNT(s.orderId) AS totalOrders, AVG(DATEDIFF(s.orderDate, LAG(s.orderDate) OVER (PARTITION BY c.custId ORDER BY s.orderDate))) AS avgDaysBetweenOrders FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId, c.companyName), ChurnRisk AS (SELECT custId, companyName, lastOrderDate, totalOrders, avgDaysBetweenOrders, DATEDIFF(CURDATE(), lastOrderDate) AS daysSinceLastOrder, CASE WHEN DATEDIFF(CURDATE(), lastOrderDate) > (avgDaysBetweenOrders * 2) THEN 'High Risk' WHEN DATEDIFF(CURDATE(), lastOrderDate) > avgDaysBetweenOrders THEN 'Medium Risk' ELSE 'Low Risk' END AS churnRisk FROM CustomerLastOrder WHERE lastOrderDate IS NOT NULL) SELECT churnRisk, COUNT(*) AS customerCount, AVG(daysSinceLastOrder) AS avgDaysSinceLastOrder FROM ChurnRisk GROUP BY churnRisk ORDER BY FIELD(churnRisk, 'High Risk', 'Medium Risk', 'Low Risk');
