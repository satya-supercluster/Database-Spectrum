import os
import json

# Problem definitions with difficulty levels
problems = [
    # EASY LEVEL (1-15)
    {
        "level": "easy",
        "number": 1,
        "title": "Find All Documents",
        "description": """
Find all documents in the 'users' collection.
Expected: Use find() method to retrieve all documents.
"""
    },
    {
        "level": "easy", 
        "number": 2,
        "title": "Find by Single Field",
        "description": """
Find all users where age is 25.
Collection: users
Expected: Use find() with a simple equality condition.
"""
    },
    {
        "level": "easy",
        "number": 3,
        "title": "Count Documents",
        "description": """
Count the total number of documents in the 'products' collection.
Expected: Use countDocuments() method.
"""
    },
    {
        "level": "easy",
        "number": 4,
        "title": "Find One Document",
        "description": """
Find one user with the name 'John'.
Collection: users
Expected: Use findOne() method.
"""
    },
    {
        "level": "easy",
        "number": 5,
        "title": "Simple Projection",
        "description": """
Find all users but only return their name and email fields.
Collection: users
Expected: Use projection in find() method.
"""
    },
    {
        "level": "easy",
        "number": 6,
        "title": "Exclude Fields",
        "description": """
Find all products but exclude the 'description' field.
Collection: products
Expected: Use projection to exclude specific fields.
"""
    },
    {
        "level": "easy",
        "number": 7,
        "title": "Greater Than Query",
        "description": """
Find all products with price greater than 100.
Collection: products
Expected: Use $gt operator.
"""
    },
    {
        "level": "easy",
        "number": 8,
        "title": "Less Than Query", 
        "description": """
Find all users with age less than 30.
Collection: users
Expected: Use $lt operator.
"""
    },
    {
        "level": "easy",
        "number": 9,
        "title": "Sort Results",
        "description": """
Find all products sorted by price in ascending order.
Collection: products
Expected: Use sort() method.
"""
    },
    {
        "level": "easy",
        "number": 10,
        "title": "Limit Results",
        "description": """
Find the first 5 users in the collection.
Collection: users
Expected: Use limit() method.
"""
    },
    {
        "level": "easy",
        "number": 11,
        "title": "Skip and Limit",
        "description": """
Skip the first 10 products and return the next 5.
Collection: products
Expected: Use skip() and limit() methods together.
"""
    },
    {
        "level": "easy",
        "number": 12,
        "title": "Find with OR condition",
        "description": """
Find users where age is either 25 or 30.
Collection: users
Expected: Use $or operator.
"""
    },
    {
        "level": "easy",
        "number": 13,
        "title": "Find with IN operator",
        "description": """
Find products where category is either 'electronics', 'books', or 'clothing'.
Collection: products
Expected: Use $in operator.
"""
    },
    {
        "level": "easy",
        "number": 14,
        "title": "Find with NOT IN",
        "description": """
Find users where status is not 'inactive' or 'banned'.
Collection: users
Expected: Use $nin operator.
"""
    },
    {
        "level": "easy",
        "number": 15,
        "title": "Field Exists Check",
        "description": """
Find all users that have an 'email' field.
Collection: users
Expected: Use $exists operator.
"""
    },

    # MEDIUM LEVEL (16-30)
    {
        "level": "medium",
        "number": 16,
        "title": "Range Query",
        "description": """
Find products with price between 50 and 200 (inclusive).
Collection: products
Expected: Use $gte and $lte operators.
"""
    },
    {
        "level": "medium",
        "number": 17,
        "title": "Text Search",
        "description": """
Find products where name contains the word 'phone' (case-insensitive).
Collection: products
Expected: Use $regex operator.
"""
    },
    {
        "level": "medium",
        "number": 18,
        "title": "Array Field Query",
        "description": """
Find users who have 'javascript' in their skills array.
Collection: users
Expected: Query array fields directly.
"""
    },
    {
        "level": "medium",
        "number": 19,
        "title": "Nested Object Query",
        "description": """
Find users where address.city is 'New York'.
Collection: users
Expected: Use dot notation for nested objects.
"""
    },
    {
        "level": "medium",
        "number": 20,
        "title": "Multiple Conditions",
        "description": """
Find products where category is 'electronics' AND price is less than 500.
Collection: products
Expected: Use implicit $and with multiple conditions.
"""
    },
    {
        "level": "medium",
        "number": 21,
        "title": "Update Single Document",
        "description": """
Update the price of a product with name 'iPhone' to 999.
Collection: products
Expected: Use updateOne() method.
"""
    },
    {
        "level": "medium",
        "number": 22,
        "title": "Update Multiple Documents",
        "description": """
Increase the price of all electronics products by 10%.
Collection: products
Expected: Use updateMany() with $mul operator.
"""
    },
    {
        "level": "medium",
        "number": 23,
        "title": "Insert Single Document",
        "description": """
Insert a new user with name 'Alice', age 28, and email 'alice@example.com'.
Collection: users
Expected: Use insertOne() method.
"""
    },
    {
        "level": "medium",
        "number": 24,
        "title": "Insert Multiple Documents",
        "description": """
Insert 3 new products in a single operation.
Collection: products
Expected: Use insertMany() method.
"""
    },
    {
        "level": "medium",
        "number": 25,
        "title": "Delete Documents",
        "description": """
Delete all users with age greater than 65.
Collection: users
Expected: Use deleteMany() method.
"""
    },
    {
        "level": "medium",
        "number": 26,
        "title": "Array Size Query",
        "description": """
Find users who have exactly 3 skills.
Collection: users
Expected: Use $size operator.
"""
    },
    {
        "level": "medium",
        "number": 27,
        "title": "Date Range Query",
        "description": """
Find orders placed in the last 30 days.
Collection: orders
Expected: Use Date object and $gte operator.
"""
    },
    {
        "level": "medium",
        "number": 28,
        "title": "Type Query",
        "description": """
Find documents where the 'phone' field is a string.
Collection: users
Expected: Use $type operator.
"""
    },
    {
        "level": "medium",
        "number": 29,
        "title": "Add to Array",
        "description": """
Add 'python' to the skills array of user with name 'John'.
Collection: users
Expected: Use $push operator in updateOne().
"""
    },
    {
        "level": "medium",
        "number": 30,
        "title": "Remove from Array",
        "description": """
Remove 'java' from the skills array of all users.
Collection: users
Expected: Use $pull operator in updateMany().
"""
    },

    # INTERMEDIATE LEVEL (31-45)
    {
        "level": "intermediate",
        "number": 31,
        "title": "Basic Aggregation",
        "description": """
Group products by category and count how many products are in each category.
Collection: products
Expected: Use aggregate() with $group stage.
"""
    },
    {
        "level": "intermediate",
        "number": 32,
        "title": "Aggregation with Sum",
        "description": """
Calculate the total value of all products (sum of price * quantity).
Collection: products
Expected: Use $group with $sum and $multiply operators.
"""
    },
    {
        "level": "intermediate",
        "number": 33,
        "title": "Average Calculation",
        "description": """
Find the average age of users in each city.
Collection: users
Expected: Use $group with $avg operator.
"""
    },
    {
        "level": "intermediate",
        "number": 34,
        "title": "Match and Group",
        "description": """
Find the total sales amount for orders placed after 2023-01-01, grouped by customer.
Collection: orders
Expected: Use $match followed by $group.
"""
    },
    {
        "level": "intermediate",
        "number": 35,
        "title": "Sort Aggregated Results",
        "description": """
Group products by category, count them, and sort by count in descending order.
Collection: products
Expected: Use $group followed by $sort.
"""
    },
    {
        "level": "intermediate",
        "number": 36,
        "title": "Project with Calculations",
        "description": """
For each product, calculate a discounted price (20% off) and include it in results.
Collection: products
Expected: Use $project with arithmetic operations.
"""
    },
    {
        "level": "intermediate",
        "number": 37,
        "title": "Unwind Arrays",
        "description": """
Create a document for each skill of each user (flatten the skills array).
Collection: users
Expected: Use $unwind operator.
"""
    },
    {
        "level": "intermediate",
        "number": 38,
        "title": "Lookup Basic Join",
        "description": """
Join users with their orders to show user details with their order information.
Collections: users, orders
Expected: Use $lookup operator.
"""
    },
    {
        "level": "intermediate",
        "number": 39,
        "title": "Conditional Updates",
        "description": """
Update the status of all orders: set to 'priority' if amount > 1000, otherwise 'normal'.
Collection: orders
Expected: Use $set with $cond operator.
"""
    },
    {
        "level": "intermediate",
        "number": 40,
        "title": "Upsert Operation",
        "description": """
Update product inventory, but if product doesn't exist, create it.
Collection: products
Expected: Use updateOne() with upsert: true option.
"""
    },
    {
        "level": "intermediate",
        "number": 41,
        "title": "Array Element Update",
        "description": """
Update the grade of a specific subject for a student.
Collection: students (with grades array)
Expected: Use positional operator $ or arrayFilters.
"""
    },
    {
        "level": "intermediate",
        "number": 42,
        "title": "Index Creation",
        "description": """
Create an index on the 'email' field for faster user lookups.
Collection: users
Expected: Use createIndex() method.
"""
    },
    {
        "level": "intermediate",
        "number": 43,
        "title": "Compound Index",
        "description": """
Create a compound index on 'category' and 'price' fields.
Collection: products
Expected: Use createIndex() with multiple fields.
"""
    },
    {
        "level": "intermediate",
        "number": 44,
        "title": "Text Index Search",
        "description": """
Create a text index and search for products containing 'wireless bluetooth'.
Collection: products
Expected: Use text index and $text operator.
"""
    },
    {
        "level": "intermediate",
        "number": 45,
        "title": "Bulk Operations",
        "description": """
Perform multiple insert, update, and delete operations in a single batch.
Collection: products
Expected: Use bulkWrite() method.
"""
    },

    # HARD LEVEL (46-60)
    {
        "level": "hard",
        "number": 46,
        "title": "Complex Aggregation Pipeline",
        "description": """
Find the top 5 customers by total order amount, including their user details.
Collections: users, orders
Expected: Use complex pipeline with $lookup, $group, $sort, $limit.
"""
    },
    {
        "level": "hard",
        "number": 47,
        "title": "Advanced Array Operations",
        "description": """
Find users whose skills include both 'javascript' and 'python'.
Collection: users
Expected: Use $all operator.
"""
    },
    {
        "level": "hard",
        "number": 48,
        "title": "Faceted Search",
        "description": """
Create faceted search results showing product count by category and price ranges.
Collection: products
Expected: Use $facet operator.
"""
    },
    {
        "level": "hard",
        "number": 49,
        "title": "Time Series Analysis",
        "description": """
Group sales by month and calculate monthly growth percentage.
Collection: orders
Expected: Use date operators and complex aggregation.
"""
    },
    {
        "level": "hard",
        "number": 50,
        "title": "Geospatial Query",
        "description": """
Find all stores within 10km of coordinates [40.7128, -74.0060] (NYC).
Collection: stores
Expected: Use 2dsphere index and $near operator.
"""
    },
    {
        "level": "hard",
        "number": 51,
        "title": "Advanced Lookup with Pipeline",
        "description": """
Join orders with products, but only include products with rating > 4.
Collections: orders, products
Expected: Use $lookup with pipeline parameter.
"""
    },
    {
        "level": "hard",
        "number": 52,
        "title": "Dynamic Schema Query",
        "description": """
Find documents that have at least one field ending with '_id'.
Collection: mixed_schema
Expected: Use $objectToArray and complex matching.
"""
    },
    {
        "level": "hard",
        "number": 53,
        "title": "Recursive Data Query",
        "description": """
Find all employees and their subordinates in a hierarchical structure.
Collection: employees
Expected: Use $graphLookup for recursive relationships.
"""
    },
    {
        "level": "hard",
        "number": 54,
        "title": "Complex Array Filtering",
        "description": """
Find products where at least 2 reviews have rating >= 4.
Collection: products (with reviews array)
Expected: Use $expr with $size and $filter.
"""
    },
    {
        "level": "hard",
        "number": 55,
        "title": "Advanced Text Search",
        "description": """
Search products with text matching and boost results by rating.
Collection: products
Expected: Use $text with $meta score and sorting.
"""
    },
    {
        "level": "hard",
        "number": 56,
        "title": "Transaction Simulation",
        "description": """
Transfer money between two user accounts atomically.
Collection: accounts
Expected: Use sessions and transactions.
"""
    },
    {
        "level": "hard",
        "number": 57,
        "title": "Advanced Pipeline Optimization",
        "description": """
Find the most popular product category for users aged 25-35.
Collections: users, orders, products
Expected: Optimize pipeline order for performance.
"""
    },
    {
        "level": "hard",
        "number": 58,
        "title": "Window Functions Simulation",
        "description": """
Calculate running total of sales for each month.
Collection: sales
Expected: Use $group with complex accumulator operations.
"""
    },
    {
        "level": "hard",
        "number": 59,
        "title": "Advanced Array Updates",
        "description": """
Update all array elements that match multiple conditions.
Collection: students (with nested grade objects)
Expected: Use arrayFilters with complex conditions.
"""
    },
    {
        "level": "hard",
        "number": 60,
        "title": "Custom Aggregation Expression",
        "description": """
Create a custom scoring system based on multiple weighted factors.
Collection: products
Expected: Use $expr with complex mathematical operations.
"""
    },

    # ADVANCED LEVEL (61-65)
    {
        "level": "advanced",
        "number": 61,
        "title": "MapReduce Alternative",
        "description": """
Implement MapReduce-style processing using aggregation pipeline.
Calculate word frequency across all product descriptions.
Collection: products
Expected: Use $split, $unwind, $group for word counting.
"""
    },
    {
        "level": "advanced",
        "number": 62,
        "title": "Advanced Geospatial Analysis",
        "description": """
Find the optimal location for a new store based on customer distribution.
Collections: customers, stores
Expected: Use geospatial aggregation with $geoNear.
"""
    },
    {
        "level": "advanced",
        "number": 63,
        "title": "Real-time Analytics Pipeline",
        "description": """
Create a real-time dashboard showing current sales metrics.
Collection: sales_events
Expected: Use change streams and aggregation pipeline.
"""
    },
    {
        "level": "advanced",
        "number": 64,
        "title": "Advanced Schema Validation",
        "description": """
Implement complex schema validation with custom rules.
Collection: complex_documents
Expected: Use JSON Schema validation with custom validators.
"""
    },
    {
        "level": "advanced",
        "number": 65,
        "title": "Performance Optimization Challenge",
        "description": """
Optimize a slow query that joins multiple large collections.
Collections: users, orders, products, reviews
Expected: Use explain(), proper indexing, and pipeline optimization.
"""
    },

    # COMPLEX LEVEL (66-70)
    {
        "level": "complex",
        "number": 66,
        "title": "Multi-Collection Data Migration",
        "description": """
Migrate data from legacy schema to new schema across multiple collections.
Collections: old_users, old_orders -> users, orders
Expected: Complex aggregation with data transformation.
"""
    },
    {
        "level": "complex",
        "number": 67,
        "title": "Advanced Time Series Aggregation",
        "description": """
Create a time-series analysis with moving averages and trend detection.
Collection: stock_prices
Expected: Use time-based bucketing and statistical operations.
"""
    },
    {
        "level": "complex",
        "number": 68,
        "title": "Graph Analytics",
        "description": """
Find shortest path between two users in a social network.
Collection: connections
Expected: Use $graphLookup with complex path analysis.
"""
    },
    {
        "level": "complex",
        "number": 69,
        "title": "Machine Learning Pipeline",
        "description": """
Prepare and aggregate data for machine learning model training.
Collections: user_behavior, purchases, demographics
Expected: Feature engineering through aggregation pipeline.
"""
    },
    {
        "level": "complex",
        "number": 70,
        "title": "Distributed Data Processing",
        "description": """
Process large dataset with memory-efficient aggregation.
Collection: big_data (millions of documents)
Expected: Use cursor, batch processing, and memory optimization.
"""
    }
]

