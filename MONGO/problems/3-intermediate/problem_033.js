/*
 * Problem 33: Average Calculation
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Find the average age of users in each city.
Collection: users
Expected: Use $group with $avg operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
