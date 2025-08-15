-- Problem 40: Order Value Analysis
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to calculate the total value of each order (quantity * unitPrice - discount).

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT od.orderId, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalOrderValue FROM OrderDetail od GROUP BY od.orderId ORDER BY totalOrderValue DESC;
