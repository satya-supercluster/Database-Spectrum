/*
 * Problem 26: Array Size Query
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Find users who have exactly 3 skills.
Collection: users
Expected: Use $size operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
