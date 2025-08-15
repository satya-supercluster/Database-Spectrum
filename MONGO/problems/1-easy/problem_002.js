/*
 * Problem 2: Find by Single Field
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find all users where age is 25.
Collection: users
Expected: Use find() with a simple equality condition.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
