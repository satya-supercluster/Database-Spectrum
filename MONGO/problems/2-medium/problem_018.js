/*
 * Problem 18: Array Field Query
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Find users who have 'javascript' in their skills array.
Collection: users
Expected: Query array fields directly.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
