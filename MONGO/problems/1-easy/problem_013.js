/*
 * Problem 13: Find with IN operator
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find products where category is either 'electronics', 'books', or 'clothing'.
Collection: products
Expected: Use $in operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
