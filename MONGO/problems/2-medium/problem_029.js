/*
 * Problem 29: Add to Array
 * Difficulty: 2-MEDIUM
 * 
 * Problem Statement:

Add 'python' to the skills array of user with name 'John'.
Collection: users
Expected: Use $push operator in updateOne().

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