def create_directory_structure():
    """Create the main problems directory and level subdirectories"""
    base_dir = "problems"
    levels = ["1-easy", "2-medium", "3-intermediate", "4-hard", "5-advanced", "6-complex"]
    
    # Create base problems directory if it doesn't exist
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"✅ Created directory: {base_dir}")
    
    # Create level subdirectories
    for level in levels:
        level_dir = os.path.join(base_dir, level)
        if not os.path.exists(level_dir):
            os.makedirs(level_dir)
            print(f"✅ Created directory: {level_dir}")

def create_problem_file(problem):
    """Create a problem file with the given problem data"""
    # Map problem level to numbered directory
    level_map = {
        "easy": "1-easy",
        "medium": "2-medium",
        "intermediate": "3-intermediate",
        "hard": "4-hard",
        "advanced": "5-advanced",
        "complex": "6-complex"
    }
    level = level_map.get(problem["level"], problem["level"])
    number = problem["number"]
    title = problem["title"]
    description = problem["description"]
    
    # Create filename
    filename = f"problem_{number:03}.js"
    filepath = os.path.join("problems", level, filename)
    
    # Create file content
    content = f'''/*
 * Problem {number}: {title}
 * Difficulty: {level.upper()}
 * 
 * Problem Statement:
{description}
 */

const {{ connectDB, client }} = require("../../config/db");

async function run() {{
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}}

run();
'''
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Created: {filepath}")

