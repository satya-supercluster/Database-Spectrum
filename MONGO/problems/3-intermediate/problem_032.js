/*
 * Problem 32: Aggregation with Sum
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Calculate the total value of all products (sum of price * quantity).
Collection: products
Expected: Use $group with $sum and $multiply operators.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
