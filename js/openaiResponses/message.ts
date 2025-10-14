import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";

const client = wrapOpenAI(new OpenAI());

export async function main() {
  const response = await client.responses.create({
    model: "gpt-4o",
    input: "What is the capital of France? Explain in one sentence.",
  });

  console.log("Response API output:");
  console.log(response.output_text);
}
