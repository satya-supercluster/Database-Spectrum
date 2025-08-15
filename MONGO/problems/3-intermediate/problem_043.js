/*
 * Problem 43: Compound Index
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Create a compound index on 'category' and 'price' fields.
Collection: products
Expected: Use createIndex() with multiple fields.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
