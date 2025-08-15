-- Problem 33: Customer Orders with Shipping Info
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display customer orders with shipping company information.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT c.companyName AS customer, s.orderId, sh.companyName AS shipper, s.shippedDate FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN Shipper sh ON s.shipperid = sh.shipperId;
