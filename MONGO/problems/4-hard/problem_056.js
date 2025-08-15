/*
 * Problem 56: Transaction Simulation
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Transfer money between two user accounts atomically.
Collection: accounts
Expected: Use sessions and transactions.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
