/*
 * Problem 38: Lookup Basic Join
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Join users with their orders to show user details with their order information.
Collections: users, orders
Expected: Use $lookup operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
