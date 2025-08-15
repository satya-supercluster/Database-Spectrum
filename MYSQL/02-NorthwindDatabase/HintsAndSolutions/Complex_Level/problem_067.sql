-- Problem 67: Advanced Price Elasticity and Optimization Analysis
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to calculate price elasticity of demand and suggest optimal pricing strategies for products.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH PricePoints AS (SELECT p.productId, p.productName, od.unitPrice, SUM(od.quantity) AS quantitySold, COUNT(DISTINCT od.orderId) AS orderCount, AVG(od.discount) AS avgDiscount FROM Product p JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName, od.unitPrice), PriceElasticity AS (SELECT pp1.productId, pp1.productName, pp1.unitPrice AS price1, pp2.unitPrice AS price2, pp1.quantitySold AS quantity1, pp2.quantitySold AS quantity2, CASE WHEN pp1.unitPrice != pp2.unitPrice AND pp1.quantitySold != pp2.quantitySold THEN ((pp2.quantitySold - pp1.quantitySold) / pp1.quantitySold) / ((pp2.unitPrice - pp1.unitPrice) / pp1.unitPrice) ELSE NULL END AS priceElasticity FROM PricePoints pp1 JOIN PricePoints pp2 ON pp1.productId = pp2.productId AND pp1.unitPrice < pp2.unitPrice), OptimalPricing AS (SELECT pe.productId, pe.productName, AVG(pe.priceElasticity) AS avgElasticity, MIN(pp.unitPrice) AS minPrice, MAX(pp.unitPrice) AS maxPrice, AVG(pp.unitPrice) AS avgPrice, SUM(pp.quantitySold) AS totalQuantity FROM PriceElasticity pe JOIN PricePoints pp ON pe.productId = pp.productId GROUP BY pe.productId, pe.productName HAVING AVG(pe.priceElasticity) IS NOT NULL), PricingStrategy AS (SELECT productId, productName, avgElasticity, minPrice, maxPrice, avgPrice, CASE WHEN avgElasticity > -1 THEN 'Inelastic - Increase Price' WHEN avgElasticity BETWEEN -2 AND -1 THEN 'Unit Elastic - Maintain Price' ELSE 'Elastic - Consider Decrease' END AS pricingRecommendation, CASE WHEN avgElasticity > -1 THEN avgPrice * 1.1 WHEN avgElasticity < -2 THEN avgPrice * 0.95 ELSE avgPrice END AS recommendedPrice FROM OptimalPricing) SELECT pricingRecommendation, COUNT(*) AS productCount, AVG(avgElasticity) AS avgElasticity, AVG(recommendedPrice - avgPrice) AS avgPriceChange FROM PricingStrategy GROUP BY pricingRecommendation;
