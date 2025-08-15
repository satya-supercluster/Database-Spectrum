-- Problem 64: Customer Journey Analysis with Touchpoint Attribution
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to analyze customer journey paths and attribute value to different touchpoints in the sales process.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH CustomerOrderSequence AS (SELECT c.custId, c.companyName, s.orderId, s.orderDate, ROW_NUMBER() OVER (PARTITION BY c.custId ORDER BY s.orderDate) AS orderSequence, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS orderValue, LEAD(s.orderDate) OVER (PARTITION BY c.custId ORDER BY s.orderDate) AS nextOrderDate FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId, c.companyName, s.orderId, s.orderDate), JourneyAnalysis AS (SELECT custId, companyName, orderSequence, orderValue, CASE WHEN orderSequence = 1 THEN 'Acquisition' WHEN orderSequence = 2 THEN 'Activation' WHEN orderSequence <= 5 THEN 'Retention' ELSE 'Loyalty' END AS journeyStage, CASE WHEN nextOrderDate IS NOT NULL THEN DATEDIFF(nextOrderDate, orderDate) ELSE NULL END AS daysToNextOrder FROM CustomerOrderSequence), TouchpointValue AS (SELECT journeyStage, COUNT(*) AS touchpointCount, AVG(orderValue) AS avgOrderValue, SUM(orderValue) AS totalValue, AVG(daysToNextOrder) AS avgDaysToNext FROM JourneyAnalysis GROUP BY journeyStage), AttributionModel AS (SELECT journeyStage, touchpointCount, avgOrderValue, totalValue, avgDaysToNext, totalValue / SUM(totalValue) OVER () * 100 AS valueAttribution, CASE WHEN journeyStage = 'Acquisition' THEN 0.4 WHEN journeyStage = 'Activation' THEN 0.3 WHEN journeyStage = 'Retention' THEN 0.2 ELSE 0.1 END AS attributionWeight FROM TouchpointValue) SELECT journeyStage, touchpointCount, avgOrderValue, totalValue, valueAttribution, attributionWeight, (totalValue * attributionWeight) AS weightedValue FROM AttributionModel ORDER BY FIELD(journeyStage, 'Acquisition', 'Activation', 'Retention', 'Loyalty');
