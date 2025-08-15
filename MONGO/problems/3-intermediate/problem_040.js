/*
 * Problem 40: Upsert Operation
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Update product inventory, but if product doesn't exist, create it.
Collection: products
Expected: Use updateOne() with upsert: true option.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
