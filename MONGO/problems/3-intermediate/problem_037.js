/*
 * Problem 37: Unwind Arrays
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Create a document for each skill of each user (flatten the skills array).
Collection: users
Expected: Use $unwind operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
