-- Problem 80: Comprehensive Data Quality Assessment
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to assess data quality across all tables and identify data integrity issues.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH DataQualityChecks AS (SELECT 'Customer' AS table_name, 'Missing Phone' AS issue_type, COUNT(*) AS issue_count FROM Customer WHERE phone IS NULL OR phone = '' UNION ALL SELECT 'Customer', 'Missing Email', COUNT(*) FROM Customer WHERE email IS NULL OR email = '' UNION ALL SELECT 'Product', 'Zero Price', COUNT(*) FROM Product WHERE unitPrice = 0 OR unitPrice IS NULL UNION ALL SELECT 'Product', 'Negative Stock', COUNT(*) FROM Product WHERE unitsInStock < 0 UNION ALL SELECT 'OrderDetail', 'Invalid Discount', COUNT(*) FROM OrderDetail WHERE discount < 0 OR discount > 1 UNION ALL SELECT 'Employee', 'Missing Hire Date', COUNT(*) FROM Employee WHERE hireDate IS NULL), QualityScores AS (SELECT table_name, SUM(issue_count) AS total_issues, COUNT(*) AS total_checks FROM DataQualityChecks GROUP BY table_name) SELECT table_name, total_issues, total_checks, (total_checks - total_issues) / total_checks * 100 AS quality_score FROM QualityScores ORDER BY quality_score;
