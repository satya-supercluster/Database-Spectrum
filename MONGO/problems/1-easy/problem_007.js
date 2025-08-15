/*
 * Problem 7: Greater Than Query
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find all products with price greater than 100.
Collection: products
Expected: Use $gt operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
