-- Problem 48: Customer Segmentation by RFM Analysis
-- Level: Hard
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to perform RFM (Recency, Frequency, Monetary) analysis for customer segmentation.

-- ============================================================
-- SOLUTION:
-- ============================================================

WITH CustomerRFM AS (SELECT c.custId, c.companyName, DATEDIFF(CURDATE(), MAX(s.orderDate)) AS recency, COUNT(s.orderId) AS frequency, SUM(s.freight) AS monetary FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId, c.companyName), RFMScores AS (SELECT custId, companyName, recency, frequency, monetary, NTILE(5) OVER (ORDER BY recency DESC) AS R_Score, NTILE(5) OVER (ORDER BY frequency ASC) AS F_Score, NTILE(5) OVER (ORDER BY monetary ASC) AS M_Score FROM CustomerRFM) SELECT companyName, recency, frequency, monetary, R_Score, F_Score, M_Score, CONCAT(R_Score, F_Score, M_Score) AS RFM_Score FROM RFMScores ORDER BY RFM_Score DESC;
