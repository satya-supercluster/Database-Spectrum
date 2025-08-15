/*
 * Problem 35: Sort Aggregated Results
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Group products by category, count them, and sort by count in descending order.
Collection: products
Expected: Use $group followed by $sort.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
