import "dotenv/config";
import { initChatModel } from "langchain";

export async function main() {
  console.log("=== OpenAI Streaming ===");
  const oai = await initChatModel("openai:gpt-5-nano", {
    outputVersion: "v1",
  });

  const oaiStream = await oai.stream("Write a haiku about programming.");
  for await (const chunk of oaiStream) {
    console.log(chunk.content);
  }
  console.log("\n");

  console.log("=== Anthropic Streaming ===");
  const anthro = await initChatModel("anthropic:claude-sonnet-4-20250514", {
    outputVersion: "v1",
  });

  const anthroStream = await anthro.stream("Write a haiku about programming.");
  for await (const chunk of anthroStream) {
    console.log(chunk.content);
  }
  console.log("\n");
}
