/*
 * Problem 22: Update Multiple Documents
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Increase the price of all electronics products by 10%.
Collection: products
Expected: Use updateMany() with $mul operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
