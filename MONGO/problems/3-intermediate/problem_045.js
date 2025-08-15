/*
 * Problem 45: Bulk Operations
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Perform multiple insert, update, and delete operations in a single batch.
Collection: products
Expected: Use bulkWrite() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
