/*
 * Problem 49: Time Series Analysis
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Group sales by month and calculate monthly growth percentage.
Collection: orders
Expected: Use date operators and complex aggregation.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
