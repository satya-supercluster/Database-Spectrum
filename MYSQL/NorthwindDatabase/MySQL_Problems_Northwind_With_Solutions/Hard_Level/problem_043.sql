-- Problem 43: Customer Loyalty Analysis
-- Level: Hard
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to classify customers as 'New', 'Regular', or 'VIP' based on their order frequency and total spending.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH CustomerStats AS (SELECT c.custId, c.companyName, COUNT(s.orderId) AS orderCount, SUM(s.freight) AS totalSpent FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId, c.companyName) SELECT companyName, orderCount, totalSpent, CASE WHEN orderCount = 0 THEN 'Inactive' WHEN orderCount <= 2 THEN 'New' WHEN orderCount <= 5 AND totalSpent <= 100 THEN 'Regular' ELSE 'VIP' END AS customerType FROM CustomerStats ORDER BY totalSpent DESC;
