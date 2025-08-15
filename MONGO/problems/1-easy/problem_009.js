/*
 * Problem 9: Sort Results
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find all products sorted by price in ascending order.
Collection: products
Expected: Use sort() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
