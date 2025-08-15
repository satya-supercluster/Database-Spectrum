/*
 * Problem 36: Project with Calculations
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

For each product, calculate a discounted price (20% off) and include it in results.
Collection: products
Expected: Use $project with arithmetic operations.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
