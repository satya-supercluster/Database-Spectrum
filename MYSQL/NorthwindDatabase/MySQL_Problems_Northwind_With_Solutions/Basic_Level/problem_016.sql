-- Problem 16: Categories with Description
-- Level: Basic
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display category names and descriptions where description is not null.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT categoryName, description FROM Category WHERE description IS NOT NULL;
