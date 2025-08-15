/*
 * Problem 14: Find with NOT IN
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find users where status is not 'inactive' or 'banned'.
Collection: users
Expected: Use $nin operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
