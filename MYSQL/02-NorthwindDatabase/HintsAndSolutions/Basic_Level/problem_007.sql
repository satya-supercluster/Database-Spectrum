-- Problem 7: Top 5 Most Expensive Products
-- Level: Basic
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display the top 5 most expensive products.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT * FROM Product ORDER BY unitPrice DESC LIMIT 5;
