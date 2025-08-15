import os

def create_mysql_problems():
    """
    Creates 100 MySQL query problems based on Northwind database schema
    Organized in difficulty levels: Basic, Intermediate, Hard, Advanced, Complex
    """
    
    # Problem definitions organized by difficulty
    problems = {
        "01_Basic": [
            "-- Problem 1: Retrieve all columns from the Category table.",
            "-- Problem 2: Find all customer company names and contact names.",
            "-- Problem 3: List all product names and their unit prices.",
            "-- Problem 4: Get all employee first names and last names.",
            "-- Problem 5: Display all supplier company names from USA.",
            "-- Problem 6: Find all products that are discontinued.",
            "-- Problem 7: List all customers from London.",
            "-- Problem 8: Get all orders placed in the year 1996.",
            "-- Problem 9: Find all employees hired after January 1, 1993.",
            "-- Problem 10: Display all products with unit price greater than $20.",
            "-- Problem 11: List all territories in the 'Northern' region.",
            "-- Problem 12: Find all customers whose company name starts with 'A'.",
            "-- Problem 13: Get all products from category ID 1.",
            "-- Problem 14: Display all orders with freight cost less than $10.",
            "-- Problem 15: Find all employees with 'Sales' in their title.",
            "-- Problem 16: List all products that have units in stock greater than 0.",
            "-- Problem 17: Get all customers from Germany or France.",
            "-- Problem 18: Find all orders shipped by shipper ID 3.",
            "-- Problem 19: Display all products with reorder level of 0.",
            "-- Problem 20: List all employees born before 1960.",
        ],
        
        "02_Intermediate": [
            "-- Problem 21: Find the total number of products in each category (show category name).",
            "-- Problem 22: Calculate the average unit price of all products.",
            "-- Problem 23: Get the count of orders placed by each customer (show company name).",
            "-- Problem 24: Find the most expensive product in each category.",
            "-- Problem 25: List customers who have placed more than 5 orders.",
            "-- Problem 26: Calculate the total freight cost for all orders in 1997.",
            "-- Problem 27: Find employees who manage other employees (show manager details).",
            "-- Problem 28: Get the total value of inventory for each supplier.",
            "-- Problem 29: List products that have never been ordered.",
            "-- Problem 30: Find the top 5 customers by total order value.",
            "-- Problem 31: Calculate the average quantity ordered for each product.",
            "-- Problem 32: Get customers who have ordered products from more than 3 different categories.",
            "-- Problem 33: Find the month with the highest total sales in 1997.",
            "-- Problem 34: List employees and the territories they cover (show territory description).",
            "-- Problem 35: Calculate the total discount given on each order.",
            "-- Problem 36: Find products that are low in stock (below reorder level).",
            "-- Problem 37: Get the number of orders handled by each employee per year.",
            "-- Problem 38: List customers who haven't placed any orders in 1998.",
            "-- Problem 39: Find the average order value for each customer.",
            "-- Problem 40: Get products with the highest profit margin (assuming cost is 60% of unit price).",
        ],
        
        "03_Hard": [
            "-- Problem 41: Find customers who have ordered all products from a specific category.",
            "-- Problem 42: Calculate the running total of orders for each customer by date.",
            "-- Problem 43: Get the second highest unit price product in each category.",
            "-- Problem 44: Find employees who have sold products to customers in more than 5 different countries.",
            "-- Problem 45: List the top 3 products by revenue in each quarter of 1997.",
            "-- Problem 46: Calculate the percentage contribution of each category to total sales.",
            "-- Problem 47: Find customers whose average order value is above the overall average.",
            "-- Problem 48: Get the growth rate of orders month-over-month for 1997.",
            "-- Problem 49: List products that have been ordered by more than 50% of all customers.",
            "-- Problem 50: Find the correlation between product price and order quantity.",
            "-- Problem 51: Calculate the customer retention rate (customers who ordered in consecutive years).",
            "-- Problem 52: Get suppliers whose products have the highest average discount.",
            "-- Problem 53: Find the optimal reorder point for each product based on historical data.",
            "-- Problem 54: List customers who have the most diverse product portfolio (different categories).",
            "-- Problem 55: Calculate the seasonal sales pattern for each product category.",
            "-- Problem 56: Find employees with the highest customer satisfaction (lowest return rate).",
            "-- Problem 57: Get the market share of each supplier in their respective categories.",
            "-- Problem 58: List the most profitable customer-product combinations.",
            "-- Problem 59: Find territories with declining sales trends over time.",
            "-- Problem 60: Calculate the inventory turnover rate for each product.",
        ],
        
        "04_Advanced": [
            "-- Problem 61: Create a recursive query to build the employee hierarchy tree.",
            "-- Problem 62: Calculate the Pareto analysis (80/20 rule) for customers and revenue.",
            "-- Problem 63: Find the optimal product bundling opportunities using association rules.",
            "-- Problem 64: Implement a cohort analysis for customer behavior over time.",
            "-- Problem 65: Calculate the churn probability for each customer segment.",
            "-- Problem 66: Create a recommendation system for products based on purchase history.",
            "-- Problem 67: Find anomalies in ordering patterns using statistical methods.",
            "-- Problem 68: Calculate the lifetime value of each customer using predictive modeling.",
            "-- Problem 69: Implement dynamic pricing analysis based on demand patterns.",
            "-- Problem 70: Create a territory optimization model based on sales performance.",
            "-- Problem 71: Calculate the cross-selling effectiveness matrix.",
            "-- Problem 72: Find the optimal inventory levels using economic order quantity (EOQ).",
            "-- Problem 73: Implement a sales forecasting model using moving averages.",
            "-- Problem 74: Create a customer segmentation model using RFM analysis.",
            "-- Problem 75: Calculate the product cannibalization effect within categories.",
            "-- Problem 76: Find the most effective sales channels for each product type.",
            "-- Problem 77: Implement a demand sensing algorithm for better inventory management.",
            "-- Problem 78: Create a dynamic territory assignment system for employees.",
            "-- Problem 79: Calculate the price elasticity of demand for each product.",
            "-- Problem 80: Find the optimal product mix for maximum profitability.",
        ],
        
        "05_Complex": [
            "-- Problem 81: Build a comprehensive dashboard showing KPIs with drill-down capabilities using CTEs and window functions.",
            "-- Problem 82: Create a multi-dimensional analysis cube for sales data with all possible combinations of dimensions.",
            "-- Problem 83: Implement a complete supply chain optimization model considering lead times, costs, and demand variability.",
            "-- Problem 84: Design a fraud detection system for unusual ordering patterns using multiple statistical techniques.",
            "-- Problem 85: Create a comprehensive customer journey analysis from first contact to last purchase with attribution modeling.",
            "-- Problem 86: Build a real-time inventory management system with automatic reordering and supplier selection optimization.",
            "-- Problem 87: Implement a complete A/B testing framework for pricing strategies with statistical significance testing.",
            "-- Problem 88: Create a multi-objective optimization system for territory management balancing workload, revenue, and geography.",
            "-- Problem 89: Build a comprehensive competitor analysis system using market share evolution and pricing benchmarks.",
            "-- Problem 90: Design a complete business intelligence solution with automated data quality checks and anomaly detection.",
            "-- Problem 91: Create a sophisticated customer lifetime value model incorporating multiple touchpoints and channels.",
            "-- Problem 92: Implement a comprehensive sales performance management system with goal setting and achievement tracking.",
            "-- Problem 93: Build a complete market basket analysis system with confidence, support, and lift calculations.",
            "-- Problem 94: Create a dynamic pricing optimization engine considering competition, inventory, and demand elasticity.",
            "-- Problem 95: Design a comprehensive supplier relationship management system with performance scorecards.",
            "-- Problem 96: Implement a complete sales territory optimization system using geographic and demographic data.",
            "-- Problem 97: Build a sophisticated demand planning system incorporating seasonality, trends, and external factors.",
            "-- Problem 98: Create a comprehensive customer churn prevention system with predictive modeling and intervention strategies.",
            "-- Problem 99: Design a complete financial performance analysis system with variance analysis and forecasting.",
            "-- Problem 100: Build an integrated business optimization platform combining all previous analyses into a unified decision support system.",
        ]
    }
    
    # Create main directory
    main_dir = "MySQL_Query_Problems"
    if not os.path.exists(main_dir):
        os.makedirs(main_dir)
    
    problem_counter = 1
    
    # Create subdirectories and files
    for level, level_problems in problems.items():
        level_dir = os.path.join(main_dir, level)
        if not os.path.exists(level_dir):
            os.makedirs(level_dir)
        
        # Create SQL files for each problem
        for problem_statement in level_problems:
            filename = f"problem_{problem_counter:03d}.sql"
            filepath = os.path.join(level_dir, filename)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write("/*\n")
                f.write(f" * MySQL Query Problem #{problem_counter}\n")
                f.write(f" * Difficulty Level: {level.split('_')[1]}\n")
                f.write(" * Database: NorthwindCore\n")
                f.write(" * \n")
                f.write(f" * {problem_statement[3:]}\n")  # Remove the '-- ' prefix
                f.write(" * \n")
                f.write(" * Tables involved: Refer to the schema provided\n")
                f.write(" * \n")
                f.write(" * Instructions:\n")
                f.write(" * - Write a MySQL query to solve this problem\n")
                f.write(" * - Ensure your query is optimized and follows best practices\n")
                f.write(" * - Test your query against the Northwind database\n")
                f.write(" * - Consider edge cases and data validation\n")
                f.write(" */\n\n")
                f.write("-- Write your MySQL query below:\n\n")
            
            problem_counter += 1
    
    # Create README file with instructions
    readme_content = """# MySQL Query Problems - Northwind Database

This collection contains 100 MySQL query problems based on the Northwind database schema, organized into 5 difficulty levels:

## Structure
- **01_Basic** (Problems 1-20): Simple SELECT statements, basic WHERE clauses, simple JOINs
- **02_Intermediate** (Problems 21-40): Aggregate functions, GROUP BY, subqueries, multiple JOINs
- **03_Hard** (Problems 41-60): Complex JOINs, window functions, advanced subqueries, statistical analysis
- **04_Advanced** (Problems 61-80): Recursive queries, complex analytical functions, optimization problems
- **05_Complex** (Problems 81-100): Multi-faceted business problems requiring comprehensive analysis

## Database Schema
The problems are based on the NorthwindCore database with the following main tables:
- Category, Product, Supplier
- Customer, SalesOrder, OrderDetail
- Employee, Territory, Region, Shipper
- CustomerDemographics, CustomerCustomerDemographics, EmployeeTerritory

## How to Use
1. Set up the NorthwindCore database using the provided schema
2. Navigate to each problem file
3. Read the problem statement in the comments
4. Write your MySQL query below the comment section
5. Test your solution against the database

## Skills Covered
- Basic SQL syntax and operations
- JOIN operations (INNER, LEFT, RIGHT, FULL OUTER)
- Aggregate functions and GROUP BY
- Subqueries and CTEs
- Window functions
- Recursive queries
- Performance optimization
- Business intelligence and analytics
- Statistical analysis with SQL

## Tips
- Always test your queries with sample data first
- Consider query performance and optimization
- Validate edge cases and null values
- Use proper indexing strategies
- Follow SQL best practices and naming conventions

Good luck with your MySQL learning journey!
"""
    
    readme_path = os.path.join(main_dir, "README.md")
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"Successfully created {problem_counter-1} MySQL problems!")
    print(f"Directory structure created: {main_dir}/")
    print("Levels created:")
    for level in problems.keys():
        level_name = level.split('_')[1]
        count = len(problems[level])
        print(f"  - {level_name}: {count} problems")
    
    print(f"\nAll files saved in '{main_dir}' directory")
    print("Each .sql file contains the problem statement as comments")
    print("README.md file created with detailed instructions")

if __name__ == "__main__":
    create_mysql_problems()