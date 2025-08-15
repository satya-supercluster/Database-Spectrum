/*
 * Problem 20: Multiple Conditions
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Find products where category is 'electronics' AND price is less than 500.
Collection: products
Expected: Use implicit $and with multiple conditions.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
