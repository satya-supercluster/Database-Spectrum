-- Problem 28: Monthly Order Summary
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to show the number of orders placed in each month of 2023.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT MONTH(orderDate) AS month, COUNT(*) AS orderCount FROM SalesOrder WHERE YEAR(orderDate) = 2023 GROUP BY MONTH(orderDate) ORDER BY month;
