/*
 * Problem 30: Remove from Array
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Remove 'java' from the skills array of all users.
Collection: users
Expected: Use $pull operator in updateMany().

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
