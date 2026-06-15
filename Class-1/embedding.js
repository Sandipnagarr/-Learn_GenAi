import OpenAI from "openai";
import dotenv from "dotenv";

dotenv.config();

const client = new OpenAI({
  apiKey: process.env.OPENAI_API_KEY,
});

const text ="Eiffel Tower is in Paris and is a famous landmark, it is 324 meters tall";

async function generateEmbedding() {
  const response = await client.embeddings.create({
    model: "text-embedding-3-small",
    input: text,
  });

  console.log("Vector Embedding:");
  console.log(response.data[0].embedding);

  console.log("\nVector Length:");
  console.log(response.data[0].embedding.length);
}

generateEmbedding();