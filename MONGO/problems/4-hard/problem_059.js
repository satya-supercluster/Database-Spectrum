/*
 * Problem 59: Advanced Array Updates
 * Difficulty: 4-HARD
 * 
 * Problem Statement:

Update all array elements that match multiple conditions.
Collection: students (with nested grade objects)
Expected: Use arrayFilters with complex conditions.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
