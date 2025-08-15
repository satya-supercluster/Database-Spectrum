/*
 * Problem 44: Text Index Search
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Create a text index and search for products containing 'wireless bluetooth'.
Collection: products
Expected: Use text index and $text operator.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
