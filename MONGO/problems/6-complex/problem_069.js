/*
 * Problem 69: Machine Learning Pipeline
 * Difficulty: 6-COMPLEX
 * 
 * Problem Statement:

Prepare and aggregate data for machine learning model training.
Collections: user_behavior, purchases, demographics
Expected: Feature engineering through aggregation pipeline.

 */

const { connectDB, client } = require("../../config/db");

async function run() {
  const db = await connectDB();
  
  // Write your code here
  




  await client.close();
}

run();
