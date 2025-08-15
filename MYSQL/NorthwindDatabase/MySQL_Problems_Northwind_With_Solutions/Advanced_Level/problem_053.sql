-- Problem 53: Supply Chain Optimization
-- Level: Advanced
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to identify potential supply chain bottlenecks and optimization opportunities.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH SupplyChainMetrics AS (SELECT s.supplierId, s.companyName AS supplier, s.country AS supplierCountry, COUNT(p.productId) AS productCount, AVG(p.unitPrice) AS avgProductPrice, SUM(p.unitsInStock) AS totalInventory, AVG(p.reorderLevel) AS avgReorderLevel FROM Supplier s LEFT JOIN Product p ON s.supplierId = p.supplierId GROUP BY s.supplierId, s.companyName, s.country), ProductDemand AS (SELECT p.supplierId, SUM(od.quantity) AS totalDemand FROM Product p JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.supplierId) SELECT scm.supplier, scm.supplierCountry, scm.productCount, scm.totalInventory, pd.totalDemand, CASE WHEN pd.totalDemand > scm.totalInventory THEN 'High Demand - Low Inventory' WHEN pd.totalDemand < scm.totalInventory * 0.1 THEN 'Low Demand - High Inventory' ELSE 'Balanced' END AS inventoryStatus FROM SupplyChainMetrics scm LEFT JOIN ProductDemand pd ON scm.supplierId = pd.supplierId ORDER BY pd.totalDemand DESC;
