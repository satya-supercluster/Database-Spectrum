-- Problem 36: Orders Shipped Late
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to find orders that were shipped after the required date.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT orderId, orderDate, requiredDate, shippedDate FROM SalesOrder WHERE shippedDate > requiredDate;