def create_readme():
    """Create a comprehensive README file"""
    readme_content = '''# MongoDB Learning Problems

This repository contains 70 progressive MongoDB problems designed to help you master MongoDB queries and operations.

## 📁 Structure

```
mongodb-learning/
├── config/
│   └── db.js          # MongoDB connection setup
├── problems/
│   ├── easy/          # Problems 1-15 (Basic queries, CRUD operations)
│   ├── medium/        # Problems 16-30 (Updates, arrays, dates)
│   ├── intermediate/  # Problems 31-45 (Aggregation, indexes)
│   ├── hard/          # Problems 46-60 (Complex aggregation, joins)
│   ├── advanced/      # Problems 61-65 (Performance, geospatial)
│   └── complex/       # Problems 66-70 (Advanced analytics)
└── package.json
```

## 🎯 Difficulty Levels

### Easy (Problems 1-15)
- Basic find operations
- Simple CRUD operations
- Basic operators ($gt, $lt, $in, etc.)
- Sorting, limiting, and skipping

### Medium (Problems 16-30)
- Range queries
- Text search with regex
- Array operations
- Nested object queries
- Basic updates and deletes

### Intermediate (Problems 31-45)
- Basic aggregation pipelines
- Grouping and calculations
- Joins with $lookup
- Index creation and management
- Bulk operations

### Hard (Problems 46-60)
- Complex aggregation pipelines
- Advanced array operations
- Geospatial queries
- Transactions
- Performance optimization

### Advanced (Problems 61-65)
- MapReduce alternatives
- Real-time analytics
- Schema validation
- Change streams
- Advanced geospatial analysis

### Complex (Problems 66-70)
- Data migration
- Time series analysis
- Graph analytics
- Machine learning pipelines
- Distributed data processing

## 🚀 Getting Started

1. Make sure MongoDB is installed and running on localhost:27017
2. Install dependencies: `npm install mongodb`
3. Start with easy problems and progress through the levels
4. Each problem file contains the problem statement and a template
5. Run each problem: `node problems/easy/problem_1.js`

## 📚 Concepts Covered

- **Basic Queries**: find(), findOne(), count()
- **CRUD Operations**: insert, update, delete operations
- **Query Operators**: $gt, $lt, $in, $or, $and, $regex, etc.
- **Aggregation Framework**: $match, $group, $project, $sort, $limit
- **Joins**: $lookup for combining collections
- **Indexes**: Single field, compound, text indexes
- **Array Operations**: $push, $pull, $addToSet, $unwind
- **Geospatial**: 2dsphere indexes, $near, $geoWithin
- **Transactions**: Multi-document ACID transactions
- **Performance**: Query optimization, explain plans
- **Advanced Features**: Change streams, schema validation

## 💡 Tips

1. Always read the problem statement carefully
2. Think about the most efficient query structure
3. Test your solutions with sample data
4. Use MongoDB Compass to visualize query results
5. Learn to read explain() output for performance optimization

## 🔧 Sample Data

Most problems assume collections with the following structure:

### users
```javascript
{
  _id: ObjectId,
  name: "John Doe",
  email: "john@example.com",
  age: 30,
  address: {
    city: "New York",
    state: "NY"
  },
  skills: ["javascript", "python", "mongodb"],
  status: "active"
}
```

### products
```javascript
{
  _id: ObjectId,
  name: "Product Name",
  category: "electronics",
  price: 299.99,
  quantity: 50,
  description: "Product description",
  rating: 4.5,
  reviews: [...]
}
```

### orders
```javascript
{
  _id: ObjectId,
  userId: ObjectId,
  products: [...],
  total: 599.99,
  status: "completed",
  createdAt: ISODate,
  shippingAddress: {...}
}
```

Happy Learning! 🎉
'''
    
    with open("README.md", 'w', encoding='utf-8') as f:
        f.write(readme_content)
    print("✅ Created: README.md")

def main():
    """Main function to generate all problems"""
    print("🚀 Starting MongoDB Problem Generator...")
    print(f"📊 Total problems to generate: {len(problems)}")
    
    # Create directory structure
    create_directory_structure()
    
    # Generate all problem files
    print("\n📝 Generating problem files...")
    for problem in problems:
        create_problem_file(problem)
    
    # Create README and package.json
    print("\n📚 Creating documentation...")
    create_readme()
    
    # Summary
    print("\n✨ Generation Complete!")
    print("📁 Directory structure created")
    print(f"📝 {len(problems)} problem files generated")
    print("📚 README.md created with detailed instructions")
    
    # Problem count by level
    level_counts = {}
    for problem in problems:
        level = problem["level"]
        level_counts[level] = level_counts.get(level, 0) + 1
    
    print("\n📊 Problems by difficulty:")
    for level, count in level_counts.items():
        print(f"   {level.capitalize()}: {count} problems")
    
    print("\n🎯 Next steps:")
    print("1. Navigate to your MONGO folder")
    print("2. Run: npm install")
    print("3. Make sure MongoDB is running")
    print("4. Start with problems/easy/problem_1.js")
    print("5. Happy learning! 🚀")

if __name__ == "__main__":
    main()