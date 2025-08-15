-- Problem 35: Products with Supplier Contact Info
-- Level: Intermediate
-- ============================================================

-- PROBLEM STATEMENT:
-- Write a query to display products with their supplier contact information.

-- ============================================================
-- SOLUTION:
-- ============================================================

SELECT p.productName, s.companyName AS supplier, s.contactName, s.phone, s.email FROM Product p JOIN Supplier s ON p.supplierId = s.supplierId;
