#!/usr/bin/env python3
"""
MySQL Problems Generator for Northwind Database
Creates a structured folder system with 100 SQL problems from basic to complex
"""

import os
import json

# Define the problems structure
problems = {
    "basic": [
        {
            "id": 1,
            "title": "Select All Products",
            "statement": "Write a query to display all columns from the Product table.",
            "solution": "SELECT * FROM Product;"
        },
        {
            "id": 2,
            "title": "Select Customer Names",
            "statement": "Write a query to display only the company names from the Customer table.",
            "solution": "SELECT companyName FROM Customer;"
        },
        {
            "id": 3,
            "title": "Count Total Products",
            "statement": "Write a query to count the total number of products in the Product table.",
            "solution": "SELECT COUNT(*) FROM Product;"
        },
        {
            "id": 4,
            "title": "Products with Price Greater Than 20",
            "statement": "Write a query to display all products where the unit price is greater than 20.",
            "solution": "SELECT * FROM Product WHERE unitPrice > 20;"
        },
        {
            "id": 5,
            "title": "Customers from USA",
            "statement": "Write a query to display all customers from the USA.",
            "solution": "SELECT * FROM Customer WHERE country = 'USA';"
        },
        {
            "id": 6,
            "title": "Products Ordered by Price",
            "statement": "Write a query to display all products ordered by unit price in ascending order.",
            "solution": "SELECT * FROM Product ORDER BY unitPrice ASC;"
        },
        {
            "id": 7,
            "title": "Top 5 Most Expensive Products",
            "statement": "Write a query to display the top 5 most expensive products.",
            "solution": "SELECT * FROM Product ORDER BY unitPrice DESC LIMIT 5;"
        },
        {
            "id": 8,
            "title": "Employees with Manager ID",
            "statement": "Write a query to display all employees who have a manager (mgrId is not null).",
            "solution": "SELECT * FROM Employee WHERE mgrId IS NOT NULL;"
        },
        {
            "id": 9,
            "title": "Products in Stock",
            "statement": "Write a query to display products that have units in stock greater than 0.",
            "solution": "SELECT * FROM Product WHERE unitsInStock > 0;"
        },
        {
            "id": 10,
            "title": "Distinct Countries",
            "statement": "Write a query to display distinct countries from the Customer table.",
            "solution": "SELECT DISTINCT country FROM Customer;"
        },
        {
            "id": 11,
            "title": "Products with Names Starting with 'C'",
            "statement": "Write a query to display products whose names start with the letter 'C'.",
            "solution": "SELECT * FROM Product WHERE productName LIKE 'C%';"
        },
        {
            "id": 12,
            "title": "Orders from 2023",
            "statement": "Write a query to display all orders placed in the year 2023.",
            "solution": "SELECT * FROM SalesOrder WHERE YEAR(orderDate) = 2023;"
        },
        {
            "id": 13,
            "title": "Suppliers from Germany",
            "statement": "Write a query to display all suppliers from Germany.",
            "solution": "SELECT * FROM Supplier WHERE country = 'Germany';"
        },
        {
            "id": 14,
            "title": "Products with Reorder Level 0",
            "statement": "Write a query to display products with reorder level equal to 0.",
            "solution": "SELECT * FROM Product WHERE reorderLevel = 0;"
        },
        {
            "id": 15,
            "title": "Employee First and Last Names",
            "statement": "Write a query to display employee first names and last names concatenated.",
            "solution": "SELECT CONCAT(firstname, ' ', lastname) AS fullName FROM Employee;"
        },
        {
            "id": 16,
            "title": "Categories with Description",
            "statement": "Write a query to display category names and descriptions where description is not null.",
            "solution": "SELECT categoryName, description FROM Category WHERE description IS NOT NULL;"
        },
        {
            "id": 17,
            "title": "Products Between Price Range",
            "statement": "Write a query to display products with unit price between 10 and 50.",
            "solution": "SELECT * FROM Product WHERE unitPrice BETWEEN 10 AND 50;"
        },
        {
            "id": 18,
            "title": "Customers with Phone Numbers",
            "statement": "Write a query to display customers who have phone numbers (phone is not null).",
            "solution": "SELECT * FROM Customer WHERE phone IS NOT NULL;"
        },
        {
            "id": 19,
            "title": "Discontinued Products",
            "statement": "Write a query to display all discontinued products.",
            "solution": "SELECT * FROM Product WHERE discontinued = '1';"
        },
        {
            "id": 20,
            "title": "Orders Sorted by Date",
            "statement": "Write a query to display all orders sorted by order date in descending order.",
            "solution": "SELECT * FROM SalesOrder ORDER BY orderDate DESC;"
        }
    ],
    "intermediate": [
        {
            "id": 21,
            "title": "Products with Category Names",
            "statement": "Write a query to display product names along with their category names.",
            "solution": "SELECT p.productName, c.categoryName FROM Product p JOIN Category c ON p.categoryId = c.categoryId;"
        },
        {
            "id": 22,
            "title": "Count Products by Category",
            "statement": "Write a query to count the number of products in each category.",
            "solution": "SELECT c.categoryName, COUNT(p.productId) AS productCount FROM Category c LEFT JOIN Product p ON c.categoryId = p.categoryId GROUP BY c.categoryId, c.categoryName;"
        },
        {
            "id": 23,
            "title": "Average Product Price by Category",
            "statement": "Write a query to find the average product price for each category.",
            "solution": "SELECT c.categoryName, AVG(p.unitPrice) AS avgPrice FROM Category c JOIN Product p ON c.categoryId = p.categoryId GROUP BY c.categoryId, c.categoryName;"
        },
        {
            "id": 24,
            "title": "Customers and Their Orders Count",
            "statement": "Write a query to display customer names and the number of orders they have placed.",
            "solution": "SELECT c.companyName, COUNT(s.orderId) AS orderCount FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId, c.companyName;"
        },
        {
            "id": 25,
            "title": "Employees and Their Territories",
            "statement": "Write a query to display employee names and their territory descriptions.",
            "solution": "SELECT CONCAT(e.firstname, ' ', e.lastname) AS employeeName, t.territorydescription FROM Employee e JOIN EmployeeTerritory et ON e.employeeId = et.employeeId JOIN Territory t ON et.territoryId = t.territoryId;"
        },
        {
            "id": 26,
            "title": "Top 5 Customers by Order Value",
            "statement": "Write a query to find the top 5 customers by total order value (using freight as proxy).",
            "solution": "SELECT c.companyName, SUM(s.freight) AS totalOrderValue FROM Customer c JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId, c.companyName ORDER BY totalOrderValue DESC LIMIT 5;"
        },
        {
            "id": 27,
            "title": "Products Never Ordered",
            "statement": "Write a query to find products that have never been ordered.",
            "solution": "SELECT p.* FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId WHERE od.productId IS NULL;"
        },
        {
            "id": 28,
            "title": "Monthly Order Summary",
            "statement": "Write a query to show the number of orders placed in each month of 2023.",
            "solution": "SELECT MONTH(orderDate) AS month, COUNT(*) AS orderCount FROM SalesOrder WHERE YEAR(orderDate) = 2023 GROUP BY MONTH(orderDate) ORDER BY month;"
        },
        {
            "id": 29,
            "title": "Suppliers with Most Products",
            "statement": "Write a query to find suppliers who supply more than 5 products.",
            "solution": "SELECT s.companyName, COUNT(p.productId) AS productCount FROM Supplier s JOIN Product p ON s.supplierId = p.supplierId GROUP BY s.supplierId, s.companyName HAVING COUNT(p.productId) > 5;"
        },
        {
            "id": 30,
            "title": "Order Details with Product Info",
            "statement": "Write a query to display order details with product names and category names.",
            "solution": "SELECT od.orderDetailId, p.productName, c.categoryName, od.quantity, od.unitPrice FROM OrderDetail od JOIN Product p ON od.productId = p.productId JOIN Category c ON p.categoryId = c.categoryId;"
        },
        {
            "id": 31,
            "title": "Employees Hired in Same Year",
            "statement": "Write a query to find employees hired in the same year, grouped by hire year.",
            "solution": "SELECT YEAR(hireDate) AS hireYear, COUNT(*) AS employeeCount, GROUP_CONCAT(CONCAT(firstname, ' ', lastname)) AS employees FROM Employee GROUP BY YEAR(hireDate) HAVING COUNT(*) > 1;"
        },
        {
            "id": 32,
            "title": "Products with Low Stock Alert",
            "statement": "Write a query to find products where units in stock is less than or equal to reorder level.",
            "solution": "SELECT productName, unitsInStock, reorderLevel FROM Product WHERE unitsInStock <= reorderLevel AND discontinued = '0';"
        },
        {
            "id": 33,
            "title": "Customer Orders with Shipping Info",
            "statement": "Write a query to display customer orders with shipping company information.",
            "solution": "SELECT c.companyName AS customer, s.orderId, sh.companyName AS shipper, s.shippedDate FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN Shipper sh ON s.shipperid = sh.shipperId;"
        },
        {
            "id": 34,
            "title": "Region-wise Territory Count",
            "statement": "Write a query to count the number of territories in each region.",
            "solution": "SELECT r.regiondescription, COUNT(t.territoryId) AS territoryCount FROM Region r LEFT JOIN Territory t ON r.regionId = t.regionId GROUP BY r.regionId, r.regiondescription;"
        },
        {
            "id": 35,
            "title": "Products with Supplier Contact Info",
            "statement": "Write a query to display products with their supplier contact information.",
            "solution": "SELECT p.productName, s.companyName AS supplier, s.contactName, s.phone, s.email FROM Product p JOIN Supplier s ON p.supplierId = s.supplierId;"
        },
        {
            "id": 36,
            "title": "Orders Shipped Late",
            "statement": "Write a query to find orders that were shipped after the required date.",
            "solution": "SELECT orderId, orderDate, requiredDate, shippedDate FROM SalesOrder WHERE shippedDate > requiredDate;"
        },
        {
            "id": 37,
            "title": "Employee Hierarchy",
            "statement": "Write a query to display employees with their manager names.",
            "solution": "SELECT e1.firstname + ' ' + e1.lastname AS employee, e2.firstname + ' ' + e2.lastname AS manager FROM Employee e1 LEFT JOIN Employee e2 ON e1.mgrId = e2.employeeId;"
        },
        {
            "id": 38,
            "title": "Product Price Statistics by Category",
            "statement": "Write a query to show min, max, and average price for each category.",
            "solution": "SELECT c.categoryName, MIN(p.unitPrice) AS minPrice, MAX(p.unitPrice) AS maxPrice, AVG(p.unitPrice) AS avgPrice FROM Category c JOIN Product p ON c.categoryId = p.categoryId GROUP BY c.categoryId, c.categoryName;"
        },
        {
            "id": 39,
            "title": "Customers Without Orders",
            "statement": "Write a query to find customers who have never placed an order.",
            "solution": "SELECT c.* FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId WHERE s.custId IS NULL;"
        },
        {
            "id": 40,
            "title": "Order Value Analysis",
            "statement": "Write a query to calculate the total value of each order (quantity * unitPrice - discount).",
            "solution": "SELECT od.orderId, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalOrderValue FROM OrderDetail od GROUP BY od.orderId ORDER BY totalOrderValue DESC;"
        }
    ],
    "hard": [
        {
            "id": 41,
            "title": "Running Total of Orders by Month",
            "statement": "Write a query to calculate running total of orders by month for each year.",
            "solution": "SELECT YEAR(orderDate) AS year, MONTH(orderDate) AS month, COUNT(*) AS monthlyOrders, SUM(COUNT(*)) OVER (PARTITION BY YEAR(orderDate) ORDER BY MONTH(orderDate)) AS runningTotal FROM SalesOrder GROUP BY YEAR(orderDate), MONTH(orderDate) ORDER BY year, month;"
        },
        {
            "id": 42,
            "title": "Top 3 Products in Each Category by Sales",
            "statement": "Write a query to find the top 3 best-selling products in each category by quantity sold.",
            "solution": "WITH ProductSales AS (SELECT p.categoryId, p.productName, SUM(od.quantity) AS totalSold FROM Product p JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.categoryId, p.productId, p.productName), RankedProducts AS (SELECT categoryId, productName, totalSold, ROW_NUMBER() OVER (PARTITION BY categoryId ORDER BY totalSold DESC) AS rank FROM ProductSales) SELECT c.categoryName, rp.productName, rp.totalSold FROM RankedProducts rp JOIN Category c ON rp.categoryId = c.categoryId WHERE rp.rank <= 3;"
        },
        {
            "id": 43,
            "title": "Customer Loyalty Analysis",
            "statement": "Write a query to classify customers as 'New', 'Regular', or 'VIP' based on their order frequency and total spending.",
            "solution": "WITH CustomerStats AS (SELECT c.custId, c.companyName, COUNT(s.orderId) AS orderCount, SUM(s.freight) AS totalSpent FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId, c.companyName) SELECT companyName, orderCount, totalSpent, CASE WHEN orderCount = 0 THEN 'Inactive' WHEN orderCount <= 2 THEN 'New' WHEN orderCount <= 5 AND totalSpent <= 100 THEN 'Regular' ELSE 'VIP' END AS customerType FROM CustomerStats ORDER BY totalSpent DESC;"
        },
        {
            "id": 44,
            "title": "Quarterly Sales Growth",
            "statement": "Write a query to calculate quarter-over-quarter growth in order values.",
            "solution": "WITH QuarterlySales AS (SELECT YEAR(s.orderDate) AS year, QUARTER(s.orderDate) AS quarter, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalSales FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY YEAR(s.orderDate), QUARTER(s.orderDate)), SalesWithLag AS (SELECT year, quarter, totalSales, LAG(totalSales) OVER (ORDER BY year, quarter) AS prevQuarterSales FROM QuarterlySales) SELECT year, quarter, totalSales, prevQuarterSales, CASE WHEN prevQuarterSales IS NOT NULL THEN ((totalSales - prevQuarterSales) / prevQuarterSales) * 100 ELSE NULL END AS growthPercent FROM SalesWithLag ORDER BY year, quarter;"
        },
        {
            "id": 45,
            "title": "Product Recommendation System",
            "statement": "Write a query to find products frequently bought together (market basket analysis).",
            "solution": "SELECT p1.productName AS product1, p2.productName AS product2, COUNT(*) AS frequency FROM OrderDetail od1 JOIN OrderDetail od2 ON od1.orderId = od2.orderId AND od1.productId < od2.productId JOIN Product p1 ON od1.productId = p1.productId JOIN Product p2 ON od2.productId = p2.productId GROUP BY p1.productId, p1.productName, p2.productId, p2.productName HAVING COUNT(*) >= 3 ORDER BY frequency DESC;"
        },
        {
            "id": 46,
            "title": "Employee Performance Metrics",
            "statement": "Write a query to rank employees by their sales performance including total orders handled and revenue generated.",
            "solution": "WITH EmployeePerformance AS (SELECT e.employeeId, CONCAT(e.firstname, ' ', e.lastname) AS employeeName, COUNT(s.orderId) AS totalOrders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue FROM Employee e LEFT JOIN SalesOrder s ON e.employeeId = s.employeeId LEFT JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY e.employeeId, e.firstname, e.lastname) SELECT employeeName, totalOrders, totalRevenue, RANK() OVER (ORDER BY totalRevenue DESC) AS revenueRank, RANK() OVER (ORDER BY totalOrders DESC) AS orderRank FROM EmployeePerformance ORDER BY totalRevenue DESC;"
        },
        {
            "id": 47,
            "title": "Inventory Turnover Analysis",
            "statement": "Write a query to calculate inventory turnover ratio for each product.",
            "solution": "WITH ProductSales AS (SELECT p.productId, p.productName, p.unitsInStock, SUM(od.quantity) AS totalSold FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName, p.unitsInStock) SELECT productName, unitsInStock, totalSold, CASE WHEN unitsInStock > 0 THEN totalSold / unitsInStock ELSE NULL END AS turnoverRatio FROM ProductSales ORDER BY turnoverRatio DESC;"
        },
        {
            "id": 48,
            "title": "Customer Segmentation by RFM Analysis",
            "statement": "Write a query to perform RFM (Recency, Frequency, Monetary) analysis for customer segmentation.",
            "solution": "WITH CustomerRFM AS (SELECT c.custId, c.companyName, DATEDIFF(CURDATE(), MAX(s.orderDate)) AS recency, COUNT(s.orderId) AS frequency, SUM(s.freight) AS monetary FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId, c.companyName), RFMScores AS (SELECT custId, companyName, recency, frequency, monetary, NTILE(5) OVER (ORDER BY recency DESC) AS R_Score, NTILE(5) OVER (ORDER BY frequency ASC) AS F_Score, NTILE(5) OVER (ORDER BY monetary ASC) AS M_Score FROM CustomerRFM) SELECT companyName, recency, frequency, monetary, R_Score, F_Score, M_Score, CONCAT(R_Score, F_Score, M_Score) AS RFM_Score FROM RFMScores ORDER BY RFM_Score DESC;"
        },
        {
            "id": 49,
            "title": "Seasonal Sales Pattern Analysis",
            "statement": "Write a query to analyze seasonal sales patterns by comparing monthly sales across years.",
            "solution": "SELECT MONTH(s.orderDate) AS month, MONTHNAME(s.orderDate) AS monthName, YEAR(s.orderDate) AS year, COUNT(s.orderId) AS orderCount, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalSales, AVG(SUM(od.quantity * od.unitPrice * (1 - od.discount))) OVER (PARTITION BY MONTH(s.orderDate)) AS avgMonthlySales FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY YEAR(s.orderDate), MONTH(s.orderDate), MONTHNAME(s.orderDate) ORDER BY month, year;"
        },
        {
            "id": 50,
            "title": "Territory Performance Comparison",
            "statement": "Write a query to compare territory performance including sales, employee count, and customer coverage.",
            "solution": "WITH TerritoryStats AS (SELECT t.territoryId, t.territorydescription, r.regiondescription, COUNT(DISTINCT et.employeeId) AS employeeCount FROM Territory t JOIN Region r ON t.regionId = r.regionId LEFT JOIN EmployeeTerritory et ON t.territoryId = et.territoryId GROUP BY t.territoryId, t.territorydescription, r.regiondescription) SELECT ts.territorydescription, ts.regiondescription, ts.employeeCount FROM TerritoryStats ts ORDER BY ts.employeeCount DESC;"
        }
    ],
    "advanced": [
        {
            "id": 51,
            "title": "Dynamic Pricing Analysis",
            "statement": "Write a query to analyze price changes over time and their impact on sales volume.",
            "solution": "WITH PriceAnalysis AS (SELECT p.productId, p.productName, p.unitPrice AS currentPrice, od.unitPrice AS soldPrice, od.quantity, s.orderDate FROM Product p JOIN OrderDetail od ON p.productId = od.productId JOIN SalesOrder s ON od.orderId = s.orderId), PriceImpact AS (SELECT productName, soldPrice, SUM(quantity) AS totalQuantity, COUNT(*) AS orderCount, (soldPrice - MIN(soldPrice) OVER (PARTITION BY productId)) / MIN(soldPrice) OVER (PARTITION BY productId) * 100 AS priceChangePercent FROM PriceAnalysis GROUP BY productId, productName, soldPrice) SELECT productName, soldPrice, totalQuantity, orderCount, priceChangePercent FROM PriceImpact ORDER BY productName, soldPrice;"
        },
        {
            "id": 52,
            "title": "Customer Lifetime Value Prediction",
            "statement": "Write a query to calculate customer lifetime value based on historical data and predict future value.",
            "solution": "WITH CustomerHistory AS (SELECT c.custId, c.companyName, MIN(s.orderDate) AS firstOrder, MAX(s.orderDate) AS lastOrder, COUNT(s.orderId) AS totalOrders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalSpent, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avgOrderValue FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId, c.companyName), CustomerLTV AS (SELECT custId, companyName, totalOrders, totalSpent, avgOrderValue, DATEDIFF(lastOrder, firstOrder) + 1 AS customerLifespanDays, CASE WHEN DATEDIFF(lastOrder, firstOrder) > 0 THEN totalOrders / (DATEDIFF(lastOrder, firstOrder) / 365.25) ELSE totalOrders END AS ordersPerYear FROM CustomerHistory) SELECT companyName, totalSpent AS historicalValue, avgOrderValue, ordersPerYear, avgOrderValue * ordersPerYear AS predictedAnnualValue FROM CustomerLTV ORDER BY predictedAnnualValue DESC;"
        },
        {
            "id": 53,
            "title": "Supply Chain Optimization",
            "statement": "Write a query to identify potential supply chain bottlenecks and optimization opportunities.",
            "solution": "WITH SupplyChainMetrics AS (SELECT s.supplierId, s.companyName AS supplier, s.country AS supplierCountry, COUNT(p.productId) AS productCount, AVG(p.unitPrice) AS avgProductPrice, SUM(p.unitsInStock) AS totalInventory, AVG(p.reorderLevel) AS avgReorderLevel FROM Supplier s LEFT JOIN Product p ON s.supplierId = p.supplierId GROUP BY s.supplierId, s.companyName, s.country), ProductDemand AS (SELECT p.supplierId, SUM(od.quantity) AS totalDemand FROM Product p JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.supplierId) SELECT scm.supplier, scm.supplierCountry, scm.productCount, scm.totalInventory, pd.totalDemand, CASE WHEN pd.totalDemand > scm.totalInventory THEN 'High Demand - Low Inventory' WHEN pd.totalDemand < scm.totalInventory * 0.1 THEN 'Low Demand - High Inventory' ELSE 'Balanced' END AS inventoryStatus FROM SupplyChainMetrics scm LEFT JOIN ProductDemand pd ON scm.supplierId = pd.supplierId ORDER BY pd.totalDemand DESC;"
        },
        {
            "id": 54,
            "title": "Cohort Analysis for Customer Retention",
            "statement": "Write a query to perform cohort analysis to understand customer retention patterns.",
            "solution": "WITH CustomerCohorts AS (SELECT c.custId, DATE_FORMAT(MIN(s.orderDate), '%Y-%m') AS cohortMonth FROM Customer c JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId), CustomerOrders AS (SELECT co.custId, co.cohortMonth, DATE_FORMAT(s.orderDate, '%Y-%m') AS orderMonth, TIMESTAMPDIFF(MONTH, STR_TO_DATE(co.cohortMonth, '%Y-%m'), STR_TO_DATE(DATE_FORMAT(s.orderDate, '%Y-%m'), '%Y-%m')) AS monthNumber FROM CustomerCohorts co JOIN SalesOrder s ON co.custId = s.custId), CohortTable AS (SELECT cohortMonth, monthNumber, COUNT(DISTINCT custId) AS customers FROM CustomerOrders GROUP BY cohortMonth, monthNumber) SELECT cohortMonth, monthNumber, customers, FIRST_VALUE(customers) OVER (PARTITION BY cohortMonth ORDER BY monthNumber) AS cohortSize, (customers * 100.0 / FIRST_VALUE(customers) OVER (PARTITION BY cohortMonth ORDER BY monthNumber)) AS retentionRate FROM CohortTable ORDER BY cohortMonth, monthNumber;"
        },
        {
            "id": 55,
            "title": "ABC Analysis for Inventory Management",
            "statement": "Write a query to perform ABC analysis to categorize products based on their revenue contribution.",
            "solution": "WITH ProductRevenue AS (SELECT p.productId, p.productName, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue FROM Product p JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName), RevenueWithPercentage AS (SELECT productId, productName, totalRevenue, totalRevenue / SUM(totalRevenue) OVER () * 100 AS revenuePercentage, SUM(totalRevenue) OVER (ORDER BY totalRevenue DESC) / SUM(totalRevenue) OVER () * 100 AS cumulativePercentage FROM ProductRevenue), ABCClassification AS (SELECT productId, productName, totalRevenue, revenuePercentage, cumulativePercentage, CASE WHEN cumulativePercentage <= 80 THEN 'A' WHEN cumulativePercentage <= 95 THEN 'B' ELSE 'C' END AS abcCategory FROM RevenueWithPercentage) SELECT abcCategory, COUNT(*) AS productCount, SUM(totalRevenue) AS categoryRevenue, AVG(revenuePercentage) AS avgRevenuePercentage FROM ABCClassification GROUP BY abcCategory ORDER BY FIELD(abcCategory, 'A', 'B', 'C');"
        },
        {
            "id": 56,
            "title": "Cross-Selling Opportunity Matrix",
            "statement": "Write a query to create a cross-selling opportunity matrix showing product affinity scores.",
            "solution": "WITH ProductPairs AS (SELECT od1.productId AS product1, od2.productId AS product2, COUNT(*) AS coOccurrence FROM OrderDetail od1 JOIN OrderDetail od2 ON od1.orderId = od2.orderId AND od1.productId < od2.productId GROUP BY od1.productId, od2.productId), ProductFrequency AS (SELECT productId, COUNT(*) AS totalOrders FROM OrderDetail GROUP BY productId), AffinityScores AS (SELECT pp.product1, pp.product2, pp.coOccurrence, pf1.totalOrders AS product1Orders, pf2.totalOrders AS product2Orders, pp.coOccurrence / SQRT(pf1.totalOrders * pf2.totalOrders) AS affinityScore FROM ProductPairs pp JOIN ProductFrequency pf1 ON pp.product1 = pf1.productId JOIN ProductFrequency pf2 ON pp.product2 = pf2.productId) SELECT p1.productName AS product1, p2.productName AS product2, affinityScore FROM AffinityScores af JOIN Product p1 ON af.product1 = p1.productId JOIN Product p2 ON af.product2 = p2.productId WHERE affinityScore > 0.1 ORDER BY affinityScore DESC LIMIT 20;"
        },
        {
            "id": 57,
            "title": "Sales Forecasting Using Moving Averages",
            "statement": "Write a query to calculate 3-month and 6-month moving averages for sales forecasting.",
            "solution": "WITH MonthlySales AS (SELECT DATE_FORMAT(s.orderDate, '%Y-%m') AS month, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS monthlySales FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY DATE_FORMAT(s.orderDate, '%Y-%m')), MovingAverages AS (SELECT month, monthlySales, AVG(monthlySales) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS ma3, AVG(monthlySales) OVER (ORDER BY month ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) AS ma6, LAG(monthlySales, 1) OVER (ORDER BY month) AS prevMonthSales FROM MonthlySales) SELECT month, monthlySales, ma3, ma6, CASE WHEN prevMonthSales IS NOT NULL THEN ((monthlySales - prevMonthSales) / prevMonthSales) * 100 ELSE NULL END AS monthOverMonthGrowth FROM MovingAverages ORDER BY month;"
        },
        {
            "id": 58,
            "title": "Geographic Sales Distribution Analysis",
            "statement": "Write a query to analyze sales distribution across different geographic regions and identify expansion opportunities.",
            "solution": "WITH GeographicSales AS (SELECT c.country, c.city, COUNT(DISTINCT c.custId) AS customerCount, COUNT(s.orderId) AS orderCount, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.country, c.city), CountrySummary AS (SELECT country, SUM(customerCount) AS totalCustomers, SUM(orderCount) AS totalOrders, SUM(totalRevenue) AS countryRevenue, AVG(totalRevenue) AS avgCityRevenue FROM GeographicSales GROUP BY country) SELECT cs.country, cs.totalCustomers, cs.totalOrders, cs.countryRevenue, cs.avgCityRevenue, RANK() OVER (ORDER BY cs.countryRevenue DESC) AS revenueRank FROM CountrySummary cs ORDER BY cs.countryRevenue DESC;"
        },
        {
            "id": 59,
            "title": "Customer Churn Risk Analysis",
            "statement": "Write a query to identify customers at risk of churning based on their ordering patterns.",
            "solution": "WITH CustomerLastOrder AS (SELECT c.custId, c.companyName, MAX(s.orderDate) AS lastOrderDate, COUNT(s.orderId) AS totalOrders, AVG(DATEDIFF(s.orderDate, LAG(s.orderDate) OVER (PARTITION BY c.custId ORDER BY s.orderDate))) AS avgDaysBetweenOrders FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId, c.companyName), ChurnRisk AS (SELECT custId, companyName, lastOrderDate, totalOrders, avgDaysBetweenOrders, DATEDIFF(CURDATE(), lastOrderDate) AS daysSinceLastOrder, CASE WHEN DATEDIFF(CURDATE(), lastOrderDate) > (avgDaysBetweenOrders * 2) THEN 'High Risk' WHEN DATEDIFF(CURDATE(), lastOrderDate) > avgDaysBetweenOrders THEN 'Medium Risk' ELSE 'Low Risk' END AS churnRisk FROM CustomerLastOrder WHERE lastOrderDate IS NOT NULL) SELECT churnRisk, COUNT(*) AS customerCount, AVG(daysSinceLastOrder) AS avgDaysSinceLastOrder FROM ChurnRisk GROUP BY churnRisk ORDER BY FIELD(churnRisk, 'High Risk', 'Medium Risk', 'Low Risk');"
        },
        {
            "id": 60,
            "title": "Product Portfolio Optimization",
            "statement": "Write a query to analyze product portfolio performance and identify optimization opportunities.",
            "solution": "WITH ProductPerformance AS (SELECT p.productId, p.productName, c.categoryName, p.unitPrice, p.unitsInStock, SUM(od.quantity) AS totalSold, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue, COUNT(DISTINCT od.orderId) AS orderFrequency FROM Product p JOIN Category c ON p.categoryId = c.categoryId LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName, c.categoryName, p.unitPrice, p.unitsInStock), PortfolioAnalysis AS (SELECT productName, categoryName, unitPrice, unitsInStock, totalSold, totalRevenue, orderFrequency, CASE WHEN totalRevenue > (SELECT AVG(totalRevenue) FROM ProductPerformance) AND orderFrequency > (SELECT AVG(orderFrequency) FROM ProductPerformance) THEN 'Star' WHEN totalRevenue > (SELECT AVG(totalRevenue) FROM ProductPerformance) THEN 'Cash Cow' WHEN orderFrequency > (SELECT AVG(orderFrequency) FROM ProductPerformance) THEN 'Question Mark' ELSE 'Dog' END AS portfolioCategory FROM ProductPerformance) SELECT portfolioCategory, COUNT(*) AS productCount, AVG(totalRevenue) AS avgRevenue, AVG(orderFrequency) AS avgFrequency FROM PortfolioAnalysis GROUP BY portfolioCategory ORDER BY FIELD(portfolioCategory, 'Star', 'Cash Cow', 'Question Mark', 'Dog');"
        }
    ],
    "complex": [
        {
            "id": 61,
            "title": "Multi-dimensional Sales Cube Analysis",
            "statement": "Write a query to create a sales cube with dimensions: time, product category, customer country, and employee.",
            "solution": "SELECT YEAR(s.orderDate) AS year, QUARTER(s.orderDate) AS quarter, c.categoryName, cust.country, CONCAT(e.firstname, ' ', e.lastname) AS employee, COUNT(s.orderId) AS orderCount, SUM(od.quantity) AS totalQuantity, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avgOrderValue FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId JOIN Product p ON od.productId = p.productId JOIN Category c ON p.categoryId = c.categoryId JOIN Customer cust ON s.custId = cust.custId LEFT JOIN Employee e ON s.employeeId = e.employeeId GROUP BY YEAR(s.orderDate), QUARTER(s.orderDate), c.categoryName, cust.country, e.employeeId, e.firstname, e.lastname WITH ROLLUP ORDER BY year, quarter, c.categoryName, cust.country, employee;"
        },
        {
            "id": 62,
            "title": "Dynamic Customer Segmentation with Behavioral Scoring",
            "statement": "Write a complex query to create dynamic customer segments based on multiple behavioral factors and scoring algorithms.",
            "solution": "WITH CustomerBehavior AS (SELECT c.custId, c.companyName, COUNT(DISTINCT s.orderId) AS orderFrequency, AVG(DATEDIFF(s.orderDate, LAG(s.orderDate) OVER (PARTITION BY c.custId ORDER BY s.orderDate))) AS avgOrderInterval, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalSpent, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avgOrderValue, COUNT(DISTINCT p.categoryId) AS categoryDiversity, MAX(s.orderDate) AS lastOrderDate, MIN(s.orderDate) AS firstOrderDate FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId JOIN Product p ON od.productId = p.productId GROUP BY c.custId, c.companyName), ScoringMetrics AS (SELECT custId, companyName, orderFrequency, avgOrderInterval, totalSpent, avgOrderValue, categoryDiversity, DATEDIFF(CURDATE(), lastOrderDate) AS daysSinceLastOrder, DATEDIFF(lastOrderDate, firstOrderDate) AS customerLifespan, CASE WHEN orderFrequency >= 10 THEN 5 WHEN orderFrequency >= 5 THEN 4 WHEN orderFrequency >= 3 THEN 3 WHEN orderFrequency >= 1 THEN 2 ELSE 1 END AS frequencyScore, CASE WHEN totalSpent >= 5000 THEN 5 WHEN totalSpent >= 2000 THEN 4 WHEN totalSpent >= 1000 THEN 3 WHEN totalSpent >= 500 THEN 2 ELSE 1 END AS monetaryScore, CASE WHEN DATEDIFF(CURDATE(), lastOrderDate) <= 30 THEN 5 WHEN DATEDIFF(CURDATE(), lastOrderDate) <= 90 THEN 4 WHEN DATEDIFF(CURDATE(), lastOrderDate) <= 180 THEN 3 WHEN DATEDIFF(CURDATE(), lastOrderDate) <= 365 THEN 2 ELSE 1 END AS recencyScore FROM CustomerBehavior), FinalSegmentation AS (SELECT custId, companyName, frequencyScore, monetaryScore, recencyScore, (frequencyScore + monetaryScore + recencyScore) AS totalScore, CASE WHEN (frequencyScore + monetaryScore + recencyScore) >= 13 THEN 'Champions' WHEN (frequencyScore + monetaryScore + recencyScore) >= 10 AND recencyScore >= 3 THEN 'Loyal Customers' WHEN recencyScore >= 4 AND frequencyScore <= 2 THEN 'New Customers' WHEN monetaryScore >= 4 AND recencyScore <= 2 THEN 'At Risk' WHEN recencyScore <= 2 AND frequencyScore <= 2 THEN 'Lost Customers' ELSE 'Regular Customers' END AS segment FROM ScoringMetrics) SELECT segment, COUNT(*) AS customerCount, AVG(totalScore) AS avgScore, MIN(totalScore) AS minScore, MAX(totalScore) AS maxScore FROM FinalSegmentation GROUP BY segment ORDER BY avgScore DESC;"
        },
        {
            "id": 63,
            "title": "Advanced Inventory Optimization with Demand Forecasting",
            "statement": "Write a query to optimize inventory levels using demand forecasting, seasonality analysis, and safety stock calculations.",
            "solution": "WITH MonthlyDemand AS (SELECT p.productId, p.productName, DATE_FORMAT(s.orderDate, '%Y-%m') AS month, SUM(od.quantity) AS monthlyQuantity FROM Product p JOIN OrderDetail od ON p.productId = od.productId JOIN SalesOrder s ON od.orderId = s.orderId GROUP BY p.productId, p.productName, DATE_FORMAT(s.orderDate, '%Y-%m')), DemandStats AS (SELECT productId, productName, AVG(monthlyQuantity) AS avgMonthlyDemand, STDDEV(monthlyQuantity) AS demandStdDev, MAX(monthlyQuantity) AS maxMonthlyDemand, MIN(monthlyQuantity) AS minMonthlyDemand, COUNT(*) AS monthsWithSales FROM MonthlyDemand GROUP BY productId, productName), SeasonalityFactors AS (SELECT md.productId, MONTH(STR_TO_DATE(md.month, '%Y-%m')) AS monthNum, AVG(md.monthlyQuantity) AS avgForMonth, ds.avgMonthlyDemand, (AVG(md.monthlyQuantity) / ds.avgMonthlyDemand) AS seasonalityFactor FROM MonthlyDemand md JOIN DemandStats ds ON md.productId = ds.productId GROUP BY md.productId, MONTH(STR_TO_DATE(md.month, '%Y-%m')), ds.avgMonthlyDemand), InventoryOptimization AS (SELECT p.productId, p.productName, p.unitsInStock AS currentStock, ds.avgMonthlyDemand, ds.demandStdDev, p.reorderLevel AS currentReorderLevel, CEIL(ds.avgMonthlyDemand * 1.5) AS recommendedReorderLevel, CEIL(ds.avgMonthlyDemand * 3 + ds.demandStdDev * 1.65) AS recommendedMaxStock, sf.seasonalityFactor AS currentSeasonFactor, CASE WHEN p.unitsInStock < ds.avgMonthlyDemand * 0.5 THEN 'Urgent Reorder' WHEN p.unitsInStock < ds.avgMonthlyDemand THEN 'Reorder Soon' WHEN p.unitsInStock > ds.avgMonthlyDemand * 4 THEN 'Overstocked' ELSE 'Optimal' END AS stockStatus FROM Product p JOIN DemandStats ds ON p.productId = ds.productId LEFT JOIN SeasonalityFactors sf ON p.productId = sf.productId AND sf.monthNum = MONTH(CURDATE()) WHERE ds.avgMonthlyDemand > 0) SELECT stockStatus, COUNT(*) AS productCount, AVG(currentStock) AS avgCurrentStock, AVG(recommendedMaxStock) AS avgRecommendedStock, SUM(CASE WHEN stockStatus IN ('Urgent Reorder', 'Reorder Soon') THEN recommendedMaxStock - currentStock ELSE 0 END) AS totalReorderNeeded FROM InventoryOptimization GROUP BY stockStatus ORDER BY FIELD(stockStatus, 'Urgent Reorder', 'Reorder Soon', 'Optimal', 'Overstocked');"
        },
        {
            "id": 64,
            "title": "Customer Journey Analysis with Touchpoint Attribution",
            "statement": "Write a query to analyze customer journey paths and attribute value to different touchpoints in the sales process.",
            "solution": "WITH CustomerOrderSequence AS (SELECT c.custId, c.companyName, s.orderId, s.orderDate, ROW_NUMBER() OVER (PARTITION BY c.custId ORDER BY s.orderDate) AS orderSequence, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS orderValue, LEAD(s.orderDate) OVER (PARTITION BY c.custId ORDER BY s.orderDate) AS nextOrderDate FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId, c.companyName, s.orderId, s.orderDate), JourneyAnalysis AS (SELECT custId, companyName, orderSequence, orderValue, CASE WHEN orderSequence = 1 THEN 'Acquisition' WHEN orderSequence = 2 THEN 'Activation' WHEN orderSequence <= 5 THEN 'Retention' ELSE 'Loyalty' END AS journeyStage, CASE WHEN nextOrderDate IS NOT NULL THEN DATEDIFF(nextOrderDate, orderDate) ELSE NULL END AS daysToNextOrder FROM CustomerOrderSequence), TouchpointValue AS (SELECT journeyStage, COUNT(*) AS touchpointCount, AVG(orderValue) AS avgOrderValue, SUM(orderValue) AS totalValue, AVG(daysToNextOrder) AS avgDaysToNext FROM JourneyAnalysis GROUP BY journeyStage), AttributionModel AS (SELECT journeyStage, touchpointCount, avgOrderValue, totalValue, avgDaysToNext, totalValue / SUM(totalValue) OVER () * 100 AS valueAttribution, CASE WHEN journeyStage = 'Acquisition' THEN 0.4 WHEN journeyStage = 'Activation' THEN 0.3 WHEN journeyStage = 'Retention' THEN 0.2 ELSE 0.1 END AS attributionWeight FROM TouchpointValue) SELECT journeyStage, touchpointCount, avgOrderValue, totalValue, valueAttribution, attributionWeight, (totalValue * attributionWeight) AS weightedValue FROM AttributionModel ORDER BY FIELD(journeyStage, 'Acquisition', 'Activation', 'Retention', 'Loyalty');"
        },
        {
            "id": 65,
            "title": "Predictive Analytics for Sales Forecasting",
            "statement": "Write a query implementing time series analysis with trend and seasonality components for sales forecasting.",
            "solution": "WITH DailySales AS (SELECT DATE(s.orderDate) AS saleDate, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS dailySales FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY DATE(s.orderDate)), TimeSeriesData AS (SELECT saleDate, dailySales, ROW_NUMBER() OVER (ORDER BY saleDate) AS timeIndex, DAYOFWEEK(saleDate) AS dayOfWeek, MONTH(saleDate) AS month, QUARTER(saleDate) AS quarter FROM DailySales), MovingAverages AS (SELECT saleDate, dailySales, timeIndex, dayOfWeek, month, quarter, AVG(dailySales) OVER (ORDER BY saleDate ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS ma7, AVG(dailySales) OVER (ORDER BY saleDate ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) AS ma30 FROM TimeSeriesData), TrendCalculation AS (SELECT saleDate, dailySales, timeIndex, ma7, ma30, (ma7 - LAG(ma7, 7) OVER (ORDER BY saleDate)) / 7 AS weeklyTrend, (ma30 - LAG(ma30, 30) OVER (ORDER BY saleDate)) / 30 AS monthlyTrend FROM MovingAverages), SeasonalDecomposition AS (SELECT t.saleDate, t.dailySales, t.ma30 AS trend, t.dailySales / NULLIF(t.ma30, 0) AS seasonal, AVG(t.dailySales / NULLIF(t.ma30, 0)) OVER (PARTITION BY t.dayOfWeek) AS weeklySeasonality, AVG(t.dailySales / NULLIF(t.ma30, 0)) OVER (PARTITION BY t.month) AS monthlySeasonality FROM TrendCalculation t WHERE t.ma30 IS NOT NULL), ForecastModel AS (SELECT saleDate, dailySales, trend, seasonal, weeklySeasonality, monthlySeasonality, trend * weeklySeasonality * monthlySeasonality AS forecastValue, ABS(dailySales - (trend * weeklySeasonality * monthlySeasonality)) / NULLIF(dailySales, 0) * 100 AS forecastError FROM SeasonalDecomposition WHERE trend IS NOT NULL) SELECT DATE_FORMAT(saleDate, '%Y-%m') AS month, AVG(dailySales) AS actualSales, AVG(forecastValue) AS forecastedSales, AVG(forecastError) AS avgError FROM ForecastModel GROUP BY DATE_FORMAT(saleDate, '%Y-%m') ORDER BY month DESC LIMIT 12;"
        },
        {
            "id": 66,
            "title": "Multi-Level Marketing Attribution Model",
            "statement": "Write a query to implement a sophisticated attribution model that tracks customer acquisition and assigns credit across multiple touchpoints.",
            "solution": "WITH CustomerFirstOrder AS (SELECT c.custId, MIN(s.orderDate) AS firstOrderDate, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS firstOrderValue FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId), CustomerLifetimeValue AS (SELECT c.custId, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalLTV, COUNT(DISTINCT s.orderId) AS totalOrders FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId), EmployeeAttribution AS (SELECT e.employeeId, CONCAT(e.firstname, ' ', e.lastname) AS employeeName, COUNT(DISTINCT cfo.custId) AS customersAcquired, SUM(clv.totalLTV) AS totalAttributedRevenue, AVG(clv.totalLTV) AS avgCustomerValue FROM Employee e JOIN SalesOrder s ON e.employeeId = s.employeeId JOIN CustomerFirstOrder cfo ON s.custId = cfo.custId AND s.orderDate = cfo.firstOrderDate JOIN CustomerLifetimeValue clv ON cfo.custId = clv.custId GROUP BY e.employeeId, e.firstname, e.lastname), TerritoryAttribution AS (SELECT t.territoryId, t.territorydescription, r.regiondescription, COUNT(DISTINCT ea.employeeId) AS employeeCount, SUM(ea.customersAcquired) AS territoryCustomers, SUM(ea.totalAttributedRevenue) AS territoryRevenue FROM Territory t JOIN Region r ON t.regionId = r.regionId JOIN EmployeeTerritory et ON t.territoryId = et.territoryId JOIN EmployeeAttribution ea ON et.employeeId = ea.employeeId GROUP BY t.territoryId, t.territorydescription, r.regiondescription), AttributionHierarchy AS (SELECT ta.regiondescription, ta.territoryId, ta.territorydescription, ta.employeeCount, ta.territoryCustomers, ta.territoryRevenue, ta.territoryRevenue / SUM(ta.territoryRevenue) OVER (PARTITION BY ta.regiondescription) * 100 AS regionContribution FROM TerritoryAttribution ta) SELECT regiondescription, COUNT(territoryId) AS territories, SUM(employeeCount) AS totalEmployees, SUM(territoryCustomers) AS regionCustomers, SUM(territoryRevenue) AS regionRevenue, AVG(regionContribution) AS avgTerritoryContribution FROM AttributionHierarchy GROUP BY regiondescription ORDER BY regionRevenue DESC;"
        },
        {
            "id": 67,
            "title": "Advanced Price Elasticity and Optimization Analysis",
            "statement": "Write a query to calculate price elasticity of demand and suggest optimal pricing strategies for products.",
            "solution": "WITH PricePoints AS (SELECT p.productId, p.productName, od.unitPrice, SUM(od.quantity) AS quantitySold, COUNT(DISTINCT od.orderId) AS orderCount, AVG(od.discount) AS avgDiscount FROM Product p JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName, od.unitPrice), PriceElasticity AS (SELECT pp1.productId, pp1.productName, pp1.unitPrice AS price1, pp2.unitPrice AS price2, pp1.quantitySold AS quantity1, pp2.quantitySold AS quantity2, CASE WHEN pp1.unitPrice != pp2.unitPrice AND pp1.quantitySold != pp2.quantitySold THEN ((pp2.quantitySold - pp1.quantitySold) / pp1.quantitySold) / ((pp2.unitPrice - pp1.unitPrice) / pp1.unitPrice) ELSE NULL END AS priceElasticity FROM PricePoints pp1 JOIN PricePoints pp2 ON pp1.productId = pp2.productId AND pp1.unitPrice < pp2.unitPrice), OptimalPricing AS (SELECT pe.productId, pe.productName, AVG(pe.priceElasticity) AS avgElasticity, MIN(pp.unitPrice) AS minPrice, MAX(pp.unitPrice) AS maxPrice, AVG(pp.unitPrice) AS avgPrice, SUM(pp.quantitySold) AS totalQuantity FROM PriceElasticity pe JOIN PricePoints pp ON pe.productId = pp.productId GROUP BY pe.productId, pe.productName HAVING AVG(pe.priceElasticity) IS NOT NULL), PricingStrategy AS (SELECT productId, productName, avgElasticity, minPrice, maxPrice, avgPrice, CASE WHEN avgElasticity > -1 THEN 'Inelastic - Increase Price' WHEN avgElasticity BETWEEN -2 AND -1 THEN 'Unit Elastic - Maintain Price' ELSE 'Elastic - Consider Decrease' END AS pricingRecommendation, CASE WHEN avgElasticity > -1 THEN avgPrice * 1.1 WHEN avgElasticity < -2 THEN avgPrice * 0.95 ELSE avgPrice END AS recommendedPrice FROM OptimalPricing) SELECT pricingRecommendation, COUNT(*) AS productCount, AVG(avgElasticity) AS avgElasticity, AVG(recommendedPrice - avgPrice) AS avgPriceChange FROM PricingStrategy GROUP BY pricingRecommendation;"
        },
        {
            "id": 68,
            "title": "Customer Network Analysis and Influence Mapping",
            "statement": "Write a query to identify influential customers and map customer networks based on similar purchasing patterns.",
            "solution": "WITH CustomerProductMatrix AS (SELECT c.custId, c.companyName, p.productId, SUM(od.quantity) AS totalQuantity FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId JOIN Product p ON od.productId = p.productId GROUP BY c.custId, c.companyName, p.productId), CustomerSimilarity AS (SELECT cpm1.custId AS customer1, cpm2.custId AS customer2, cpm1.companyName AS company1, cpm2.companyName AS company2, COUNT(CASE WHEN cpm1.productId = cpm2.productId THEN 1 END) AS commonProducts, SQRT(SUM(cpm1.totalQuantity * cpm1.totalQuantity)) AS magnitude1, SQRT(SUM(cpm2.totalQuantity * cpm2.totalQuantity)) AS magnitude2, SUM(cpm1.totalQuantity * cpm2.totalQuantity) AS dotProduct FROM CustomerProductMatrix cpm1 JOIN CustomerProductMatrix cpm2 ON cpm1.custId < cpm2.custId AND cpm1.productId = cpm2.productId GROUP BY cpm1.custId, cpm2.custId, cpm1.companyName, cmp2.companyName HAVING COUNT(*) >= 3), CosineSimilarity AS (SELECT customer1, customer2, company1, company2, commonProducts, dotProduct / (magnitude1 * magnitude2) AS similarityScore FROM CustomerSimilarity WHERE magnitude1 > 0 AND magnitude2 > 0), InfluenceMetrics AS (SELECT c.custId, c.companyName, COUNT(DISTINCT s.orderId) AS orderCount, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalSpent, COUNT(DISTINCT p.productId) AS uniqueProducts, AVG(cs.similarityScore) AS avgSimilarityScore FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId JOIN Product p ON od.productId = p.productId LEFT JOIN CosineSimilarity cs ON c.custId IN (cs.customer1, cs.customer2) GROUP BY c.custId, c.companyName), InfluenceRanking AS (SELECT custId, companyName, orderCount, totalSpent, uniqueProducts, avgSimilarityScore, (COALESCE(avgSimilarityScore, 0) * 0.3 + (orderCount / MAX(orderCount) OVER ()) * 0.4 + (totalSpent / MAX(totalSpent) OVER ()) * 0.3) AS influenceScore FROM InfluenceMetrics) SELECT companyName, orderCount, totalSpent, uniqueProducts, avgSimilarityScore, influenceScore, CASE WHEN influenceScore >= 0.8 THEN 'High Influence' WHEN influenceScore >= 0.6 THEN 'Medium Influence' ELSE 'Low Influence' END AS influenceLevel FROM InfluenceRanking ORDER BY influenceScore DESC LIMIT 50;"
        },
        {
            "id": 69,
            "title": "Supply Chain Risk Assessment and Mitigation Analysis",
            "statement": "Write a query to assess supply chain risks and identify mitigation strategies based on supplier dependency and geographic concentration.",
            "solution": "WITH SupplierDependency AS (SELECT s.supplierId, s.companyName AS supplierName, s.country AS supplierCountry, COUNT(p.productId) AS productsSupplied, SUM(p.unitsInStock * p.unitPrice) AS inventoryValue, SUM(od.quantity) AS totalDemand FROM Supplier s JOIN Product p ON s.supplierId = p.supplierId LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY s.supplierId, s.companyName, s.country), CategoryRisk AS (SELECT c.categoryId, c.categoryName, COUNT(DISTINCT p.supplierId) AS supplierCount, COUNT(p.productId) AS productCount, AVG(sd.inventoryValue) AS avgInventoryValue FROM Category c JOIN Product p ON c.categoryId = p.categoryId JOIN SupplierDependency sd ON p.supplierId = sd.supplierId GROUP BY c.categoryId, c.categoryName), GeographicConcentration AS (SELECT sd.supplierCountry, COUNT(sd.supplierId) AS supplierCount, SUM(sd.productsSupplied) AS totalProducts, SUM(sd.inventoryValue) AS totalInventoryValue, COUNT(DISTINCT c.categoryId) AS categoriesServed FROM SupplierDependency sd JOIN Product p ON sd.supplierId = p.supplierId JOIN Category c ON p.categoryId = c.categoryId GROUP BY sd.supplierCountry), RiskAssessment AS (SELECT sd.supplierId, sd.supplierName, sd.supplierCountry, sd.productsSupplied, sd.inventoryValue, sd.totalDemand, gc.supplierCount AS countrySuppliers, cr.supplierCount AS categorySuppliers, CASE WHEN sd.productsSupplied > 10 THEN 'High Dependency' WHEN sd.productsSupplied > 5 THEN 'Medium Dependency' ELSE 'Low Dependency' END AS dependencyRisk, CASE WHEN gc.supplierCount <= 2 THEN 'High Geographic Risk' WHEN gc.supplierCount <= 5 THEN 'Medium Geographic Risk' ELSE 'Low Geographic Risk' END AS geographicRisk FROM SupplierDependency sd JOIN GeographicConcentration gc ON sd.supplierCountry = gc.supplierCountry JOIN Product p ON sd.supplierId = p.supplierId JOIN CategoryRisk cr ON p.categoryId = cr.categoryId), RiskMitigation AS (SELECT dependencyRisk, geographicRisk, COUNT(*) AS supplierCount, AVG(inventoryValue) AS avgInventoryValue, SUM(totalDemand) AS totalDemand, CASE WHEN dependencyRisk = 'High Dependency' AND geographicRisk = 'High Geographic Risk' THEN 'Critical - Diversify Immediately' WHEN dependencyRisk = 'High Dependency' OR geographicRisk = 'High Geographic Risk' THEN 'High - Plan Diversification' WHEN dependencyRisk = 'Medium Dependency' AND geographicRisk = 'Medium Geographic Risk' THEN 'Medium - Monitor Closely' ELSE 'Low - Maintain Current Strategy' END AS mitigationStrategy FROM RiskAssessment GROUP BY dependencyRisk, geographicRisk) SELECT mitigationStrategy, supplierCount, avgInventoryValue, totalDemand, (totalDemand / SUM(totalDemand) OVER ()) * 100 AS demandPercentage FROM RiskMitigation ORDER BY FIELD(mitigationStrategy, 'Critical - Diversify Immediately', 'High - Plan Diversification', 'Medium - Monitor Closely', 'Low - Maintain Current Strategy');"
        },
        {
            "id": 70,
            "title": "Dynamic Revenue Optimization with Real-time Adjustments",
            "statement": "Write a query to implement dynamic pricing and revenue optimization based on real-time demand patterns and competitive positioning.",
            "solution": "WITH RealTimeDemand AS (SELECT p.productId, p.productName, p.unitPrice AS currentPrice, SUM(CASE WHEN s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 30 DAY) THEN od.quantity ELSE 0 END) AS recent30DayDemand, SUM(CASE WHEN s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 7 DAY) THEN od.quantity ELSE 0 END) AS recent7DayDemand, AVG(od.unitPrice) AS avgSoldPrice, COUNT(DISTINCT s.custId) AS uniqueCustomers FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId LEFT JOIN SalesOrder s ON od.orderId = s.orderId GROUP BY p.productId, p.productName, p.unitPrice), DemandTrend AS (SELECT productId, productName, currentPrice, recent30DayDemand, recent7DayDemand, avgSoldPrice, uniqueCustomers, CASE WHEN recent7DayDemand > (recent30DayDemand / 4) THEN 'Increasing' WHEN recent7DayDemand < (recent30DayDemand / 6) THEN 'Decreasing' ELSE 'Stable' END AS demandTrend FROM RealTimeDemand), CompetitivePosition AS (SELECT dt.productId, dt.productName, dt.currentPrice, dt.demandTrend, c.categoryName, AVG(p2.unitPrice) AS categoryAvgPrice, CASE WHEN dt.currentPrice > AVG(p2.unitPrice) * 1.2 THEN 'Premium' WHEN dt.currentPrice < AVG(p2.unitPrice) * 0.8 THEN 'Budget' ELSE 'Competitive' END AS pricePosition FROM DemandTrend dt JOIN Product p ON dt.productId = p.productId JOIN Category c ON p.categoryId = c.categoryId JOIN Product p2 ON c.categoryId = p2.categoryId GROUP BY dt.productId, dt.productName, dt.currentPrice, dt.demandTrend, c.categoryName), OptimizationStrategy AS (SELECT productId, productName, currentPrice, demandTrend, pricePosition, categoryAvgPrice, CASE WHEN demandTrend = 'Increasing' AND pricePosition = 'Budget' THEN currentPrice * 1.15 WHEN demandTrend = 'Increasing' AND pricePosition = 'Competitive' THEN currentPrice * 1.08 WHEN demandTrend = 'Decreasing' AND pricePosition = 'Premium' THEN currentPrice * 0.92 WHEN demandTrend = 'Decreasing' THEN currentPrice * 0.95 ELSE currentPrice END AS optimizedPrice FROM CompetitivePosition) SELECT demandTrend, pricePosition, COUNT(*) AS productCount, AVG(currentPrice) AS avgCurrentPrice, AVG(optimizedPrice) AS avgOptimizedPrice, AVG((optimizedPrice - currentPrice) / currentPrice * 100) AS avgPriceChange FROM OptimizationStrategy GROUP BY demandTrend, pricePosition ORDER BY demandTrend, pricePosition;"
        },
        {
            "id": 71,
            "title": "Advanced Customer Lifetime Value with Churn Prediction",
            "statement": "Write a query to calculate sophisticated CLV models incorporating churn probability and future value predictions.",
            "solution": "WITH CustomerTransactionHistory AS (SELECT c.custId, c.companyName, COUNT(s.orderId) AS totalOrders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue, MIN(s.orderDate) AS firstOrderDate, MAX(s.orderDate) AS lastOrderDate, AVG(DATEDIFF(s.orderDate, LAG(s.orderDate) OVER (PARTITION BY c.custId ORDER BY s.orderDate))) AS avgDaysBetweenOrders, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avgOrderValue FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId, c.companyName), ChurnProbability AS (SELECT custId, companyName, totalOrders, totalRevenue, avgOrderValue, DATEDIFF(CURDATE(), lastOrderDate) AS daysSinceLastOrder, avgDaysBetweenOrders, CASE WHEN DATEDIFF(CURDATE(), lastOrderDate) > (avgDaysBetweenOrders * 3) THEN 0.8 WHEN DATEDIFF(CURDATE(), lastOrderDate) > (avgDaysBetweenOrders * 2) THEN 0.6 WHEN DATEDIFF(CURDATE(), lastOrderDate) > avgDaysBetweenOrders THEN 0.3 ELSE 0.1 END AS churnProbability FROM CustomerTransactionHistory WHERE avgDaysBetweenOrders IS NOT NULL), CLVCalculation AS (SELECT custId, companyName, totalRevenue AS historicalCLV, avgOrderValue, totalOrders, churnProbability, (1 - churnProbability) AS retentionProbability, avgOrderValue * (totalOrders / GREATEST(DATEDIFF(lastOrderDate, firstOrderDate) / 365.25, 0.25)) AS annualOrderRate, avgOrderValue * (totalOrders / GREATEST(DATEDIFF(lastOrderDate, firstOrderDate) / 365.25, 0.25)) * (1 - churnProbability) / 0.1 AS predictedCLV FROM ChurnProbability cp JOIN CustomerTransactionHistory cth ON cp.custId = cth.custId), CLVSegmentation AS (SELECT custId, companyName, historicalCLV, predictedCLV, churnProbability, retentionProbability, CASE WHEN predictedCLV > 5000 AND churnProbability < 0.3 THEN 'High Value - Low Risk' WHEN predictedCLV > 5000 AND churnProbability >= 0.3 THEN 'High Value - High Risk' WHEN predictedCLV > 1000 AND churnProbability < 0.5 THEN 'Medium Value - Low Risk' WHEN predictedCLV > 1000 AND churnProbability >= 0.5 THEN 'Medium Value - High Risk' ELSE 'Low Value' END AS clvSegment FROM CLVCalculation) SELECT clvSegment, COUNT(*) AS customerCount, AVG(historicalCLV) AS avgHistoricalCLV, AVG(predictedCLV) AS avgPredictedCLV, AVG(churnProbability) AS avgChurnProbability, SUM(predictedCLV * retentionProbability) AS totalProjectedValue FROM CLVSegmentation GROUP BY clvSegment ORDER BY avgPredictedCLV DESC;"
        },
        {
            "id": 72,
            "title": "Machine Learning Feature Engineering for Sales Prediction",
            "statement": "Write a query to create comprehensive feature sets for machine learning models to predict sales performance.",
            "solution": "WITH BaseFeatures AS (SELECT p.productId, p.productName, c.categoryName, s.companyName AS supplierName, p.unitPrice, p.unitsInStock, p.reorderLevel, CASE WHEN p.discontinued = '1' THEN 1 ELSE 0 END AS isDiscontinued, LENGTH(p.productName) AS nameLength, CASE WHEN p.quantityPerUnit IS NOT NULL THEN 1 ELSE 0 END AS hasQuantityUnit FROM Product p JOIN Category c ON p.categoryId = c.categoryId JOIN Supplier s ON p.supplierId = s.supplierId), SalesFeatures AS (SELECT bf.productId, bf.productName, bf.categoryName, COUNT(od.orderDetailId) AS totalOrderLines, SUM(od.quantity) AS totalQuantitySold, AVG(od.quantity) AS avgQuantityPerOrder, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue, AVG(od.unitPrice) AS avgSoldPrice, AVG(od.discount) AS avgDiscount, COUNT(DISTINCT so.custId) AS uniqueCustomers, COUNT(DISTINCT so.employeeId) AS uniqueEmployees FROM BaseFeatures bf LEFT JOIN OrderDetail od ON bf.productId = od.productId LEFT JOIN SalesOrder so ON od.orderId = so.orderId GROUP BY bf.productId, bf.productName, bf.categoryName), TimeFeatures AS (SELECT sf.productId, sf.totalRevenue, COALESCE(MIN(so.orderDate), '1900-01-01') AS firstSaleDate, COALESCE(MAX(so.orderDate), '1900-01-01') AS lastSaleDate, COUNT(DISTINCT DATE_FORMAT(so.orderDate, '%Y-%m')) AS monthsWithSales, SUM(CASE WHEN so.orderDate >= DATE_SUB(CURDATE(), INTERVAL 90 DAY) THEN od.quantity ELSE 0 END) AS sales90Days, SUM(CASE WHEN so.orderDate >= DATE_SUB(CURDATE(), INTERVAL 30 DAY) THEN od.quantity ELSE 0 END) AS sales30Days FROM SalesFeatures sf LEFT JOIN OrderDetail od ON sf.productId = od.productId LEFT JOIN SalesOrder so ON od.orderId = so.orderId GROUP BY sf.productId, sf.totalRevenue), CategoryFeatures AS (SELECT c.categoryId, c.categoryName, COUNT(p.productId) AS categoryProductCount, AVG(p.unitPrice) AS categoryAvgPrice, SUM(sf.totalRevenue) AS categoryTotalRevenue FROM Category c JOIN Product p ON c.categoryId = p.categoryId LEFT JOIN SalesFeatures sf ON p.productId = sf.productId GROUP BY c.categoryId, c.categoryName), MLFeatureSet AS (SELECT bf.productId, bf.productName, bf.categoryName, bf.unitPrice, bf.unitsInStock, bf.reorderLevel, bf.isDiscontinued, bf.nameLength, bf.hasQuantityUnit, COALESCE(sf.totalOrderLines, 0) AS totalOrderLines, COALESCE(sf.totalQuantitySold, 0) AS totalQuantitySold, COALESCE(sf.avgQuantityPerOrder, 0) AS avgQuantityPerOrder, COALESCE(sf.totalRevenue, 0) AS totalRevenue, COALESCE(sf.avgSoldPrice, bf.unitPrice) AS avgSoldPrice, COALESCE(sf.avgDiscount, 0) AS avgDiscount, COALESCE(sf.uniqueCustomers, 0) AS uniqueCustomers, COALESCE(tf.monthsWithSales, 0) AS monthsWithSales, COALESCE(tf.sales90Days, 0) AS sales90Days, COALESCE(tf.sales30Days, 0) AS sales30Days, cf.categoryProductCount, cf.categoryAvgPrice, cf.categoryTotalRevenue, bf.unitPrice / NULLIF(cf.categoryAvgPrice, 0) AS priceVsCategoryAvg, COALESCE(sf.totalRevenue, 0) / NULLIF(cf.categoryTotalRevenue, 0) * 100 AS categoryRevenueShare FROM BaseFeatures bf LEFT JOIN SalesFeatures sf ON bf.productId = sf.productId LEFT JOIN TimeFeatures tf ON bf.productId = tf.productId JOIN Product p ON bf.productId = p.productId JOIN CategoryFeatures cf ON p.categoryId = cf.categoryId) SELECT productName, categoryName, unitPrice, totalRevenue, sales30Days, sales90Days, uniqueCustomers, priceVsCategoryAvg, categoryRevenueShare, CASE WHEN totalRevenue > (SELECT AVG(totalRevenue) FROM MLFeatureSet) THEN 1 ELSE 0 END AS highPerformer FROM MLFeatureSet ORDER BY totalRevenue DESC;"
        },
        {
            "id": 73,
            "title": "Comprehensive Business Intelligence Dashboard Query",
            "statement": "Write a query to create a comprehensive BI dashboard with KPIs, trends, and actionable insights across all business dimensions.",
            "solution": "WITH SalesMetrics AS (SELECT COUNT(DISTINCT s.orderId) AS totalOrders, COUNT(DISTINCT s.custId) AS activeCustomers, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS totalRevenue, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avgOrderValue, SUM(od.quantity) AS totalUnitsSold FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)), ProductMetrics AS (SELECT COUNT(*) AS totalProducts, COUNT(CASE WHEN unitsInStock > 0 THEN 1 END) AS inStockProducts, COUNT(CASE WHEN discontinued = '1' THEN 1 END) AS discontinuedProducts, AVG(unitPrice) AS avgProductPrice FROM Product), CustomerMetrics AS (SELECT COUNT(*) AS totalCustomers, COUNT(DISTINCT country) AS countriesServed, AVG(orderCount) AS avgOrdersPerCustomer FROM (SELECT c.custId, COUNT(s.orderId) AS orderCount FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId) AS customerOrders), MonthlyTrends AS (SELECT DATE_FORMAT(s.orderDate, '%Y-%m') AS month, COUNT(s.orderId) AS monthlyOrders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS monthlyRevenue, COUNT(DISTINCT s.custId) AS monthlyActiveCustomers FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH) GROUP BY DATE_FORMAT(s.orderDate, '%Y-%m')), CategoryPerformance AS (SELECT c.categoryName, COUNT(p.productId) AS productCount, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS categoryRevenue, AVG(p.unitPrice) AS avgCategoryPrice, RANK() OVER (ORDER BY SUM(od.quantity * od.unitPrice * (1 - od.discount)) DESC) AS revenueRank FROM Category c JOIN Product p ON c.categoryId = p.categoryId LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY c.categoryId, c.categoryName), TopCustomers AS (SELECT c.companyName, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS customerRevenue, COUNT(s.orderId) AS customerOrders, RANK() OVER (ORDER BY SUM(od.quantity * od.unitPrice * (1 - od.discount)) DESC) AS customerRank FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId, c.companyName LIMIT 10), EmployeePerformance AS (SELECT CONCAT(e.firstname, ' ', e.lastname) AS employeeName, COUNT(s.orderId) AS ordersHandled, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS employeeRevenue, RANK() OVER (ORDER BY SUM(od.quantity * od.unitPrice * (1 - od.discount)) DESC) AS performanceRank FROM Employee e LEFT JOIN SalesOrder s ON e.employeeId = s.employeeId LEFT JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY e.employeeId, e.firstname, e.lastname), BusinessSummary AS (SELECT 'Sales Overview' AS section, CONCAT('Total Orders: ', sm.totalOrders, ', Revenue: , FORMAT(sm.totalRevenue, 2), ', AOV: , FORMAT(sm.avgOrderValue, 2)) AS summary FROM SalesMetrics sm UNION ALL SELECT 'Product Portfolio', CONCAT('Total Products: ', pm.totalProducts, ', In Stock: ', pm.inStockProducts, ', Avg Price: , FORMAT(pm.avgProductPrice, 2)) FROM ProductMetrics pm UNION ALL SELECT 'Customer Base', CONCAT('Total Customers: ', cm.totalCustomers, ', Countries: ', cm.countriesServed, ', Avg Orders: ', FORMAT(cm.avgOrdersPerCustomer, 1)) FROM CustomerMetrics cm) SELECT section, summary FROM BusinessSummary;"
        },
        {
            "id": 74,
            "title": "Real-time Anomaly Detection in Sales Patterns",
            "statement": "Write a query to detect anomalies in sales patterns using statistical methods and alert on unusual trends.",
            "solution": "WITH DailySalesData AS (SELECT DATE(s.orderDate) AS saleDate, COUNT(s.orderId) AS dailyOrderCount, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS dailyRevenue, COUNT(DISTINCT s.custId) AS dailyUniqueCustomers, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS dailyAvgOrderValue FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 180 DAY) GROUP BY DATE(s.orderDate)), StatisticalBaseline AS (SELECT AVG(dailyRevenue) AS avgDailyRevenue, STDDEV(dailyRevenue) AS stdDailyRevenue, AVG(dailyOrderCount) AS avgDailyOrders, STDDEV(dailyOrderCount) AS stdDailyOrders, AVG(dailyAvgOrderValue) AS avgOrderValue, STDDEV(dailyAvgOrderValue) AS stdOrderValue FROM DailySalesData), AnomalyDetection AS (SELECT dsd.saleDate, dsd.dailyRevenue, dsd.dailyOrderCount, dsd.dailyAvgOrderValue, sb.avgDailyRevenue, sb.stdDailyRevenue, sb.avgDailyOrders, sb.stdDailyOrders, (dsd.dailyRevenue - sb.avgDailyRevenue) / NULLIF(sb.stdDailyRevenue, 0) AS revenueZScore, (dsd.dailyOrderCount - sb.avgDailyOrders) / NULLIF(sb.stdDailyOrders, 0) AS orderCountZScore, (dsd.dailyAvgOrderValue - sb.avgOrderValue) / NULLIF(sb.stdOrderValue, 0) AS orderValueZScore FROM DailySalesData dsd CROSS JOIN StatisticalBaseline sb), AnomalyClassification AS (SELECT saleDate, dailyRevenue, dailyOrderCount, dailyAvgOrderValue, revenueZScore, orderCountZScore, orderValueZScore, CASE WHEN ABS(revenueZScore) > 2.5 OR ABS(orderCountZScore) > 2.5 OR ABS(orderValueZScore) > 2.5 THEN 'High Anomaly' WHEN ABS(revenueZScore) > 2.0 OR ABS(orderCountZScore) > 2.0 OR ABS(orderValueZScore) > 2.0 THEN 'Medium Anomaly' WHEN ABS(revenueZScore) > 1.5 OR ABS(orderCountZScore) > 1.5 OR ABS(orderValueZScore) > 1.5 THEN 'Low Anomaly' ELSE 'Normal' END AS anomalyLevel, CASE WHEN revenueZScore > 2.0 THEN 'Unusually High Revenue' WHEN revenueZScore < -2.0 THEN 'Unusually Low Revenue' WHEN orderCountZScore > 2.0 THEN 'Unusually High Order Volume' WHEN orderCountZScore < -2.0 THEN 'Unusually Low Order Volume' WHEN orderValueZScore > 2.0 THEN 'Unusually High Order Values' WHEN orderValueZScore < -2.0 THEN 'Unusually Low Order Values' ELSE 'Normal Pattern' END AS anomalyDescription FROM AnomalyDetection), RecentAnomalies AS (SELECT saleDate, anomalyLevel, anomalyDescription, dailyRevenue, revenueZScore FROM AnomalyClassification WHERE saleDate >= DATE_SUB(CURDATE(), INTERVAL 30 DAY) AND anomalyLevel != 'Normal') SELECT anomalyLevel, COUNT(*) AS anomalyCount, AVG(ABS(revenueZScore)) AS avgZScore, GROUP_CONCAT(DISTINCT anomalyDescription) AS alertTypes FROM RecentAnomalies GROUP BY anomalyLevel ORDER BY FIELD(anomalyLevel, 'High Anomaly', 'Medium Anomaly', 'Low Anomaly');"
        },
        {
            "id": 75,
            "title": "Integrated Supply Chain and Demand Planning Optimization",
            "statement": "Write a query for comprehensive supply chain optimization integrating demand forecasting, inventory planning, and supplier performance.",
            "solution": "WITH DemandForecast AS (SELECT p.productId, p.productName, SUM(CASE WHEN s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 90 DAY) THEN od.quantity ELSE 0 END) / 3 AS avgMonthlyDemand, SUM(CASE WHEN s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 30 DAY) THEN od.quantity ELSE 0 END) AS last30DayDemand, STDDEV(CASE WHEN s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 90 DAY) THEN od.quantity END) AS demandVariability FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId LEFT JOIN SalesOrder s ON od.orderId = s.orderId GROUP BY p.productId, p.productName), InventoryAnalysis AS (SELECT df.productId, df.productName, df.avgMonthlyDemand, df.demandVariability, p.unitsInStock, p.reorderLevel, p.unitPrice, CASE WHEN df.avgMonthlyDemand > 0 THEN p.unitsInStock / df.avgMonthlyDemand ELSE NULL END AS monthsOfInventory, CASE WHEN df.avgMonthlyDemand > 0 AND p.unitsInStock <= df.avgMonthlyDemand * 0.5 THEN 'Critical' WHEN df.avgMonthlyDemand > 0 AND p.unitsInStock <= df.avgMonthlyDemand THEN 'Low' WHEN p.unitsInStock > df.avgMonthlyDemand * 4 THEN 'Excess' ELSE 'Normal' END AS inventoryStatus FROM DemandForecast df JOIN Product p ON df.productId = p.productId), SupplierPerformance AS (SELECT s.supplierId, s.companyName AS supplierName, s.country, COUNT(p.productId) AS productsSupplied, AVG(ia.avgMonthlyDemand) AS avgSupplierDemand, SUM(ia.unitsInStock * p.unitPrice) AS supplierInventoryValue, COUNT(CASE WHEN ia.inventoryStatus = 'Critical' THEN 1 END) AS criticalProducts FROM Supplier s JOIN Product p ON s.supplierId = p.supplierId JOIN InventoryAnalysis ia ON p.productId = ia.productId GROUP BY s.supplierId, s.companyName, s.country), OptimizationRecommendations AS (SELECT ia.productId, ia.productName, ia.inventoryStatus, ia.monthsOfInventory, sp.supplierName, sp.country AS supplierCountry, CASE WHEN ia.inventoryStatus = 'Critical' THEN CEIL(ia.avgMonthlyDemand * 3 + ia.demandVariability * 1.65) WHEN ia.inventoryStatus = 'Low' THEN CEIL(ia.avgMonthlyDemand * 2) WHEN ia.inventoryStatus = 'Excess' THEN FLOOR(ia.avgMonthlyDemand * 1.5) ELSE ia.reorderLevel END AS recommendedReorderLevel, CASE WHEN ia.inventoryStatus = 'Critical' THEN 'Emergency Purchase Order' WHEN ia.inventoryStatus = 'Low' THEN 'Planned Reorder' WHEN ia.inventoryStatus = 'Excess' THEN 'Reduce Future Orders' ELSE 'Maintain Current Level' END AS action FROM InventoryAnalysis ia JOIN Product p ON ia.productId = p.productId JOIN SupplierPerformance sp ON p.supplierId = sp.supplierId), SupplyChainSummary AS (SELECT sp.supplierName, sp.country, sp.productsSupplied, sp.criticalProducts, sp.supplierInventoryValue, COUNT(or.productId) AS totalRecommendations, SUM(CASE WHEN or.action = 'Emergency Purchase Order' THEN 1 ELSE 0 END) AS urgentActions FROM SupplierPerformance sp LEFT JOIN Product p ON sp.supplierId = p.supplierId LEFT JOIN OptimizationRecommendations or ON p.productId = or.productId GROUP BY sp.supplierId, sp.supplierName, sp.country, sp.productsSupplied, sp.criticalProducts, sp.supplierInventoryValue) SELECT supplierName, country, productsSupplied, criticalProducts, FORMAT(supplierInventoryValue, 2) AS inventoryValue, totalRecommendations, urgentActions, CASE WHEN criticalProducts > productsSupplied * 0.5 THEN 'High Risk Supplier' WHEN urgentActions > 0 THEN 'Action Required' ELSE 'Stable' END AS supplierStatus FROM SupplyChainSummary ORDER BY urgentActions DESC, criticalProducts DESC;"
        }
    ]
}

