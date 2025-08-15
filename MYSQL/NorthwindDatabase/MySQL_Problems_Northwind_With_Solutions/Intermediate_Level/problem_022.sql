-- Problem 22: Count Products by Category
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to count the number of products in each category.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT c.categoryName, COUNT(p.productId) AS productCount FROM Category c LEFT JOIN Product p ON c.categoryId = p.categoryId GROUP BY c.categoryId, c.categoryName;
