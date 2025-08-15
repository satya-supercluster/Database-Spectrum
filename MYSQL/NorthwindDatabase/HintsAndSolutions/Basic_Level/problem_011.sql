-- Problem 11: Products with Names Starting with 'C'
-- Level: Basic
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display products whose names start with the letter 'C'.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT * FROM Product WHERE productName LIKE 'C%';
