/*
 * Problem 28: Type Query
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Find documents where the 'phone' field is a string.
Collection: users
Expected: Use $type operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
