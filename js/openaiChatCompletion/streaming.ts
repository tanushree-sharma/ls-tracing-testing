import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";

const client = wrapOpenAI(new OpenAI());

export async function main() {
  const stream = await client.chat.completions.create({
    model: "gpt-5-2025-08-07",
    messages: [
      {
        role: "user",
        content: "Write a short poem about artificial intelligence.",
      },
    ],
    stream: true,
  });

  console.log("Streaming response:");
  for await (const chunk of stream) {
    const content = chunk.choices[0]?.delta?.content;
    if (content) {
      console.log(content);
    }
  }
  console.log("\n");
}
