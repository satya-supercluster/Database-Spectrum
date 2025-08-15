-- Problem 23: Average Product Price by Category
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to find the average product price for each category.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT c.categoryName, AVG(p.unitPrice) AS avgPrice FROM Category c JOIN Product p ON c.categoryId = p.categoryId GROUP BY c.categoryId, c.categoryName;
