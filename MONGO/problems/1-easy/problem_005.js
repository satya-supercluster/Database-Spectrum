/*
 * Problem 5: Simple Projection
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find all users but only return their name and email fields.
Collection: users
Expected: Use projection in find() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
