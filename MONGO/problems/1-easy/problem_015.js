/*
 * Problem 15: Field Exists Check
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find all users that have an 'email' field.
Collection: users
Expected: Use $exists operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
