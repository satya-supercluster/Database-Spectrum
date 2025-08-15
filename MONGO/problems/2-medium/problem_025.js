/*
 * Problem 25: Delete Documents
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Delete all users with age greater than 65.
Collection: users
Expected: Use deleteMany() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
