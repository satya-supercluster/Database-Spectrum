/*
 * Problem 57: Advanced Pipeline Optimization
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Find the most popular product category for users aged 25-35.
Collections: users, orders, products
Expected: Optimize pipeline order for performance.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
