-- Problem 91: Enterprise Resource Planning Integration
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to simulate ERP integration by creating a comprehensive resource allocation and planning analysis.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH ResourceAllocation AS (SELECT e.employeeId, CONCAT(e.firstname, ' ', e.lastname) AS employee_name, COUNT(s.orderId) AS orders_handled, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS revenue_generated, COUNT(DISTINCT s.custId) AS customers_served FROM Employee e LEFT JOIN SalesOrder s ON e.employeeId = s.employeeId LEFT JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY e.employeeId, e.firstname, e.lastname), CapacityAnalysis AS (SELECT ra.employee_name, ra.orders_handled, ra.revenue_generated, ra.customers_served, ra.revenue_generated / NULLIF(ra.orders_handled, 0) AS revenue_per_order FROM ResourceAllocation ra) SELECT employee_name, orders_handled, revenue_generated, revenue_per_order, CASE WHEN orders_handled > 50 THEN 'High Capacity' WHEN orders_handled > 20 THEN 'Medium Capacity' ELSE 'Low Capacity' END AS capacity_level FROM CapacityAnalysis ORDER BY revenue_generated DESC;
