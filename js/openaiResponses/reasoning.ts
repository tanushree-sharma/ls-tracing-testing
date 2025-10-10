import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";

const client = wrapOpenAI(new OpenAI());

async function main() {
  const response = await client.responses.create({
    model: "gpt-5",
    reasoning: {
      effort: "high",
    },
    input: "What is the capital of France? Explain in one sentence.",
  });

  console.log("Response API output:");
  console.log(response.output_text);
}

main();
