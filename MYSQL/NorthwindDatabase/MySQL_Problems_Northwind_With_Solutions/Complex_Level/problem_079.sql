-- Problem 79: Customer Journey Attribution Modeling
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to track customer touchpoints and attribute revenue across the customer journey.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH CustomerTouchpoints AS (SELECT c.custId, s.orderId, s.orderDate, e.employeeId, ROW_NUMBER() OVER (PARTITION BY c.custId ORDER BY s.orderDate) AS touchpoint_order, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS order_value FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId LEFT JOIN Employee e ON s.employeeId = e.employeeId GROUP BY c.custId, s.orderId, s.orderDate, e.employeeId), JourneyAttribution AS (SELECT custId, touchpoint_order, order_value, CASE WHEN touchpoint_order = 1 THEN order_value * 0.4 WHEN touchpoint_order = 2 THEN order_value * 0.3 WHEN touchpoint_order <= 5 THEN order_value * 0.2 ELSE order_value * 0.1 END AS attributed_value FROM CustomerTouchpoints) SELECT touchpoint_order, COUNT(*) AS touchpoint_count, AVG(order_value) AS avg_order_value, SUM(attributed_value) AS total_attributed_value FROM JourneyAttribution GROUP BY touchpoint_order ORDER BY touchpoint_order;