# Create the complete problem set with remaining complex problems
remaining_complex = [
    {
        "id": 76,
        "title": "Multi-Variate Sales Correlation Analysis",
        "statement": "Write a query to perform correlation analysis between different sales variables and identify key relationships.",
        "solution": "-- Complex correlation analysis between sales variables\nWITH SalesVariables AS (\n  SELECT \n    p.productId, p.unitPrice, od.quantity, od.discount,\n    c.categoryId, s.orderDate,\n    (od.quantity * od.unitPrice * (1 - od.discount)) AS orderValue\n  FROM Product p\n  JOIN OrderDetail od ON p.productId = od.productId\n  JOIN SalesOrder s ON od.orderId = s.orderId\n  JOIN Category c ON p.categoryId = c.categoryId\n)\nSELECT \n  categoryId,\n  CORR(unitPrice, quantity) AS price_quantity_corr,\n  CORR(discount, orderValue) AS discount_value_corr,\n  COUNT(*) AS sample_size\nFROM SalesVariables\nGROUP BY categoryId;"
    },
    {
        "id": 77,
        "title": "Dynamic Product Bundling Recommendations",
        "statement": "Write a query to identify optimal product bundles based on purchase patterns and profit margins.",
        "solution": "-- Product bundling analysis with profitability scoring\nWITH ProductPairs AS (\n  SELECT \n    od1.productId AS product1,\n    od2.productId AS product2,\n    COUNT(*) AS frequency,\n    AVG(od1.unitPrice + od2.unitPrice) AS bundle_price\n  FROM OrderDetail od1\n  JOIN OrderDetail od2 ON od1.orderId = od2.orderId AND od1.productId < od2.productId\n  GROUP BY od1.productId, od2.productId\n  HAVING COUNT(*) >= 5\n)\nSELECT \n  p1.productName AS product1,\n  p2.productName AS product2,\n  pp.frequency,\n  pp.bundle_price,\n  RANK() OVER (ORDER BY pp.frequency DESC) AS bundle_rank\nFROM ProductPairs pp\nJOIN Product p1 ON pp.product1 = p1.productId\nJOIN Product p2 ON pp.product2 = p2.productId\nLIMIT 20;"
    },
    {
        "id": 78,
        "title": "Advanced Territory Performance Analytics",
        "statement": "Write a query for comprehensive territory analysis including market penetration and growth opportunities.",
        "solution": "-- Territory performance with market analysis\nWITH TerritoryMetrics AS (\n  SELECT \n    t.territoryId,\n    t.territorydescription,\n    COUNT(DISTINCT et.employeeId) AS employee_count,\n    COUNT(DISTINCT c.custId) AS customer_count,\n    SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS territory_revenue\n  FROM Territory t\n  LEFT JOIN EmployeeTerritory et ON t.territoryId = et.territoryId\n  LEFT JOIN SalesOrder s ON et.employeeId = s.employeeId\n  LEFT JOIN Customer c ON s.custId = c.custId\n  LEFT JOIN OrderDetail od ON s.orderId = od.orderId\n  GROUP BY t.territoryId, t.territorydescription\n)\nSELECT \n  territorydescription,\n  employee_count,\n  customer_count,\n  territory_revenue,\n  territory_revenue / NULLIF(employee_count, 0) AS revenue_per_employee,\n  CASE \n    WHEN territory_revenue > 10000 THEN 'High Performance'\n    WHEN territory_revenue > 5000 THEN 'Medium Performance'\n    ELSE 'Low Performance'\n  END AS performance_tier\nFROM TerritoryMetrics\nORDER BY territory_revenue DESC;"
    },
    {
        "id": 79,
        "title": "Customer Journey Attribution Modeling",
        "statement": "Write a query to track customer touchpoints and attribute revenue across the customer journey.",
        "solution": "WITH CustomerTouchpoints AS (SELECT c.custId, s.orderId, s.orderDate, e.employeeId, ROW_NUMBER() OVER (PARTITION BY c.custId ORDER BY s.orderDate) AS touchpoint_order, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS order_value FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId LEFT JOIN Employee e ON s.employeeId = e.employeeId GROUP BY c.custId, s.orderId, s.orderDate, e.employeeId), JourneyAttribution AS (SELECT custId, touchpoint_order, order_value, CASE WHEN touchpoint_order = 1 THEN order_value * 0.4 WHEN touchpoint_order = 2 THEN order_value * 0.3 WHEN touchpoint_order <= 5 THEN order_value * 0.2 ELSE order_value * 0.1 END AS attributed_value FROM CustomerTouchpoints) SELECT touchpoint_order, COUNT(*) AS touchpoint_count, AVG(order_value) AS avg_order_value, SUM(attributed_value) AS total_attributed_value FROM JourneyAttribution GROUP BY touchpoint_order ORDER BY touchpoint_order;"
    },
    {
        "id": 80,
        "title": "Comprehensive Data Quality Assessment",
        "statement": "Write a query to assess data quality across all tables and identify data integrity issues.",
        "solution": "WITH DataQualityChecks AS (SELECT 'Customer' AS table_name, 'Missing Phone' AS issue_type, COUNT(*) AS issue_count FROM Customer WHERE phone IS NULL OR phone = '' UNION ALL SELECT 'Customer', 'Missing Email', COUNT(*) FROM Customer WHERE email IS NULL OR email = '' UNION ALL SELECT 'Product', 'Zero Price', COUNT(*) FROM Product WHERE unitPrice = 0 OR unitPrice IS NULL UNION ALL SELECT 'Product', 'Negative Stock', COUNT(*) FROM Product WHERE unitsInStock < 0 UNION ALL SELECT 'OrderDetail', 'Invalid Discount', COUNT(*) FROM OrderDetail WHERE discount < 0 OR discount > 1 UNION ALL SELECT 'Employee', 'Missing Hire Date', COUNT(*) FROM Employee WHERE hireDate IS NULL), QualityScores AS (SELECT table_name, SUM(issue_count) AS total_issues, COUNT(*) AS total_checks FROM DataQualityChecks GROUP BY table_name) SELECT table_name, total_issues, total_checks, (total_checks - total_issues) / total_checks * 100 AS quality_score FROM QualityScores ORDER BY quality_score;"
    },
    {
        "id": 81,
        "title": "Advanced Seasonal Decomposition Analysis",
        "statement": "Write a query to decompose sales data into trend, seasonal, and residual components.",
        "solution": "WITH MonthlySales AS (SELECT DATE_FORMAT(s.orderDate, '%Y-%m') AS month, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS monthly_sales FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY DATE_FORMAT(s.orderDate, '%Y-%m')), TrendAnalysis AS (SELECT month, monthly_sales, AVG(monthly_sales) OVER (ORDER BY month ROWS BETWEEN 5 PRECEDING AND 5 FOLLOWING) AS trend FROM MonthlySales), SeasonalDecomposition AS (SELECT month, monthly_sales, trend, monthly_sales / NULLIF(trend, 0) AS seasonal_factor, monthly_sales - trend AS residual FROM TrendAnalysis) SELECT SUBSTRING(month, 6, 2) AS month_num, AVG(seasonal_factor) AS avg_seasonal_factor, STDDEV(residual) AS residual_variance FROM SeasonalDecomposition GROUP BY SUBSTRING(month, 6, 2) ORDER BY month_num;"
    },
    {
        "id": 82,
        "title": "Market Basket Optimization with Profit Margins",
        "statement": "Write a query to optimize market basket recommendations considering profit margins and inventory levels.",
        "solution": "WITH ProductProfitability AS (SELECT p.productId, p.productName, p.unitPrice, (p.unitPrice * 0.3) AS estimated_profit, p.unitsInStock FROM Product p), BasketAnalysis AS (SELECT od1.productId AS product1, od2.productId AS product2, COUNT(*) AS frequency, AVG(pp1.estimated_profit + pp2.estimated_profit) AS bundle_profit FROM OrderDetail od1 JOIN OrderDetail od2 ON od1.orderId = od2.orderId AND od1.productId < od2.productId JOIN ProductProfitability pp1 ON od1.productId = pp1.productId JOIN ProductProfitability pp2 ON od2.productId = pp2.productId GROUP BY od1.productId, od2.productId HAVING COUNT(*) >= 3), OptimizedBaskets AS (SELECT ba.product1, ba.product2, ba.frequency, ba.bundle_profit, (ba.frequency * ba.bundle_profit) AS optimization_score FROM BasketAnalysis ba JOIN ProductProfitability pp1 ON ba.product1 = pp1.productId JOIN ProductProfitability pp2 ON ba.product2 = pp2.productId WHERE pp1.unitsInStock > 5 AND pp2.unitsInStock > 5) SELECT p1.productName AS product1, p2.productName AS product2, frequency, bundle_profit, optimization_score FROM OptimizedBaskets ob JOIN Product p1 ON ob.product1 = p1.productId JOIN Product p2 ON ob.product2 = p2.productId ORDER BY optimization_score DESC LIMIT 15;"
    },
    {
        "id": 83,
        "title": "Customer Segmentation with Behavioral Clustering",
        "statement": "Write a query to perform advanced customer segmentation using multiple behavioral dimensions.",
        "solution": "WITH CustomerBehavior AS (SELECT c.custId, c.companyName, COUNT(DISTINCT s.orderId) AS order_frequency, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS total_spent, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avg_order_value, COUNT(DISTINCT p.categoryId) AS category_diversity, DATEDIFF(MAX(s.orderDate), MIN(s.orderDate)) AS customer_lifespan, MAX(s.orderDate) AS last_order_date FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId LEFT JOIN OrderDetail od ON s.orderId = od.orderId LEFT JOIN Product p ON od.productId = p.productId GROUP BY c.custId, c.companyName), BehavioralScores AS (SELECT custId, companyName, CASE WHEN order_frequency >= 10 THEN 5 WHEN order_frequency >= 5 THEN 4 WHEN order_frequency >= 3 THEN 3 WHEN order_frequency >= 1 THEN 2 ELSE 1 END AS frequency_score, CASE WHEN total_spent >= 5000 THEN 5 WHEN total_spent >= 2000 THEN 4 WHEN total_spent >= 1000 THEN 3 WHEN total_spent >= 500 THEN 2 ELSE 1 END AS monetary_score, CASE WHEN DATEDIFF(CURDATE(), last_order_date) <= 30 THEN 5 WHEN DATEDIFF(CURDATE(), last_order_date) <= 90 THEN 4 WHEN DATEDIFF(CURDATE(), last_order_date) <= 180 THEN 3 WHEN DATEDIFF(CURDATE(), last_order_date) <= 365 THEN 2 ELSE 1 END AS recency_score FROM CustomerBehavior WHERE last_order_date IS NOT NULL), CustomerClusters AS (SELECT custId, companyName, frequency_score, monetary_score, recency_score, (frequency_score + monetary_score + recency_score) AS total_score, CASE WHEN (frequency_score + monetary_score + recency_score) >= 13 THEN 'Champions' WHEN (frequency_score >= 3 AND monetary_score >= 3) THEN 'Loyal Customers' WHEN recency_score >= 4 THEN 'New Customers' WHEN (frequency_score <= 2 AND recency_score <= 2) THEN 'At Risk' ELSE 'Regular' END AS customer_segment FROM BehavioralScores) SELECT customer_segment, COUNT(*) AS customer_count, AVG(total_score) AS avg_score, AVG(frequency_score) AS avg_frequency, AVG(monetary_score) AS avg_monetary, AVG(recency_score) AS avg_recency FROM CustomerClusters GROUP BY customer_segment ORDER BY avg_score DESC;"
    },
    {
        "id": 84,
        "title": "Predictive Inventory Management with Safety Stock",
        "statement": "Write a query to calculate optimal inventory levels with safety stock considering demand variability.",
        "solution": "WITH DemandHistory AS (SELECT p.productId, p.productName, DATE_FORMAT(s.orderDate, '%Y-%m') AS month, SUM(od.quantity) AS monthly_demand FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId LEFT JOIN SalesOrder s ON od.orderId = s.orderId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH) GROUP BY p.productId, p.productName, DATE_FORMAT(s.orderDate, '%Y-%m')), DemandStatistics AS (SELECT productId, productName, AVG(monthly_demand) AS avg_demand, STDDEV(monthly_demand) AS demand_stddev, COUNT(*) AS months_with_data FROM DemandHistory WHERE monthly_demand > 0 GROUP BY productId, productName HAVING COUNT(*) >= 3), SafetyStockCalculation AS (SELECT ds.productId, ds.productName, ds.avg_demand, ds.demand_stddev, p.unitsInStock, p.reorderLevel, CEIL(ds.avg_demand + 1.65 * ds.demand_stddev) AS safety_stock, CEIL(ds.avg_demand * 2 + 1.65 * ds.demand_stddev) AS optimal_reorder_point, CEIL(ds.avg_demand * 3 + 2 * ds.demand_stddev) AS max_stock_level FROM DemandStatistics ds JOIN Product p ON ds.productId = p.productId), InventoryRecommendations AS (SELECT productName, unitsInStock, current_reorder_level = reorderLevel, optimal_reorder_point, safety_stock, max_stock_level, CASE WHEN unitsInStock < safety_stock THEN 'Critical - Immediate Reorder' WHEN unitsInStock < optimal_reorder_point THEN 'Low - Schedule Reorder' WHEN unitsInStock > max_stock_level THEN 'Excess - Reduce Orders' ELSE 'Optimal' END AS inventory_status FROM SafetyStockCalculation) SELECT inventory_status, COUNT(*) AS product_count, AVG(unitsInStock) AS avg_current_stock, AVG(optimal_reorder_point) AS avg_optimal_reorder FROM InventoryRecommendations GROUP BY inventory_status ORDER BY FIELD(inventory_status, 'Critical - Immediate Reorder', 'Low - Schedule Reorder', 'Optimal', 'Excess - Reduce Orders');"
    },
    {
        "id": 85,
        "title": "Multi-dimensional Profitability Analysis",
        "statement": "Write a query to analyze profitability across multiple dimensions: product, customer, territory, and time.",
        "solution": "WITH ProfitabilityMetrics AS (SELECT p.productId, p.productName, c.categoryName, cust.custId, cust.companyName AS customer_name, cust.country, YEAR(s.orderDate) AS year, QUARTER(s.orderDate) AS quarter, od.quantity, od.unitPrice, od.discount, (od.quantity * od.unitPrice * (1 - od.discount)) AS revenue, (od.quantity * od.unitPrice * 0.3) AS estimated_cost, (od.quantity * od.unitPrice * (1 - od.discount) - od.quantity * od.unitPrice * 0.3) AS estimated_profit FROM Product p JOIN OrderDetail od ON p.productId = od.productId JOIN SalesOrder s ON od.orderId = s.orderId JOIN Customer cust ON s.custId = cust.custId JOIN Category c ON p.categoryId = c.categoryId), DimensionalProfitability AS (SELECT categoryName, customer_name, country, year, quarter, SUM(revenue) AS total_revenue, SUM(estimated_profit) AS total_profit, AVG(estimated_profit / NULLIF(revenue, 0)) AS profit_margin, COUNT(DISTINCT productId) AS unique_products FROM ProfitabilityMetrics GROUP BY categoryName, customer_name, country, year, quarter), ProfitabilityRanking AS (SELECT categoryName, customer_name, country, total_revenue, total_profit, profit_margin, unique_products, RANK() OVER (PARTITION BY categoryName ORDER BY total_profit DESC) AS profit_rank_in_category, RANK() OVER (ORDER BY total_profit DESC) AS overall_profit_rank FROM DimensionalProfitability WHERE year = YEAR(CURDATE()) - 1) SELECT categoryName, customer_name, country, FORMAT(total_revenue, 2) AS revenue, FORMAT(total_profit, 2) AS profit, ROUND(profit_margin * 100, 2) AS profit_margin_pct, profit_rank_in_category, overall_profit_rank FROM ProfitabilityRanking WHERE overall_profit_rank <= 50 ORDER BY overall_profit_rank;"
    },
    {
        "id": 86,
        "title": "Advanced Sales Forecasting with Multiple Models",
        "statement": "Write a query to implement multiple forecasting models and compare their accuracy for sales prediction.",
        "solution": "WITH HistoricalData AS (SELECT DATE_FORMAT(s.orderDate, '%Y-%m') AS month, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS monthly_sales, ROW_NUMBER() OVER (ORDER BY DATE_FORMAT(s.orderDate, '%Y-%m')) AS time_index FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 24 MONTH) GROUP BY DATE_FORMAT(s.orderDate, '%Y-%m')), MovingAverage AS (SELECT month, monthly_sales, time_index, AVG(monthly_sales) OVER (ORDER BY time_index ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS ma3_forecast, AVG(monthly_sales) OVER (ORDER BY time_index ROWS BETWEEN 5 PRECEDING AND CURRENT ROW) AS ma6_forecast FROM HistoricalData), LinearTrend AS (SELECT month, monthly_sales, time_index, (SELECT (COUNT(*) * SUM(time_index * monthly_sales) - SUM(time_index) * SUM(monthly_sales)) / (COUNT(*) * SUM(time_index * time_index) - SUM(time_index) * SUM(time_index))) * time_index + (SELECT (SUM(monthly_sales) - (COUNT(*) * SUM(time_index * monthly_sales) - SUM(time_index) * SUM(monthly_sales)) / (COUNT(*) * SUM(time_index * time_index) - SUM(time_index) * SUM(time_index)) * SUM(time_index)) / COUNT(*)) AS linear_forecast FROM HistoricalData), ForecastAccuracy AS (SELECT hd.month, hd.monthly_sales AS actual, ma.ma3_forecast, ma.ma6_forecast, lt.linear_forecast, ABS(hd.monthly_sales - ma.ma3_forecast) / NULLIF(hd.monthly_sales, 0) * 100 AS ma3_error, ABS(hd.monthly_sales - ma.ma6_forecast) / NULLIF(hd.monthly_sales, 0) * 100 AS ma6_error, ABS(hd.monthly_sales - lt.linear_forecast) / NULLIF(hd.monthly_sales, 0) * 100 AS linear_error FROM HistoricalData hd JOIN MovingAverage ma ON hd.month = ma.month JOIN LinearTrend lt ON hd.month = lt.month WHERE ma.ma6_forecast IS NOT NULL) SELECT 'Moving Average 3' AS model, AVG(ma3_error) AS avg_error, STDDEV(ma3_error) AS error_stddev FROM ForecastAccuracy UNION ALL SELECT 'Moving Average 6', AVG(ma6_error), STDDEV(ma6_error) FROM ForecastAccuracy UNION ALL SELECT 'Linear Trend', AVG(linear_error), STDDEV(linear_error) FROM ForecastAccuracy ORDER BY avg_error;"
    },
    {
        "id": 87,
        "title": "Customer Value Migration Analysis",
        "statement": "Write a query to analyze how customer value changes over time and identify migration patterns.",
        "solution": "WITH CustomerValueHistory AS (SELECT c.custId, c.companyName, YEAR(s.orderDate) AS year, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS annual_value, COUNT(s.orderId) AS annual_orders FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId, c.companyName, YEAR(s.orderDate)), ValueSegmentation AS (SELECT custId, companyName, year, annual_value, annual_orders, CASE WHEN annual_value >= 5000 THEN 'High Value' WHEN annual_value >= 2000 THEN 'Medium Value' WHEN annual_value >= 500 THEN 'Low Value' ELSE 'Minimal Value' END AS value_segment FROM CustomerValueHistory), ValueMigration AS (SELECT cvh1.custId, cvh1.companyName, cvh1.year AS year1, cvh2.year AS year2, vs1.value_segment AS segment1, vs2.value_segment AS segment2, cvh1.annual_value AS value1, cvh2.annual_value AS value2 FROM CustomerValueHistory cvh1 JOIN CustomerValueHistory cvh2 ON cvh1.custId = cvh2.custId AND cvh2.year = cvh1.year + 1 JOIN ValueSegmentation vs1 ON cvh1.custId = vs1.custId AND cvh1.year = vs1.year JOIN ValueSegmentation vs2 ON cvh2.custId = vs2.custId AND cvh2.year = vs2.year), MigrationPatterns AS (SELECT segment1, segment2, COUNT(*) AS migration_count, AVG(value2 - value1) AS avg_value_change, AVG((value2 - value1) / NULLIF(value1, 0) * 100) AS avg_percent_change FROM ValueMigration GROUP BY segment1, segment2), MigrationMatrix AS (SELECT segment1, segment2, migration_count, avg_value_change, avg_percent_change, CASE WHEN segment1 = segment2 THEN 'Retained' WHEN (segment1 = 'Low Value' AND segment2 IN ('Medium Value', 'High Value')) OR (segment1 = 'Medium Value' AND segment2 = 'High Value') THEN 'Upgraded' WHEN (segment1 = 'High Value' AND segment2 IN ('Medium Value', 'Low Value')) OR (segment1 = 'Medium Value' AND segment2 = 'Low Value') THEN 'Downgraded' ELSE 'Other' END AS migration_type FROM MigrationPatterns) SELECT migration_type, segment1, segment2, migration_count, ROUND(avg_value_change, 2) AS avg_value_change, ROUND(avg_percent_change, 2) AS avg_percent_change FROM MigrationMatrix ORDER BY migration_type, migration_count DESC;"
    },
    {
        "id": 88,
        "title": "Comprehensive Competitor Analysis Framework",
        "statement": "Write a query to analyze competitive positioning using price comparisons, market share, and customer overlap.",
        "solution": "WITH ProductCompetitiveAnalysis AS (SELECT p.productId, p.productName, c.categoryName, p.unitPrice, AVG(p2.unitPrice) AS category_avg_price, COUNT(p2.productId) AS category_product_count, RANK() OVER (PARTITION BY p.categoryId ORDER BY p.unitPrice) AS price_rank_in_category FROM Product p JOIN Category c ON p.categoryId = c.categoryId JOIN Product p2 ON c.categoryId = p2.categoryId GROUP BY p.productId, p.productName, c.categoryName, p.unitPrice), MarketShareAnalysis AS (SELECT p.productId, p.productName, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS product_revenue, SUM(SUM(od.quantity * od.unitPrice * (1 - od.discount))) OVER (PARTITION BY p.categoryId) AS category_total_revenue, SUM(od.quantity) AS units_sold FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName), CompetitivePositioning AS (SELECT pca.productId, pca.productName, pca.categoryName, pca.unitPrice, pca.category_avg_price, pca.price_rank_in_category, msa.product_revenue, msa.category_total_revenue, (msa.product_revenue / NULLIF(msa.category_total_revenue, 0) * 100) AS market_share_pct, CASE WHEN pca.unitPrice > pca.category_avg_price * 1.2 THEN 'Premium Pricing' WHEN pca.unitPrice < pca.category_avg_price * 0.8 THEN 'Value Pricing' ELSE 'Competitive Pricing' END AS pricing_strategy, CASE WHEN (msa.product_revenue / NULLIF(msa.category_total_revenue, 0) * 100) > 20 THEN 'Market Leader' WHEN (msa.product_revenue / NULLIF(msa.category_total_revenue, 0) * 100) > 10 THEN 'Strong Player' WHEN (msa.product_revenue / NULLIF(msa.category_total_revenue, 0) * 100) > 5 THEN 'Moderate Player' ELSE 'Niche Player' END AS market_position FROM ProductCompetitiveAnalysis pca LEFT JOIN MarketShareAnalysis msa ON pca.productId = msa.productId) SELECT categoryName, pricing_strategy, market_position, COUNT(*) AS product_count, AVG(market_share_pct) AS avg_market_share, AVG(unitPrice) AS avg_price FROM CompetitivePositioning GROUP BY categoryName, pricing_strategy, market_position ORDER BY categoryName, avg_market_share DESC;"
    },
    {
        "id": 89,
        "title": "Real-time Business Performance Dashboard",
        "statement": "Write a query to create a comprehensive real-time dashboard with key performance indicators and alerts.",
        "solution": "WITH RealTimeMetrics AS (SELECT COUNT(DISTINCT s.orderId) AS orders_today, COUNT(DISTINCT s.custId) AS active_customers_today, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS revenue_today, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avg_order_value_today FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE DATE(s.orderDate) = CURDATE()), HistoricalComparison AS (SELECT AVG(daily_orders) AS avg_daily_orders, AVG(daily_revenue) AS avg_daily_revenue, STDDEV(daily_orders) AS stddev_daily_orders, STDDEV(daily_revenue) AS stddev_daily_revenue FROM (SELECT DATE(s.orderDate) AS order_date, COUNT(s.orderId) AS daily_orders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS daily_revenue FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 30 DAY) AND DATE(s.orderDate) < CURDATE() GROUP BY DATE(s.orderDate)) AS daily_stats), PerformanceAlerts AS (SELECT rtm.orders_today, rtm.revenue_today, hc.avg_daily_orders, hc.avg_daily_revenue, hc.stddev_daily_orders, hc.stddev_daily_revenue, CASE WHEN rtm.orders_today < (hc.avg_daily_orders - 2 * hc.stddev_daily_orders) THEN 'Low Order Volume Alert' WHEN rtm.orders_today > (hc.avg_daily_orders + 2 * hc.stddev_daily_orders) THEN 'High Order Volume Alert' ELSE 'Normal Order Volume' END AS order_alert, CASE WHEN rtm.revenue_today < (hc.avg_daily_revenue - 2 * hc.stddev_daily_revenue) THEN 'Low Revenue Alert' WHEN rtm.revenue_today > (hc.avg_daily_revenue + 2 * hc.stddev_daily_revenue) THEN 'High Revenue Alert' ELSE 'Normal Revenue' END AS revenue_alert FROM RealTimeMetrics rtm CROSS JOIN HistoricalComparison hc), InventoryAlerts AS (SELECT COUNT(*) AS low_stock_products FROM Product WHERE unitsInStock <= reorderLevel AND discontinued = '0'), CustomerAlerts AS (SELECT COUNT(*) AS at_risk_customers FROM (SELECT c.custId FROM Customer c JOIN SalesOrder s ON c.custId = s.custId GROUP BY c.custId HAVING MAX(s.orderDate) < DATE_SUB(CURDATE(), INTERVAL 90 DAY)) AS at_risk), DashboardSummary AS (SELECT 'Performance' AS metric_category, CONCAT('Orders: ', pa.orders_today, ' (', pa.order_alert, '), Revenue: , FORMAT(pa.revenue_today, 2), ' (', pa.revenue_alert, ')') AS metric_value FROM PerformanceAlerts pa UNION ALL SELECT 'Inventory', CONCAT('Low Stock Products: ', ia.low_stock_products) FROM InventoryAlerts ia UNION ALL SELECT 'Customer Risk', CONCAT('At Risk Customers: ', ca.at_risk_customers) FROM CustomerAlerts ca) SELECT metric_category, metric_value FROM DashboardSummary;"
    },
    {
        "id": 90,
        "title": "Advanced Financial Analysis and Forecasting",
        "statement": "Write a query to perform comprehensive financial analysis including cash flow projections and profitability forecasting.",
        "solution": "WITH MonthlyFinancials AS (SELECT DATE_FORMAT(s.orderDate, '%Y-%m') AS month, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS gross_revenue, SUM(od.quantity * od.unitPrice * 0.4) AS estimated_cogs, SUM(s.freight) AS shipping_costs, COUNT(DISTINCT s.orderId) AS order_count, COUNT(DISTINCT s.custId) AS customer_count FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 24 MONTH) GROUP BY DATE_FORMAT(s.orderDate, '%Y-%m')), ProfitabilityAnalysis AS (SELECT month, gross_revenue, estimated_cogs, shipping_costs, (gross_revenue - estimated_cogs - shipping_costs) AS net_profit, (gross_revenue - estimated_cogs - shipping_costs) / NULLIF(gross_revenue, 0) * 100 AS profit_margin_pct, order_count, customer_count, gross_revenue / NULLIF(customer_count, 0) AS revenue_per_customer FROM MonthlyFinancials), TrendAnalysis AS (SELECT month, net_profit, profit_margin_pct, revenue_per_customer, LAG(net_profit, 12) OVER (ORDER BY month) AS profit_12m_ago, LAG(profit_margin_pct, 12) OVER (ORDER BY month) AS margin_12m_ago, AVG(net_profit) OVER (ORDER BY month ROWS BETWEEN 11 PRECEDING AND CURRENT ROW) AS profit_12m_avg FROM ProfitabilityAnalysis), FinancialProjections AS (SELECT month, net_profit, profit_margin_pct, profit_12m_avg, CASE WHEN profit_12m_ago IS NOT NULL THEN ((net_profit - profit_12m_ago) / NULLIF(profit_12m_ago, 0) * 100) ELSE NULL END AS yoy_profit_growth, profit_12m_avg * 1.05 AS conservative_forecast, profit_12m_avg * 1.15 AS optimistic_forecast FROM TrendAnalysis WHERE month >= DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 12 MONTH), '%Y-%m')), CashFlowProjection AS (SELECT 'Current Month' AS period, AVG(net_profit) AS projected_cash_flow FROM FinancialProjections WHERE month = DATE_FORMAT(CURDATE(), '%Y-%m') UNION ALL SELECT 'Next 3 Months', AVG(conservative_forecast) * 3 FROM FinancialProjections WHERE month >= DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 3 MONTH), '%Y-%m') UNION ALL SELECT 'Next 6 Months', AVG(optimistic_forecast) * 6 FROM FinancialProjections WHERE month >= DATE_FORMAT(DATE_SUB(CURDATE(), INTERVAL 6 MONTH), '%Y-%m')) SELECT period, FORMAT(projected_cash_flow, 2) AS projected_cash_flow FROM CashFlowProjection;"
    }
]

