-- Problem 76: Multi-Variate Sales Correlation Analysis
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to perform correlation analysis between different sales variables and identify key relationships.

-- ============================================================
-- SOLUTION:
-- ============================================================

-- Complex correlation analysis between sales variables
WITH SalesVariables AS (
  SELECT 
    p.productId, p.unitPrice, od.quantity, od.discount,
    c.categoryId, s.orderDate,
    (od.quantity * od.unitPrice * (1 - od.discount)) AS orderValue
  FROM Product p
  JOIN OrderDetail od ON p.productId = od.productId
  JOIN SalesOrder s ON od.orderId = s.orderId
  JOIN Category c ON p.categoryId = c.categoryId
)
SELECT 
  categoryId,
  CORR(unitPrice, quantity) AS price_quantity_corr,
  CORR(discount, orderValue) AS discount_value_corr,
  COUNT(*) AS sample_size
FROM SalesVariables
GROUP BY categoryId;
