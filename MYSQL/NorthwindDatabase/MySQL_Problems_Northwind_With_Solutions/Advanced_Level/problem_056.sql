-- Problem 56: Cross-Selling Opportunity Matrix
-- Level: Advanced
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to create a cross-selling opportunity matrix showing product affinity scores.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH ProductPairs AS (SELECT od1.productId AS product1, od2.productId AS product2, COUNT(*) AS coOccurrence FROM OrderDetail od1 JOIN OrderDetail od2 ON od1.orderId = od2.orderId AND od1.productId < od2.productId GROUP BY od1.productId, od2.productId), ProductFrequency AS (SELECT productId, COUNT(*) AS totalOrders FROM OrderDetail GROUP BY productId), AffinityScores AS (SELECT pp.product1, pp.product2, pp.coOccurrence, pf1.totalOrders AS product1Orders, pf2.totalOrders AS product2Orders, pp.coOccurrence / SQRT(pf1.totalOrders * pf2.totalOrders) AS affinityScore FROM ProductPairs pp JOIN ProductFrequency pf1 ON pp.product1 = pf1.productId JOIN ProductFrequency pf2 ON pp.product2 = pf2.productId) SELECT p1.productName AS product1, p2.productName AS product2, affinityScore FROM AffinityScores af JOIN Product p1 ON af.product1 = p1.productId JOIN Product p2 ON af.product2 = p2.productId WHERE affinityScore > 0.1 ORDER BY affinityScore DESC LIMIT 20;
