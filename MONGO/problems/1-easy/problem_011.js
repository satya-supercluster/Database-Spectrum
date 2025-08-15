/*
 * Problem 11: Skip and Limit
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Skip the first 10 products and return the next 5.
Collection: products
Expected: Use skip() and limit() methods together.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
