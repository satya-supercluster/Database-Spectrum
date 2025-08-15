-- Problem 77: Dynamic Product Bundling Recommendations
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to identify optimal product bundles based on purchase patterns and profit margins.

-- ============================================================
-- SOLUTION:
-- ============================================================

-- Product bundling analysis with profitability scoring
WITH ProductPairs AS (
  SELECT 
    od1.productId AS product1,
    od2.productId AS product2,
    COUNT(*) AS frequency,
    AVG(od1.unitPrice + od2.unitPrice) AS bundle_price
  FROM OrderDetail od1
  JOIN OrderDetail od2 ON od1.orderId = od2.orderId AND od1.productId < od2.productId
  GROUP BY od1.productId, od2.productId
  HAVING COUNT(*) >= 5
)
SELECT 
  p1.productName AS product1,
  p2.productName AS product2,
  pp.frequency,
  pp.bundle_price,
  RANK() OVER (ORDER BY pp.frequency DESC) AS bundle_rank
FROM ProductPairs pp
JOIN Product p1 ON pp.product1 = p1.productId
JOIN Product p2 ON pp.product2 = p2.productId
LIMIT 20;
