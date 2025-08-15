/*
 * Problem 34: Match and Group
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Find the total sales amount for orders placed after 2023-01-01, grouped by customer.
Collection: orders
Expected: Use $match followed by $group.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
