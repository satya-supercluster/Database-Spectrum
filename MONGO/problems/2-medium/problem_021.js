/*
 * Problem 21: Update Single Document
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Update the price of a product with name 'iPhone' to 999.
Collection: products
Expected: Use updateOne() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
