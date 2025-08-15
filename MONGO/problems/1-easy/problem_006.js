/*
 * Problem 6: Exclude Fields
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find all products but exclude the 'description' field.
Collection: products
Expected: Use projection to exclude specific fields.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
