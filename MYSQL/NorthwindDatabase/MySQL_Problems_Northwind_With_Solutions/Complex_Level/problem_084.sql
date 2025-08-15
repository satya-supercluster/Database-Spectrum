-- Problem 84: Predictive Inventory Management with Safety Stock
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to calculate optimal inventory levels with safety stock considering demand variability.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH DemandHistory AS (SELECT p.productId, p.productName, DATE_FORMAT(s.orderDate, '%Y-%m') AS month, SUM(od.quantity) AS monthly_demand FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId LEFT JOIN SalesOrder s ON od.orderId = s.orderId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH) GROUP BY p.productId, p.productName, DATE_FORMAT(s.orderDate, '%Y-%m')), DemandStatistics AS (SELECT productId, productName, AVG(monthly_demand) AS avg_demand, STDDEV(monthly_demand) AS demand_stddev, COUNT(*) AS months_with_data FROM DemandHistory WHERE monthly_demand > 0 GROUP BY productId, productName HAVING COUNT(*) >= 3), SafetyStockCalculation AS (SELECT ds.productId, ds.productName, ds.avg_demand, ds.demand_stddev, p.unitsInStock, p.reorderLevel, CEIL(ds.avg_demand + 1.65 * ds.demand_stddev) AS safety_stock, CEIL(ds.avg_demand * 2 + 1.65 * ds.demand_stddev) AS optimal_reorder_point, CEIL(ds.avg_demand * 3 + 2 * ds.demand_stddev) AS max_stock_level FROM DemandStatistics ds JOIN Product p ON ds.productId = p.productId), InventoryRecommendations AS (SELECT productName, unitsInStock, current_reorder_level = reorderLevel, optimal_reorder_point, safety_stock, max_stock_level, CASE WHEN unitsInStock < safety_stock THEN 'Critical - Immediate Reorder' WHEN unitsInStock < optimal_reorder_point THEN 'Low - Schedule Reorder' WHEN unitsInStock > max_stock_level THEN 'Excess - Reduce Orders' ELSE 'Optimal' END AS inventory_status FROM SafetyStockCalculation) SELECT inventory_status, COUNT(*) AS product_count, AVG(unitsInStock) AS avg_current_stock, AVG(optimal_reorder_point) AS avg_optimal_reorder FROM InventoryRecommendations GROUP BY inventory_status ORDER BY FIELD(inventory_status, 'Critical - Immediate Reorder', 'Low - Schedule Reorder', 'Optimal', 'Excess - Reduce Orders');
