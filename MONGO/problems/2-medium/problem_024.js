/*
 * Problem 24: Insert Multiple Documents
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Insert 3 new products in a single operation.
Collection: products
Expected: Use insertMany() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