# Add the remaining problems to complete the 100 problems set
for problem in remaining_complex:
    problems["complex"].append(problem)

# Add the final 10 problems to reach 100
final_problems = [
    {
        "id": 91,
        "title": "Enterprise Resource Planning Integration",
        "statement": "Write a query to simulate ERP integration by creating a comprehensive resource allocation and planning analysis.",
        "solution": "WITH ResourceAllocation AS (SELECT e.employeeId, CONCAT(e.firstname, ' ', e.lastname) AS employee_name, COUNT(s.orderId) AS orders_handled, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS revenue_generated, COUNT(DISTINCT s.custId) AS customers_served FROM Employee e LEFT JOIN SalesOrder s ON e.employeeId = s.employeeId LEFT JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY e.employeeId, e.firstname, e.lastname), CapacityAnalysis AS (SELECT ra.employee_name, ra.orders_handled, ra.revenue_generated, ra.customers_served, ra.revenue_generated / NULLIF(ra.orders_handled, 0) AS revenue_per_order FROM ResourceAllocation ra) SELECT employee_name, orders_handled, revenue_generated, revenue_per_order, CASE WHEN orders_handled > 50 THEN 'High Capacity' WHEN orders_handled > 20 THEN 'Medium Capacity' ELSE 'Low Capacity' END AS capacity_level FROM CapacityAnalysis ORDER BY revenue_generated DESC;"
    },
    {
        "id": 92,
        "title": "Advanced Data Mining for Sales Patterns",
        "statement": "Write a query to discover hidden sales patterns using association rules and sequential pattern mining.",
        "solution": "WITH ProductSequences AS (SELECT c.custId, s.orderDate, p.productId, p.productName, ROW_NUMBER() OVER (PARTITION BY c.custId ORDER BY s.orderDate) AS purchase_sequence FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId JOIN Product p ON od.productId = p.productId), SequentialPatterns AS (SELECT ps1.productId AS first_product, ps2.productId AS second_product, ps1.productName AS first_name, ps2.productName AS second_name, COUNT(*) AS pattern_frequency FROM ProductSequences ps1 JOIN ProductSequences ps2 ON ps1.custId = ps2.custId AND ps2.purchase_sequence = ps1.purchase_sequence + 1 GROUP BY ps1.productId, ps2.productId, ps1.productName, ps2.productName HAVING COUNT(*) >= 3) SELECT first_name, second_name, pattern_frequency, RANK() OVER (ORDER BY pattern_frequency DESC) AS pattern_rank FROM SequentialPatterns ORDER BY pattern_frequency DESC LIMIT 20;"
    },
    {
        "id": 93,
        "title": "Complex Supply Chain Network Analysis",
        "statement": "Write a query to analyze the entire supply chain network including supplier dependencies and risk assessment.",
        "solution": "WITH SupplyChainNetwork AS (SELECT s.supplierId, s.companyName AS supplier_name, s.country AS supplier_country, COUNT(p.productId) AS products_supplied, COUNT(DISTINCT p.categoryId) AS categories_served, SUM(p.unitsInStock * p.unitPrice) AS inventory_value FROM Supplier s LEFT JOIN Product p ON s.supplierId = p.supplierId GROUP BY s.supplierId, s.companyName, s.country), NetworkDependencies AS (SELECT supplier_country, COUNT(*) AS supplier_count, SUM(products_supplied) AS total_products, AVG(inventory_value) AS avg_inventory_value, CASE WHEN COUNT(*) = 1 THEN 'High Risk - Single Supplier' WHEN COUNT(*) <= 3 THEN 'Medium Risk - Few Suppliers' ELSE 'Low Risk - Multiple Suppliers' END AS dependency_risk FROM SupplyChainNetwork GROUP BY supplier_country), RiskMatrix AS (SELECT scn.supplier_name, scn.supplier_country, scn.products_supplied, scn.inventory_value, nd.dependency_risk, CASE WHEN scn.products_supplied > 10 AND nd.dependency_risk LIKE 'High Risk%' THEN 'Critical' WHEN scn.products_supplied > 5 OR nd.dependency_risk LIKE 'Medium Risk%' THEN 'Moderate' ELSE 'Low' END AS overall_risk FROM SupplyChainNetwork scn JOIN NetworkDependencies nd ON scn.supplier_country = nd.supplier_country) SELECT overall_risk, COUNT(*) AS supplier_count, AVG(products_supplied) AS avg_products, AVG(inventory_value) AS avg_inventory FROM RiskMatrix GROUP BY overall_risk ORDER BY FIELD(overall_risk, 'Critical', 'Moderate', 'Low');"
    },
    {
        "id": 94,
        "title": "Comprehensive Customer Experience Analytics",
        "statement": "Write a query to analyze customer experience across all touchpoints and calculate satisfaction scores.",
        "solution": "WITH CustomerTouchpoints AS (SELECT c.custId, c.companyName, COUNT(s.orderId) AS total_orders, AVG(DATEDIFF(s.shippedDate, s.orderDate)) AS avg_shipping_time, COUNT(CASE WHEN s.shippedDate > s.requiredDate THEN 1 END) AS late_deliveries, AVG(od.discount) AS avg_discount_received, COUNT(DISTINCT e.employeeId) AS employees_interacted FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId LEFT JOIN Employee e ON s.employeeId = e.employeeId GROUP BY c.custId, c.companyName), ExperienceScoring AS (SELECT custId, companyName, total_orders, avg_shipping_time, late_deliveries, avg_discount_received, employees_interacted, CASE WHEN avg_shipping_time <= 3 THEN 5 WHEN avg_shipping_time <= 7 THEN 4 WHEN avg_shipping_time <= 10 THEN 3 ELSE 2 END AS shipping_score, CASE WHEN late_deliveries = 0 THEN 5 WHEN late_deliveries / total_orders < 0.1 THEN 4 WHEN late_deliveries / total_orders < 0.2 THEN 3 ELSE 2 END AS delivery_score, CASE WHEN avg_discount_received > 0.1 THEN 5 WHEN avg_discount_received > 0.05 THEN 4 ELSE 3 END AS discount_score FROM CustomerTouchpoints), CustomerSatisfaction AS (SELECT custId, companyName, total_orders, (shipping_score + delivery_score + discount_score) / 3 AS satisfaction_score, CASE WHEN (shipping_score + delivery_score + discount_score) / 3 >= 4.5 THEN 'Highly Satisfied' WHEN (shipping_score + delivery_score + discount_score) / 3 >= 3.5 THEN 'Satisfied' WHEN (shipping_score + delivery_score + discount_score) / 3 >= 2.5 THEN 'Neutral' ELSE 'Dissatisfied' END AS satisfaction_level FROM ExperienceScoring) SELECT satisfaction_level, COUNT(*) AS customer_count, AVG(satisfaction_score) AS avg_score, AVG(total_orders) AS avg_orders FROM CustomerSatisfaction GROUP BY satisfaction_level ORDER BY avg_score DESC;"
    },
    {
        "id": 95,
        "title": "Machine Learning Feature Engineering for Churn Prediction",
        "statement": "Write a query to create comprehensive features for machine learning models to predict customer churn.",
        "solution": "WITH CustomerFeatures AS (SELECT c.custId, c.companyName, COUNT(s.orderId) AS total_orders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS total_spent, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avg_order_value, MIN(s.orderDate) AS first_order_date, MAX(s.orderDate) AS last_order_date, DATEDIFF(CURDATE(), MAX(s.orderDate)) AS days_since_last_order, COUNT(DISTINCT p.categoryId) AS categories_purchased, AVG(DATEDIFF(s.shippedDate, s.orderDate)) AS avg_shipping_time, COUNT(CASE WHEN s.shippedDate > s.requiredDate THEN 1 END) AS late_deliveries FROM Customer c LEFT JOIN SalesOrder s ON c.custId = s.custId LEFT JOIN OrderDetail od ON s.orderId = od.orderId LEFT JOIN Product p ON od.productId = p.productId GROUP BY c.custId, c.companyName), ChurnFeatures AS (SELECT custId, companyName, total_orders, total_spent, avg_order_value, days_since_last_order, categories_purchased, avg_shipping_time, late_deliveries, DATEDIFF(last_order_date, first_order_date) AS customer_lifetime_days, total_orders / GREATEST(DATEDIFF(last_order_date, first_order_date), 1) * 365 AS orders_per_year, CASE WHEN days_since_last_order > 180 THEN 1 ELSE 0 END AS likely_churned FROM CustomerFeatures WHERE total_orders > 0), MLDataset AS (SELECT custId, total_orders, total_spent, avg_order_value, days_since_last_order, categories_purchased, avg_shipping_time, late_deliveries, customer_lifetime_days, orders_per_year, likely_churned, CASE WHEN total_spent > 5000 THEN 1 ELSE 0 END AS high_value, CASE WHEN orders_per_year > 12 THEN 1 ELSE 0 END AS frequent_buyer, CASE WHEN late_deliveries > 0 THEN 1 ELSE 0 END AS had_delivery_issues FROM ChurnFeatures) SELECT likely_churned, COUNT(*) AS customer_count, AVG(total_spent) AS avg_spent, AVG(orders_per_year) AS avg_frequency, AVG(days_since_last_order) AS avg_days_since_order FROM MLDataset GROUP BY likely_churned;"
    },
    {
        "id": 96,
        "title": "Advanced Financial Risk Assessment",
        "statement": "Write a query to assess financial risks including credit risk, operational risk, and market risk.",
        "solution": "WITH CustomerCreditRisk AS (SELECT c.custId, c.companyName, COUNT(s.orderId) AS order_count, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS total_credit, AVG(DATEDIFF(s.shippedDate, s.orderDate)) AS avg_payment_delay, COUNT(CASE WHEN s.shippedDate > s.requiredDate THEN 1 END) AS payment_delays, MAX(s.orderDate) AS last_transaction FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY c.custId, c.companyName), OperationalRisk AS (SELECT p.productId, p.productName, p.unitsInStock, SUM(od.quantity) AS total_demand, p.unitsInStock - SUM(od.quantity) AS stock_buffer, CASE WHEN p.unitsInStock < SUM(od.quantity) * 0.1 THEN 'High Risk' WHEN p.unitsInStock < SUM(od.quantity) * 0.5 THEN 'Medium Risk' ELSE 'Low Risk' END AS stockout_risk FROM Product p LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY p.productId, p.productName, p.unitsInStock), MarketRisk AS (SELECT c.categoryName, COUNT(p.productId) AS product_count, AVG(p.unitPrice) AS avg_price, STDDEV(p.unitPrice) AS price_volatility, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS category_revenue FROM Category c JOIN Product p ON c.categoryId = p.categoryId LEFT JOIN OrderDetail od ON p.productId = od.productId GROUP BY c.categoryId, c.categoryName), RiskAssessment AS (SELECT 'Credit Risk' AS risk_type, COUNT(CASE WHEN payment_delays > order_count * 0.2 THEN 1 END) AS high_risk_count, COUNT(*) AS total_entities FROM CustomerCreditRisk UNION ALL SELECT 'Operational Risk', COUNT(CASE WHEN stockout_risk = 'High Risk' THEN 1 END), COUNT(*) FROM OperationalRisk UNION ALL SELECT 'Market Risk', COUNT(CASE WHEN price_volatility > avg_price * 0.3 THEN 1 END), COUNT(*) FROM MarketRisk) SELECT risk_type, high_risk_count, total_entities, (high_risk_count * 100.0 / total_entities) AS risk_percentage FROM RiskAssessment;"
    },
    {
        "id": 97,
        "title": "Comprehensive Business Intelligence Reporting",
        "statement": "Write a query to create a comprehensive BI report with executive summary, trends, and recommendations.",
        "solution": "WITH ExecutiveSummary AS (SELECT COUNT(DISTINCT c.custId) AS total_customers, COUNT(DISTINCT s.orderId) AS total_orders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS total_revenue, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avg_order_value, COUNT(DISTINCT p.productId) AS active_products FROM Customer c JOIN SalesOrder s ON c.custId = s.custId JOIN OrderDetail od ON s.orderId = od.orderId JOIN Product p ON od.productId = p.productId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)), TrendAnalysis AS (SELECT DATE_FORMAT(s.orderDate, '%Y-%m') AS month, COUNT(s.orderId) AS monthly_orders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS monthly_revenue, LAG(COUNT(s.orderId)) OVER (ORDER BY DATE_FORMAT(s.orderDate, '%Y-%m')) AS prev_month_orders, LAG(SUM(od.quantity * od.unitPrice * (1 - od.discount))) OVER (ORDER BY DATE_FORMAT(s.orderDate, '%Y-%m')) AS prev_month_revenue FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH) GROUP BY DATE_FORMAT(s.orderDate, '%Y-%m')), PerformanceMetrics AS (SELECT ta.month, ta.monthly_orders, ta.monthly_revenue, CASE WHEN prev_month_orders IS NOT NULL THEN ((monthly_orders - prev_month_orders) / prev_month_orders * 100) ELSE NULL END AS order_growth, CASE WHEN prev_month_revenue IS NOT NULL THEN ((monthly_revenue - prev_month_revenue) / prev_month_revenue * 100) ELSE NULL END AS revenue_growth FROM TrendAnalysis ta), BusinessRecommendations AS (SELECT CASE WHEN AVG(order_growth) > 10 THEN 'Strong Growth - Scale Operations' WHEN AVG(order_growth) > 0 THEN 'Moderate Growth - Optimize Processes' WHEN AVG(order_growth) > -5 THEN 'Stable - Focus on Efficiency' ELSE 'Declining - Urgent Action Required' END AS growth_recommendation, CASE WHEN AVG(revenue_growth) > AVG(order_growth) THEN 'Pricing Strategy Working' ELSE 'Review Pricing Strategy' END AS pricing_recommendation FROM PerformanceMetrics WHERE order_growth IS NOT NULL) SELECT es.total_customers, es.total_orders, FORMAT(es.total_revenue, 2) AS total_revenue, FORMAT(es.avg_order_value, 2) AS avg_order_value, br.growth_recommendation, br.pricing_recommendation FROM ExecutiveSummary es CROSS JOIN BusinessRecommendations br;"
    },
    {
        "id": 98,
        "title": "Advanced Predictive Analytics for Strategic Planning",
        "statement": "Write a query to implement predictive models for strategic business planning and scenario analysis.",
        "solution": "WITH HistoricalGrowth AS (SELECT YEAR(s.orderDate) AS year, COUNT(s.orderId) AS annual_orders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS annual_revenue, COUNT(DISTINCT s.custId) AS annual_customers FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId GROUP BY YEAR(s.orderDate)), GrowthRates AS (SELECT year, annual_orders, annual_revenue, annual_customers, LAG(annual_revenue) OVER (ORDER BY year) AS prev_year_revenue, (annual_revenue - LAG(annual_revenue) OVER (ORDER BY year)) / LAG(annual_revenue) OVER (ORDER BY year) * 100 AS revenue_growth_rate FROM HistoricalGrowth), PredictiveModeling AS (SELECT AVG(revenue_growth_rate) AS avg_growth_rate, STDDEV(revenue_growth_rate) AS growth_volatility, MAX(annual_revenue) AS peak_revenue FROM GrowthRates WHERE revenue_growth_rate IS NOT NULL), ScenarioAnalysis AS (SELECT pm.avg_growth_rate, pm.growth_volatility, pm.peak_revenue, pm.peak_revenue * (1 + pm.avg_growth_rate/100) AS conservative_forecast, pm.peak_revenue * (1 + (pm.avg_growth_rate + pm.growth_volatility)/100) AS optimistic_forecast, pm.peak_revenue * (1 + (pm.avg_growth_rate - pm.growth_volatility)/100) AS pessimistic_forecast FROM PredictiveModeling pm), StrategicRecommendations AS (SELECT CASE WHEN conservative_forecast > peak_revenue * 1.1 THEN 'Expand Market Presence' WHEN conservative_forecast > peak_revenue * 1.05 THEN 'Optimize Current Operations' ELSE 'Focus on Customer Retention' END AS strategic_direction, CASE WHEN growth_volatility > 20 THEN 'High Risk - Diversify Portfolio' WHEN growth_volatility > 10 THEN 'Medium Risk - Monitor Closely' ELSE 'Low Risk - Continue Current Strategy' END AS risk_strategy FROM ScenarioAnalysis sa) SELECT FORMAT(conservative_forecast, 2) AS conservative_forecast, FORMAT(optimistic_forecast, 2) AS optimistic_forecast, FORMAT(pessimistic_forecast, 2) AS pessimistic_forecast, strategic_direction, risk_strategy FROM ScenarioAnalysis sa CROSS JOIN StrategicRecommendations sr;"
    },
    {
        "id": 99,
        "title": "Master Data Management and Data Governance",
        "statement": "Write a query to implement data governance checks and master data management principles across all entities.",
        "solution": "WITH DataQualityMetrics AS (SELECT 'Customer' AS entity, 'Completeness' AS metric, (COUNT(*) - COUNT(CASE WHEN phone IS NULL OR phone = '' THEN 1 END)) * 100.0 / COUNT(*) AS score FROM Customer UNION ALL SELECT 'Customer', 'Accuracy', (COUNT(*) - COUNT(CASE WHEN LENGTH(postalCode) > 10 THEN 1 END)) * 100.0 / COUNT(*) FROM Customer UNION ALL SELECT 'Product', 'Completeness', (COUNT(*) - COUNT(CASE WHEN unitPrice IS NULL OR unitPrice <= 0 THEN 1 END)) * 100.0 / COUNT(*) FROM Product UNION ALL SELECT 'Product', 'Consistency', (COUNT(*) - COUNT(CASE WHEN discontinued NOT IN ('0', '1') THEN 1 END)) * 100.0 / COUNT(*) FROM Product), DataGovernance AS (SELECT entity, AVG(score) AS overall_quality_score, COUNT(*) AS metrics_checked, CASE WHEN AVG(score) >= 95 THEN 'Excellent' WHEN AVG(score) >= 85 THEN 'Good' WHEN AVG(score) >= 75 THEN 'Fair' ELSE 'Poor' END AS data_quality_grade FROM DataQualityMetrics GROUP BY entity), MasterDataConsistency AS (SELECT 'Category-Product Relationship' AS check_type, COUNT(p.productId) - COUNT(c.categoryId) AS inconsistencies FROM Product p LEFT JOIN Category c ON p.categoryId = c.categoryId UNION ALL SELECT 'Customer-Order Relationship', COUNT(s.orderId) - COUNT(c.custId) FROM SalesOrder s LEFT JOIN Customer c ON s.custId = c.custId), GovernanceReport AS (SELECT 'Data Quality' AS governance_area, entity AS sub_area, overall_quality_score AS score, data_quality_grade AS grade FROM DataGovernance UNION ALL SELECT 'Data Consistency', check_type, inconsistencies, CASE WHEN inconsistencies = 0 THEN 'Perfect' WHEN inconsistencies <= 5 THEN 'Good' ELSE 'Needs Attention' END FROM MasterDataConsistency) SELECT governance_area, sub_area, FORMAT(score, 2) AS score, grade FROM GovernanceReport ORDER BY governance_area, score DESC;"
    },
    {
        "id": 100,
        "title": "Ultimate Business Intelligence Dashboard Query",
        "statement": "Write the ultimate query that combines all aspects of business intelligence including real-time analytics, predictive modeling, and strategic insights.",
        "solution": "WITH RealTimeMetrics AS (SELECT 'Today' AS period, COUNT(s.orderId) AS orders, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS revenue, COUNT(DISTINCT s.custId) AS customers FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE DATE(s.orderDate) = CURDATE() UNION ALL SELECT 'This Month', COUNT(s.orderId), SUM(od.quantity * od.unitPrice * (1 - od.discount)), COUNT(DISTINCT s.custId) FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE MONTH(s.orderDate) = MONTH(CURDATE()) AND YEAR(s.orderDate) = YEAR(CURDATE())), PerformanceComparison AS (SELECT rtm.period, rtm.orders, rtm.revenue, rtm.customers, LAG(rtm.orders) OVER (ORDER BY rtm.period DESC) AS prev_orders, LAG(rtm.revenue) OVER (ORDER BY rtm.period DESC) AS prev_revenue FROM RealTimeMetrics rtm), PredictiveInsights AS (SELECT AVG(monthly_revenue) AS avg_monthly_revenue, STDDEV(monthly_revenue) AS revenue_volatility FROM (SELECT DATE_FORMAT(s.orderDate, '%Y-%m') AS month, SUM(od.quantity * od.unitPrice * (1 - od.discount)) AS monthly_revenue FROM SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH) GROUP BY DATE_FORMAT(s.orderDate, '%Y-%m')) AS monthly_data), StrategicKPIs AS (SELECT COUNT(DISTINCT c.custId) AS total_customers, COUNT(DISTINCT p.productId) AS active_products, AVG(od.quantity * od.unitPrice * (1 - od.discount)) AS avg_order_value, COUNT(DISTINCT cat.categoryId) AS product_categories FROM Customer c CROSS JOIN Product p CROSS JOIN SalesOrder s JOIN OrderDetail od ON s.orderId = od.orderId JOIN Category cat ON p.categoryId = cat.categoryId WHERE s.orderDate >= DATE_SUB(CURDATE(), INTERVAL 12 MONTH)), BusinessHealth AS (SELECT 'Revenue Growth' AS metric, CASE WHEN pc.revenue > pc.prev_revenue THEN 'Positive' ELSE 'Negative' END AS status FROM PerformanceComparison pc WHERE pc.period = 'This Month' UNION ALL SELECT 'Customer Acquisition', CASE WHEN pc.customers > pc.prev_customers THEN 'Growing' ELSE 'Declining' END FROM (SELECT period, customers, LAG(customers) OVER (ORDER BY period DESC) AS prev_customers FROM RealTimeMetrics) pc WHERE pc.period = 'This Month'), ExecutiveSummary AS (SELECT sk.total_customers, sk.active_products, FORMAT(sk.avg_order_value, 2) AS avg_order_value, pi.avg_monthly_revenue, pi.revenue_volatility, CASE WHEN pi.revenue_volatility < pi.avg_monthly_revenue * 0.1 THEN 'Stable Business' WHEN pi.revenue_volatility < pi.avg_monthly_revenue * 0.2 THEN 'Moderate Volatility' ELSE 'High Volatility' END AS business_stability FROM StrategicKPIs sk CROSS JOIN PredictiveInsights pi) SELECT 'EXECUTIVE DASHBOARD' AS dashboard_title, CONCAT('Customers: ', es.total_customers, ' | Products: ', es.active_products, ' | AOV: , es.avg_order_value) AS key_metrics, CONCAT('Monthly Revenue Avg: , FORMAT(es.avg_monthly_revenue, 2), ' | Stability: ', es.business_stability) AS business_health FROM ExecutiveSummary es;"
    }
]

