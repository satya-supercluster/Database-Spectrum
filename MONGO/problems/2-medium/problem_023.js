/*
 * Problem 23: Insert Single Document
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Insert a new user with name 'Alice', age 28, and email 'alice@example.com'.
Collection: users
Expected: Use insertOne() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
