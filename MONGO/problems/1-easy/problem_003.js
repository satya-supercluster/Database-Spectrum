/*
 * Problem 3: Count Documents
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Count the total number of documents in the 'products' collection.
Expected: Use countDocuments() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
