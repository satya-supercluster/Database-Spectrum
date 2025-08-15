-- Problem 46: Employee Performance Metrics
-- Level: Hard
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to rank employees by their sales performance including total orders handled and revenue generated.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH EmployeePerformance AS (SELECT e.employeeId, CONCAT(e.firstname, ' ', e.lastname) AS employeeName, COUNT(s.orderId) AS totalOrders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue FROM Employee e LEFT JOIN SalesOrder s ON e.employeeId = s.employeeId LEFT JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY e.employeeId, e.firstname, e.lastname) SELECT employeeName, totalOrders, totalRevenue, RANK() OVER (ORDER BY totalRevenue DESC) AS revenueRank, RANK() OVER (ORDER BY totalOrders DESC) AS orderRank FROM EmployeePerformance ORDER BY totalRevenue DESC;
