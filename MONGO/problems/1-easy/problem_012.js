/*
 * Problem 12: Find with OR condition
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find users where age is either 25 or 30.
Collection: users
Expected: Use $or operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
