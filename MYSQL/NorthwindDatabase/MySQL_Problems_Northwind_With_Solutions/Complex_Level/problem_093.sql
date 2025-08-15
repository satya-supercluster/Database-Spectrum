-- Problem 93: Complex Supply Chain Network Analysis
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to analyze the entire supply chain network including supplier dependencies and risk assessment.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH SupplyChainNetwork AS (SELECT s.supplierId, s.companyName AS supplier_name, s.country AS supplier_country, COUNT(p.productId) AS products_supplied, COUNT(DISTINCT p.categoryId) AS categories_served, SUM(p.unitsInStock * p.unitPrice) AS inventory_value FROM Supplier s LEFT JOIN Product p ON s.supplierId = p.supplierId GROUP BY s.supplierId, s.companyName, s.country), NetworkDependencies AS (SELECT supplier_country, COUNT(*) AS supplier_count, SUM(products_supplied) AS total_products, AVG(inventory_value) AS avg_inventory_value, CASE WHEN COUNT(*) = 1 THEN 'High Risk - Single Supplier' WHEN COUNT(*) <= 3 THEN 'Medium Risk - Few Suppliers' ELSE 'Low Risk - Multiple Suppliers' END AS dependency_risk FROM SupplyChainNetwork GROUP BY supplier_country), RiskMatrix AS (SELECT scn.supplier_name, scn.supplier_country, scn.products_supplied, scn.inventory_value, nd.dependency_risk, CASE WHEN scn.products_supplied > 10 AND nd.dependency_risk LIKE 'High Risk%' THEN 'Critical' WHEN scn.products_supplied > 5 OR nd.dependency_risk LIKE 'Medium Risk%' THEN 'Moderate' ELSE 'Low' END AS overall_risk FROM SupplyChainNetwork scn JOIN NetworkDependencies nd ON scn.supplier_country = nd.supplier_country) SELECT overall_risk, COUNT(*) AS supplier_count, AVG(products_supplied) AS avg_products, AVG(inventory_value) AS avg_inventory FROM RiskMatrix GROUP BY overall_risk ORDER BY FIELD(overall_risk, 'Critical', 'Moderate', 'Low');
