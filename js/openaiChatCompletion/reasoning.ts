import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";

const client = wrapOpenAI(new OpenAI());

async function main() {
  // Using the Responses API (newer simplified API)
  const response = await client.chat.completions.create({
    model: "gpt-5",
    messages: [
      {
        role: "user",
        content: "What is the capital of France?",
      },
    ],
    reasoning_effort: "high",
  });

  const responseMessage = response.choices[0].message;

  console.log("Response API output:");
  console.log(responseMessage.content);
}

main();
