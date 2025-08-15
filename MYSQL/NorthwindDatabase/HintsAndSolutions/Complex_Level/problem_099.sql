-- Problem 99: Master Data Management and Data Governance
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to implement data governance checks and master data management principles across all entities.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH DataQualityMetrics AS (SELECT 'Customer' AS entity, 'Completeness' AS metric, (COUNT(*) - COUNT(CASE WHEN phone IS NULL OR phone = '' THEN 1 END)) * 100.0 / COUNT(*) AS score FROM Customer UNION ALL SELECT 'Customer', 'Accuracy', (COUNT(*) - COUNT(CASE WHEN LENGTH(postalCode) > 10 THEN 1 END)) * 100.0 / COUNT(*) FROM Customer UNION ALL SELECT 'Product', 'Completeness', (COUNT(*) - COUNT(CASE WHEN unitPrice IS NULL OR unitPrice <= 0 THEN 1 END)) * 100.0 / COUNT(*) FROM Product UNION ALL SELECT 'Product', 'Consistency', (COUNT(*) - COUNT(CASE WHEN discontinued NOT IN ('0', '1') THEN 1 END)) * 100.0 / COUNT(*) FROM Product), DataGovernance AS (SELECT entity, AVG(score) AS overall_quality_score, COUNT(*) AS metrics_checked, CASE WHEN AVG(score) >= 95 THEN 'Excellent' WHEN AVG(score) >= 85 THEN 'Good' WHEN AVG(score) >= 75 THEN 'Fair' ELSE 'Poor' END AS data_quality_grade FROM DataQualityMetrics GROUP BY entity), MasterDataConsistency AS (SELECT 'Category-Product Relationship' AS check_type, COUNT(p.productId) - COUNT(c.categoryId) AS inconsistencies FROM Product p LEFT JOIN Category c ON p.categoryId = c.categoryId UNION ALL SELECT 'Customer-Order Relationship', COUNT(s.orderId) - COUNT(c.custId) FROM SalesOrder s LEFT JOIN Customer c ON s.custId = c.custId), GovernanceReport AS (SELECT 'Data Quality' AS governance_area, entity AS sub_area, overall_quality_score AS score, data_quality_grade AS grade FROM DataGovernance UNION ALL SELECT 'Data Consistency', check_type, inconsistencies, CASE WHEN inconsistencies = 0 THEN 'Perfect' WHEN inconsistencies <= 5 THEN 'Good' ELSE 'Needs Attention' END FROM MasterDataConsistency) SELECT governance_area, sub_area, FORMAT(score, 2) AS score, grade FROM GovernanceReport ORDER BY governance_area, score DESC;
