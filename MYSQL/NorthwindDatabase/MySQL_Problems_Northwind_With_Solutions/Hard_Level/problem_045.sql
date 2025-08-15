-- Problem 45: Product Recommendation System
-- Level: Hard
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to find products frequently bought together (market basket analysis).

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT p1.productName AS product1, p2.productName AS product2, COUNT(*) AS frequency FROM OrderDetail od1 JOIN OrderDetail od2 ON od1.orderId = od2.orderId AND od1.productId < od2.productId JOIN Product p1 ON od1.productId = p1.productId JOIN Product p2 ON od2.productId = p2.productId GROUP BY p1.productId, p1.productName, p2.productId, p2.productName HAVING COUNT(*) >= 3 ORDER BY frequency DESC;
