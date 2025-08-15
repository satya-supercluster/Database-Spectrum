/*
 * Problem 10: Limit Results
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find the first 5 users in the collection.
Collection: users
Expected: Use limit() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
