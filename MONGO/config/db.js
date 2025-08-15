const { MongoClient } = require("mongodb");
const dotenv = require("dotenv");
const path = require("path");

dotenv.config({ path: path.resolve(__dirname, "../.env") });

const client = new MongoClient(process.env.MONGO_URI);
const dbName = "test";

async function connectDB() {
  try {
    await client.connect();
    console.log("✅ Connected to MongoDB Atlas");
    return client.db(dbName);
  } catch (err) {
    console.error("❌ MongoDB connection error:", err);
    process.exit(1);
  }
}

module.exports = { connectDB, client };
