-- Problem 29: Suppliers with Most Products
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to find suppliers who supply more than 5 products.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT s.companyName, COUNT(p.productId) AS productCount FROM Supplier s JOIN Product p ON s.supplierId = p.supplierId GROUP BY s.supplierId, s.companyName HAVING COUNT(p.productId) > 5;
