/*
 * Problem 54: Complex Array Filtering
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Find products where at least 2 reviews have rating >= 4.
Collection: products (with reviews array)
Expected: Use $expr with $size and $filter.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
