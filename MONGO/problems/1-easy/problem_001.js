/*
 * Problem 1: Find All Documents
 * Difficulty: 1-EASY
 * 
 * Problem Statement:

Find all documents in the 'users' collection.
Expected: Use find() method to retrieve all documents.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  
  const users = await db.collection('users').find().toArray();
  console.log(users);



  await client.close();
}

run();
