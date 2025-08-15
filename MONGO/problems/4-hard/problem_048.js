/*
 * Problem 48: Faceted Search
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Create faceted search results showing product count by category and price ranges.
Collection: products
Expected: Use $facet operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
