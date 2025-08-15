/*
 * Problem 60: Custom Aggregation Expression
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Create a custom scoring system based on multiple weighted factors.
Collection: products
Expected: Use $expr with complex mathematical operations.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
