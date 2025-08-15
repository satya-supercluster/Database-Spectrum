/*
 * Problem 46: Complex Aggregation Pipeline
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Find the top 5 customers by total order amount, including their user details.
Collections: users, orders
Expected: Use complex pipeline with $lookup, $group, $sort, $limit.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
