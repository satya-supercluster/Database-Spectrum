-- Problem 95: Machine Learning Feature Engineering for Churn Prediction
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to create comprehensive features for machine learning models to predict customer churn.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH CustomerFeatures AS (SELECT c.custId, c.companyName, COUNT(s.orderId) AS total_orders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS total_spent, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avg_order_value, MIN(s.orderDate) AS first_order_date, MAX(s.orderDate) AS last_order_date, DATEDIFF(CURDATE(), MAX(s.orderDate)) AS days_since_last_order, COUNT(DISTINCT p.categoryId) AS categories_purchased, AVG(DATEDIFF(s.shippedDate, s.orderDate)) AS avg_shipping_time, COUNT(CASE WHEN s.shippedDate > s.requiredDate THEN 1 END) AS late_deliveries FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId LEFT JOIN OrderDetail od ON s.orderId = od.orderId LEFT JOIN Product p ON od.productId = p.productId GROUP BY c.custId, c.companyName), ChurnFeatures AS (SELECT custId, companyName, total_orders, total_spent, avg_order_value, days_since_last_order, categories_purchased, avg_shipping_time, late_deliveries, DATEDIFF(last_order_date, first_order_date) AS customer_lifetime_days, total_orders / GREATEST(DATEDIFF(last_order_date, first_order_date), 1) * 365 AS orders_per_year, CASE WHEN days_since_last_order > 180 THEN 1 ELSE 0 END AS likely_churned FROM CustomerFeatures WHERE total_orders > 0), MLDataset AS (SELECT custId, total_orders, total_spent, avg_order_value, days_since_last_order, categories_purchased, avg_shipping_time, late_deliveries, customer_lifetime_days, orders_per_year, likely_churned, CASE WHEN total_spent > 5000 THEN 1 ELSE 0 END AS high_value, CASE WHEN orders_per_year > 12 THEN 1 ELSE 0 END AS frequent_buyer, CASE WHEN late_deliveries > 0 THEN 1 ELSE 0 END AS had_delivery_issues FROM ChurnFeatures) SELECT likely_churned, COUNT(*) AS customer_count, AVG(total_spent) AS avg_spent, AVG(orders_per_year) AS avg_frequency, AVG(days_since_last_order) AS avg_days_since_order FROM MLDataset GROUP BY likely_churned;
