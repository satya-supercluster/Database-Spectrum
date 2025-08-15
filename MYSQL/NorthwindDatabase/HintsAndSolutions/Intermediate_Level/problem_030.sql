-- Problem 30: Order Details with Product Info
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display order details with product names and category names.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT od.orderDetailId, p.productName, c.categoryName, od.quantity, od.unitPrice FROM OrderDetail od JOIN Product p ON od.productId = p.productId JOIN Category c ON p.categoryId = c.categoryId;
