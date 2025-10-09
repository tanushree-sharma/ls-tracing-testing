import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";

const client = wrapOpenAI(new OpenAI());

async function main() {
  // Using the Responses API (newer simplified API)
  const response = await client.responses.create({
    model: "gpt-5-2025-08-07",
    input: "What is the capital of France?",
  });

  console.log("Response API output:");
  console.log(response.output_text);
}

main();
