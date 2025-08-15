-- Problem 27: Products Never Ordered
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to find products that have never been ordered.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT p.* FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId WHERE od.productId IS NULL;
