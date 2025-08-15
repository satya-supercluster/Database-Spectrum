/*
 * Problem 47: Advanced Array Operations
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Find users whose skills include both 'javascript' and 'python'.
Collection: users
Expected: Use $all operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
