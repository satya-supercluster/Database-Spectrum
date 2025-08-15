/*
 * Problem 66: Multi-Collection Data Migration
 * Difficulty: 6-COMPLEX
 * 
 * Problem Statement:

Migrate data from legacy schema to new schema across multiple collections.
Collections: old_users, old_orders -> users, orders
Expected: Complex aggregation with data transformation.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
