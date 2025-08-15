-- Problem 78: Advanced Territory Performance Analytics
-- Level: Complex
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query for comprehensive territory analysis including market penetration and growth opportunities.

-- ============================================================
-- SOLUTION:
-- ============================================================

-- Territory performance with market analysis
WITH TerritoryMetrics AS (
  SELECT 
    t.territoryId,
    t.territorydescription,
    COUNT(DISTINCT et.employeeId) AS employee_count,
    COUNT(DISTINCT c.custId) AS customer_count,
    SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS territory_revenue
  FROM Territory t
  LEFT JOIN EmployeeTerritory et ON t.territoryId = et.territoryId
  LEFT JOIN SalesOrder s ON et.employeeId = s.employeeId
  LEFT JOIN Customer c ON s.custId = c.custId
  LEFT JOIN OrderDetail od ON s.orderId = od.orderId
  GROUP BY t.territoryId, t.territorydescription
)
SELECT 
  territorydescription,
  employee_count,
  customer_count,
  territory_revenue,
  territory_revenue / NULLIF(employee_count, 0) AS revenue_per_employee,
  CASE 
    WHEN territory_revenue > 10000 THEN 'High Performance'
    WHEN territory_revenue > 5000 THEN 'Medium Performance'
    ELSE 'Low Performance'
  END AS performance_tier
FROM TerritoryMetrics
ORDER BY territory_revenue DESC;
