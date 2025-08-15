/*
 * Problem 4: Find One Document
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find one user with the name 'John'.
Collection: users
Expected: Use findOne() method.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
