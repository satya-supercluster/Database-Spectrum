/*
 * Problem 39: Conditional Updates
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Update the status of all orders: set to 'priority' if amount > 1000, otherwise 'normal'.
Collection: orders
Expected: Use $set with $cond operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
