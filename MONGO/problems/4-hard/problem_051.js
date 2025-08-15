/*
 * Problem 51: Advanced Lookup with Pipeline
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Join orders with products, but only include products with rating > 4.
Collections: orders, products
Expected: Use $lookup with pipeline parameter.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
