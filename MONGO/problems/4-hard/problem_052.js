/*
 * Problem 52: Dynamic Schema Query
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Find documents that have at least one field ending with '_id'.
Collection: mixed_schema
Expected: Use $objectToArray and complex matching.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
