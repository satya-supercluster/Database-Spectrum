/*
 * Problem 61: MapReduce Alternative
 * Difficulty: 5-ADVANCED
 * 
 * Problem Statement:

Implement MapReduce-style processing using aggregation pipeline.
Calculate word frequency across all product descriptions.
Collection: products
Expected: Use $split, $unwind, $group for word counting.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
