import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";

const client = wrapOpenAI(new OpenAI());

async function main() {
  const stream = await client.responses.create({
    model: "gpt-5",
    input: "Write a short poem about artificial intelligence in 4 lines.",
    stream: true,
  });

  console.log("Streaming response:");
  for await (const chunk of stream) {
    if (chunk.type === "response.output_text.delta") {
      console.log(chunk.delta);
    }
  }
}

main();
