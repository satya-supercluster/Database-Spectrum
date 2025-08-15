/*
 * Problem 19: Nested Object Query
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Find users where address.city is 'New York'.
Collection: users
Expected: Use dot notation for nested objects.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
