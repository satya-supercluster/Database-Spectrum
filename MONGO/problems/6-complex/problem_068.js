/*
 * Problem 68: Graph Analytics
 * Difficulty: 6-COMPLEX
 * 
 * Problem Statement:

Find shortest path between two users in a social network.
Collection: connections
Expected: Use $graphLookup with complex path analysis.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
