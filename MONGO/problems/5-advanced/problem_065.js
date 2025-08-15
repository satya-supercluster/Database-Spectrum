/*
 * Problem 65: Performance Optimization Challenge
 * Difficulty: 5-ADVANCED
 * 
 * Problem Statement:

Optimize a slow query that joins multiple large collections.
Collections: users, orders, products, reviews
Expected: Use explain(), proper indexing, and pipeline optimization.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
