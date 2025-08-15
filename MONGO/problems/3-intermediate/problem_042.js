/*
 * Problem 42: Index Creation
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Create an index on the 'email' field for faster user lookups.
Collection: users
Expected: Use createIndex() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
