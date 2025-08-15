/*
 * Problem 64: Advanced Schema Validation
 * Difficulty: 5-ADVANCED
 * 
 * Problem Statement:

Implement complex schema validation with custom rules.
Collection: complex_documents
Expected: Use JSON Schema validation with custom validators.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
