/*
 * Problem 70: Distributed Data Processing
 * Difficulty: 6-COMPLEX
 * 
 * Problem Statement:

Process large dataset with memory-efficient aggregation.
Collection: big_data (millions of documents)
Expected: Use cursor, batch processing, and memory optimization.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
