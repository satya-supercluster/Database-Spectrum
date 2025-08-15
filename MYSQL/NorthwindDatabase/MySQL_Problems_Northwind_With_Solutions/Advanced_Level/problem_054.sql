-- Problem 54: Cohort Analysis for Customer Retention
-- Level: Advanced
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to perform cohort analysis to understand customer retention patterns.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH CustomerCohorts AS (SELECT c.custId, DATE_FORMAT(MIN(s.orderDate), '%Y-%m') AS cohortMonth FROM Customer c JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId), CustomerOrders AS (SELECT co.custId, co.cohortMonth, DATE_FORMAT(s.orderDate, '%Y-%m') AS orderMonth, TIMESTAMPDIFF(MONTH, STR_TO_DATE(co.cohortMonth, '%Y-%m'), STR_TO_DATE(DATE_FORMAT(s.orderDate, '%Y-%m'), '%Y-%m')) AS monthNumber FROM CustomerCohorts co JOIN SalesOrder s ON co.custId = s.custId), CohortTable AS (SELECT cohortMonth, monthNumber, COUNT(DISTINCT custId) AS customers FROM CustomerOrders GROUP BY cohortMonth, monthNumber) SELECT cohortMonth, monthNumber, customers, FIRST_VALUE(customers) OVER (PARTITION BY cohortMonth ORDER BY monthNumber) AS cohortSize, (customers * 100.0 / FIRST_VALUE(customers) OVER (PARTITION BY cohortMonth ORDER BY monthNumber)) AS retentionRate FROM CohortTable ORDER BY cohortMonth, monthNumber;
