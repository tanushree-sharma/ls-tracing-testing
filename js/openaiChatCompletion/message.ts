import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";

const client = wrapOpenAI(new OpenAI());

export async function main() {
  const response = await client.chat.completions.create({
    model: "gpt-4o",
    messages: [
      {
        role: "user",
        content: "What is the capital of France?",
      },
    ],
  });

  const responseMessage = response.choices[0].message;

  console.log("Response API output:");
  console.log(responseMessage.content);
}
