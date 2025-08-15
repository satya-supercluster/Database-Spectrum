/*
 * Problem 17: Text Search
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Find products where name contains the word 'phone' (case-insensitive).
Collection: products
Expected: Use $regex operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
