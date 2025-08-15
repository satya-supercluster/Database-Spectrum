-- Problem 82: Market Basket Optimization with Profit Margins
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to optimize market basket recommendations considering profit margins and inventory levels.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH ProductProfitability AS (SELECT p.productId, p.productName, p.unitPrice, (p.unitPrice * 0.3) AS estimated_profit, p.unitsInStock FROM Product p), BasketAnalysis AS (SELECT od1.productId AS product1, od2.productId AS product2, COUNT(*) AS frequency, AVG(pp1.estimated_profit + pp2.estimated_profit) AS bundle_profit FROM OrderDetail od1 JOIN OrderDetail od2 ON od1.orderId = od2.orderId AND od1.productId < od2.productId JOIN ProductProfitability pp1 ON od1.productId = pp1.productId JOIN ProductProfitability pp2 ON od2.productId = pp2.productId GROUP BY od1.productId, od2.productId HAVING COUNT(*) >= 3), OptimizedBaskets AS (SELECT ba.product1, ba.product2, ba.frequency, ba.bundle_profit, (ba.frequency * ba.bundle_profit) AS optimization_score FROM BasketAnalysis ba JOIN ProductProfitability pp1 ON ba.product1 = pp1.productId JOIN ProductProfitability pp2 ON ba.product2 = pp2.productId WHERE pp1.unitsInStock > 5 AND pp2.unitsInStock > 5) SELECT p1.productName AS product1, p2.productName AS product2, frequency, bundle_profit, optimization_score FROM OptimizedBaskets ob JOIN Product p1 ON ob.product1 = p1.productId JOIN Product p2 ON ob.product2 = p2.productId ORDER BY optimization_score DESC LIMIT 15;
