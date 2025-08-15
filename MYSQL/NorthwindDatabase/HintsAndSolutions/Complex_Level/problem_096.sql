-- Problem 96: Advanced Financial Risk Assessment
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to assess financial risks including credit risk, operational risk, and market risk.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH CustomerCreditRisk AS (SELECT c.custId, c.companyName, COUNT(s.orderId) AS order_count, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS total_credit, AVG(DATEDIFF(s.shippedDate, s.orderDate)) AS avg_payment_delay, COUNT(CASE WHEN s.shippedDate > s.requiredDate THEN 1 END) AS payment_delays, MAX(s.orderDate) AS last_transaction FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId, c.companyName), OperationalRisk AS (SELECT p.productId, p.productName, p.unitsInStock, SUM(od.quantity) AS total_demand, p.unitsInStock - SUM(od.quantity) AS stock_buffer, CASE WHEN p.unitsInStock < SUM(od.quantity) * 0.1 THEN 'High Risk' WHEN p.unitsInStock < SUM(od.quantity) * 0.5 THEN 'Medium Risk' ELSE 'Low Risk' END AS stockout_risk FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName, p.unitsInStock), MarketRisk AS (SELECT c.categoryName, COUNT(p.productId) AS product_count, AVG(p.unitPrice) AS avg_price, STDDEV(p.unitPrice) AS price_volatility, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS category_revenue FROM Category c JOIN Product p ON c.categoryId = p.categoryId LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY c.categoryId, c.categoryName), RiskAssessment AS (SELECT 'Credit Risk' AS risk_type, COUNT(CASE WHEN payment_delays > order_count * 0.2 THEN 1 END) AS high_risk_count, COUNT(*) AS total_entities FROM CustomerCreditRisk UNION ALL SELECT 'Operational Risk', COUNT(CASE WHEN stockout_risk = 'High Risk' THEN 1 END), COUNT(*) FROM OperationalRisk UNION ALL SELECT 'Market Risk', COUNT(CASE WHEN price_volatility > avg_price * 0.3 THEN 1 END), COUNT(*) FROM MarketRisk) SELECT risk_type, high_risk_count, total_entities, (high_risk_count * 100.0 / total_entities) AS risk_percentage FROM RiskAssessment;
