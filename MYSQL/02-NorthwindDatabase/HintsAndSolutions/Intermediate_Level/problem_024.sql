-- Problem 24: Customers and Their Orders Count
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display customer names and the number of orders they have placed.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT c.companyName, COUNT(s.orderId) AS orderCount FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId, c.companyName;
