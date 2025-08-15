-- Problem 26: Top 5 Customers by Order Value
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to find the top 5 customers by total order value (using freight as proxy).

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT c.companyName, SUM(s.freight) AS totalOrderValue FROM Customer c JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId, c.companyName ORDER BY totalOrderValue DESC LIMIT 5;
