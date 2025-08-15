# MongoDB Learning Problems

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
