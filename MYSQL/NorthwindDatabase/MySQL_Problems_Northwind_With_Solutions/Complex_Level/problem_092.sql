-- Problem 92: Advanced Data Mining for Sales Patterns
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to discover hidden sales patterns using association rules and sequential pattern mining.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH ProductSequences AS (SELECT c.custId, s.orderDate, p.productId, p.productName, ROW_NUMBER() OVER (PARTITION BY c.custId ORDER BY s.orderDate) AS purchase_sequence FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId JOIN Product p ON od.productId = p.productId), SequentialPatterns AS (SELECT ps1.productId AS first_product, ps2.productId AS second_product, ps1.productName AS first_name, ps2.productName AS second_name, COUNT(*) AS pattern_frequency FROM ProductSequences ps1 JOIN ProductSequences ps2 ON ps1.custId = ps2.custId AND ps2.purchase_sequence = ps1.purchase_sequence + 1 GROUP BY ps1.productId, ps2.productId, ps1.productName, ps2.productName HAVING COUNT(*) >= 3) SELECT first_name, second_name, pattern_frequency, RANK() OVER (ORDER BY pattern_frequency DESC) AS pattern_rank FROM SequentialPatterns ORDER BY pattern_frequency DESC LIMIT 20;
