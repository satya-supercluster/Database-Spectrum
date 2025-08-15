/*
 * Problem 62: Advanced Geospatial Analysis
 * Difficulty: 5-ADVANCED
 * 
 * Problem Statement:

Find the optimal location for a new store based on customer distribution.
Collections: customers, stores
Expected: Use geospatial aggregation with $geoNear.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
