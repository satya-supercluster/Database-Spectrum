/*
 * Problem 58: Window Functions Simulation
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Calculate running total of sales for each month.
Collection: sales
Expected: Use $group with complex accumulator operations.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
