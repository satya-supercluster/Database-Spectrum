-- Problem 61: Multi-dimensional Sales Cube Analysis
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to create a sales cube with dimensions: time, product category, customer country, and employee.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT YEAR(s.orderDate) AS year, QUARTER(s.orderDate) AS quarter, c.categoryName, cust.country, CONCAT(e.firstname, ' ', e.lastname) AS employee, COUNT(s.orderId) AS orderCount, SUM(od.quantity) AS totalQuantity, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avgOrderValue FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId JOIN Product p ON od.productId = p.productId JOIN Category c ON p.categoryId = c.categoryId JOIN Customer cust ON s.custId = cust.custId LEFT JOIN Employee e ON s.employeeId = e.employeeId GROUP BY YEAR(s.orderDate), QUARTER(s.orderDate), c.categoryName, cust.country, e.employeeId, e.firstname, e.lastname WITH ROLLUP ORDER BY year, quarter, c.categoryName, cust.country, employee;
