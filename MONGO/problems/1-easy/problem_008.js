/*
 * Problem 8: Less Than Query
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find all users with age less than 30.
Collection: users
Expected: Use $lt operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
