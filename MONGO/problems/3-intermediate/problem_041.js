/*
 * Problem 41: Array Element Update
 * Difficulty: 3-INTERMEDIATE
 * 
 * Problem Statement:

Update the grade of a specific subject for a student.
Collection: students (with grades array)
Expected: Use positional operator $ or arrayFilters.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
