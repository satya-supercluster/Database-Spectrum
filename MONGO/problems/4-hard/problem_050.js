/*
 * Problem 50: Geospatial Query
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Find all stores within 10km of coordinates [40.7128, -74.0060] (NYC).
Collection: stores
Expected: Use 2dsphere index and $near operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
