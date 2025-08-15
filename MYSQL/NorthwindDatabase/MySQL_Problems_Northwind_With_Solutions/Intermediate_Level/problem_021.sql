-- Problem 21: Products with Category Names
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display product names along with their category names.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT p.productName, c.categoryName FROM Product p JOIN Category c ON p.categoryId = c.categoryId;
