/*
 * Problem 63: Real-time Analytics Pipeline
 * Difficulty: 5-ADVANCED
 * 
 * Problem Statement:

Create a real-time dashboard showing current sales metrics.
Collection: sales_events
Expected: Use change streams and aggregation pipeline.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
