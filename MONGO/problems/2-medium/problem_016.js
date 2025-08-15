/*
 * Problem 16: Range Query
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Find products with price between 50 and 200 (inclusive).
Collection: products
Expected: Use $gte and $lte operators.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
