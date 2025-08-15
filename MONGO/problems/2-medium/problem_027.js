/*
 * Problem 27: Date Range Query
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Find orders placed in the last 30 days.
Collection: orders
Expected: Use Date object and $gte operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
