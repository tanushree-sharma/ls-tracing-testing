import { ChatAnthropic } from "@langchain/anthropic";
import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";

async function main() {
  console.log("=== OpenAI Streaming ===");
  const oai = new ChatOpenAI({
    model: "gpt-4o-mini",
  });

  const oaiStream = await oai.stream("Write a haiku about programming.");
  for await (const chunk of oaiStream) {
    console.log(chunk.content);
  }
  console.log("\n");

  console.log("=== Anthropic Streaming ===");
  const anthro = new ChatAnthropic({
    model: "claude-3-5-sonnet-latest",
  });

  const anthroStream = await anthro.stream("Write a haiku about programming.");
  for await (const chunk of anthroStream) {
    console.log(chunk.content);
  }
  console.log("\n");
}

main();
