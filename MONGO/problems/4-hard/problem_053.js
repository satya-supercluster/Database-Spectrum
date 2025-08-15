/*
 * Problem 53: Recursive Data Query
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Find all employees and their subordinates in a hierarchical structure.
Collection: employees
Expected: Use $graphLookup for recursive relationships.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
