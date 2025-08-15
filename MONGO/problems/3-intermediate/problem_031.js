/*
 * Problem 31: Basic Aggregation
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Group products by category and count how many products are in each category.
Collection: products
Expected: Use aggregate() with $group stage.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
