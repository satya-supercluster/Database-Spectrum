-- Problem 85: Multi-dimensional Profitability Analysis
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to analyze profitability across multiple dimensions: product, customer, territory, and time.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH ProfitabilityMetrics AS (SELECT p.productId, p.productName, c.categoryName, cust.custId, cust.companyName AS customer_name, cust.country, YEAR(s.orderDate) AS year, QUARTER(s.orderDate) AS quarter, od.quantity, od.unitPrice, od.discount, (od.quantity * od.unitPrice * (1 - od.discount)) AS revenue, (od.quantity * od.unitPrice * 0.3) AS estimated_cost, (od.quantity * od.unitPrice * (1 - od.discount) - od.quantity * od.unitPrice * 0.3) AS estimated_profit FROM Product p JOIN OrderDetail od ON p.productId = od.productId JOIN SalesOrder s ON od.orderId = s.orderId JOIN Customer cust ON s.custId = cust.custId JOIN Category c ON p.categoryId = c.categoryId), DimensionalProfitability AS (SELECT categoryName, customer_name, country, year, quarter, SUM(revenue) AS total_revenue, SUM(estimated_profit) AS total_profit, AVG(estimated_profit / NULLIF(revenue, 0)) AS profit_margin, COUNT(DISTINCT productId) AS unique_products FROM ProfitabilityMetrics GROUP BY categoryName, customer_name, country, year, quarter), ProfitabilityRanking AS (SELECT categoryName, customer_name, country, total_revenue, total_profit, profit_margin, unique_products, RANK() OVER (PARTITION BY categoryName ORDER BY total_profit DESC) AS profit_rank_in_category, RANK() OVER (ORDER BY total_profit DESC) AS overall_profit_rank FROM DimensionalProfitability WHERE year = YEAR(CURDATE()) - 1) SELECT categoryName, customer_name, country, FORMAT(total_revenue, 2) AS revenue, FORMAT(total_profit, 2) AS profit, ROUND(profit_margin * 100, 2) AS profit_margin_pct, profit_rank_in_category, overall_profit_rank FROM ProfitabilityRanking WHERE overall_profit_rank <= 50 ORDER BY overall_profit_rank;
