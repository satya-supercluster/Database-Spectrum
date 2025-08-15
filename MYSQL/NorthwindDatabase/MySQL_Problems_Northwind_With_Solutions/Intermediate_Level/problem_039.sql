-- Problem 39: Customers Without Orders
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to find customers who have never placed an order.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT c.* FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId WHERE s.custId IS NULL;
