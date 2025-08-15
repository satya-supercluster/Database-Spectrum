/*
 * Problem 55: Advanced Text Search
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Search products with text matching and boost results by rating.
Collection: products
Expected: Use $text with $meta score and sorting.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