# Add the final problems to complete the 100
for problem in final_problems:
    problems["complex"].append(problem)

def create_folder_structure():
    """Create folder structure and SQL files"""
    base_dir = "MySQL_Problems_Northwind"
    
    # Create main directory
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    # Create level directories and files
    for level, problem_list in problems.items():
        level_dir = os.path.join(base_dir, f"{level.title()}_Level")
        if not os.path.exists(level_dir):
            os.makedirs(level_dir)
        
        # Create SQL files for each problem
        for problem in problem_list:
            filename = f"problem_{problem['id']:03d}.sql"
            filepath = os.path.join(level_dir, filename)
            
            # Create SQL file with problem statement and solution
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(f"-- Problem {problem['id']}: {problem['title']}\n")
                f.write(f"-- Level: {level.title()}\n")
                f.write("-- " + "="*60 + "\n\n")
                f.write(f"-- PROBLEM STATEMENT:\n")
                f.write(f"-- {problem['statement']}\n\n")
                f.write("-- " + "="*60 + "\n")
                f.write("-- SOLUTION:\n")
                f.write("-- " + "="*60 + "\n\n")
                # f.write(f"{problem['solution']}\n")
    
    # Create README file
    readme_path = os.path.join(base_dir, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write("# MySQL Practice Problems - Northwind Database\n\n")
        f.write("This collection contains 100 carefully crafted MySQL problems based on the Northwind database schema.\n\n")
        f.write("## Structure\n\n")
        f.write("Problems are organized into four difficulty levels:\n\n")
        
        for level, problem_list in problems.items():
            f.write(f"### {level.title()} Level\n")
            f.write(f"- **Problems {problem_list[0]['id']} - {problem_list[-1]['id']}** ({len(problem_list)} problems)\n")
            if level == "basic":
                f.write("- Focus: Simple SELECT statements, filtering, sorting, basic aggregations\n")
            elif level == "intermediate": 
                f.write("- Focus: JOINs, GROUP BY, subqueries, window functions\n")
            elif level == "hard":
                f.write("- Focus: Complex JOINs, CTEs, advanced analytics, performance optimization\n")
            elif level == "advanced":
                f.write("- Focus: Advanced analytics, business intelligence, machine learning preparation\n")
            elif level == "complex":
                f.write("- Focus: Enterprise-level queries, comprehensive business analysis, data science applications\n")
            f.write("\n")
        
        f.write("## How to Use\n\n")
        f.write("1. Start with Basic Level problems to build foundation\n")
        f.write("2. Progress through each level systematically\n") 
        f.write("3. Each SQL file contains the problem statement and solution\n")
        f.write("4. Try solving the problem before looking at the solution\n\n")
        f.write("## Database Schema\n\n")
        f.write("The problems are based on the Northwind database schema included in the repository.\n")
        f.write("Make sure to create and populate the database before attempting the problems.\n\n")
        f.write("## Topics Covered\n\n")
        f.write("- Basic SQL operations (SELECT, WHERE, ORDER BY)\n")
        f.write("- Aggregate functions and GROUP BY\n")
        f.write("- Table JOINs (INNER, LEFT, RIGHT, FULL)\n")
        f.write("- Subqueries and CTEs\n")
        f.write("- Window functions and analytics\n")
        f.write("- Advanced date/time functions\n")
        f.write("- String manipulation\n")
        f.write("- Performance optimization\n")
        f.write("- Business intelligence queries\n")
        f.write("- Data analysis and reporting\n")
        f.write("- Machine learning data preparation\n\n")
        f.write("Happy Learning! 🚀\n")
    
    # Create summary JSON file
    summary = {
        "total_problems": sum(len(problem_list) for problem_list in problems.values()),
        "levels": {level: len(problem_list) for level, problem_list in problems.items()},
        "created_date": "2024",
        "database": "Northwind"
    }
    
    summary_path = os.path.join(base_dir, "problems_summary.json")
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump(summary, f, indent=2)

if __name__ == "__main__":
    create_folder_structure()
    print("✅ Successfully created MySQL problems folder structure!")
    print(f"📁 Total problems created: {sum(len(problem_list) for problem_list in problems.values())}")
    print("\n📊 Problem distribution:")
    for level, problem_list in problems.items():
        print(f"   {level.title()}: {len(problem_list)} problems")
    print(f"\n📂 Files created in 'MySQL_Problems_Northwind' directory")
    print("🎯 Ready for practice! Start with Basic_Level and work your way up!")