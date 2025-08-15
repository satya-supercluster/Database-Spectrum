-- Problem 94: Comprehensive Customer Experience Analytics
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to analyze customer experience across all touchpoints and calculate satisfaction scores.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH CustomerTouchpoints AS (SELECT c.custId, c.companyName, COUNT(s.orderId) AS total_orders, AVG(DATEDIFF(s.shippedDate, s.orderDate)) AS avg_shipping_time, COUNT(CASE WHEN s.shippedDate > s.requiredDate THEN 1 END) AS late_deliveries, AVG(od.discount) AS avg_discount_received, COUNT(DISTINCT e.employeeId) AS employees_interacted FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId LEFT JOIN Employee e ON s.employeeId = e.employeeId GROUP BY c.custId, c.companyName), ExperienceScoring AS (SELECT custId, companyName, total_orders, avg_shipping_time, late_deliveries, avg_discount_received, employees_interacted, CASE WHEN avg_shipping_time <= 3 THEN 5 WHEN avg_shipping_time <= 7 THEN 4 WHEN avg_shipping_time <= 10 THEN 3 ELSE 2 END AS shipping_score, CASE WHEN late_deliveries = 0 THEN 5 WHEN late_deliveries / total_orders < 0.1 THEN 4 WHEN late_deliveries / total_orders < 0.2 THEN 3 ELSE 2 END AS delivery_score, CASE WHEN avg_discount_received > 0.1 THEN 5 WHEN avg_discount_received > 0.05 THEN 4 ELSE 3 END AS discount_score FROM CustomerTouchpoints), CustomerSatisfaction AS (SELECT custId, companyName, total_orders, (shipping_score + delivery_score + discount_score) / 3 AS satisfaction_score, CASE WHEN (shipping_score + delivery_score + discount_score) / 3 >= 4.5 THEN 'Highly Satisfied' WHEN (shipping_score + delivery_score + discount_score) / 3 >= 3.5 THEN 'Satisfied' WHEN (shipping_score + delivery_score + discount_score) / 3 >= 2.5 THEN 'Neutral' ELSE 'Dissatisfied' END AS satisfaction_level FROM ExperienceScoring) SELECT satisfaction_level, COUNT(*) AS customer_count, AVG(satisfaction_score) AS avg_score, AVG(total_orders) AS avg_orders FROM CustomerSatisfaction GROUP BY satisfaction_level ORDER BY avg_score DESC;
