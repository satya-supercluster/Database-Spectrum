-- Problem 38: Product Price Statistics by Category
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to show min, max, and average price for each category.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT c.categoryName, MIN(p.unitPrice) AS minPrice, MAX(p.unitPrice) AS maxPrice, AVG(p.unitPrice) AS avgPrice FROM Category c JOIN Product p ON c.categoryId = p.categoryId GROUP BY c.categoryId, c.categoryName;
