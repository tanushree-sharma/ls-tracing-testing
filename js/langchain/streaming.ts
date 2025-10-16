import { ChatAnthropic } from "@langchain/anthropic";
import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";
import { traceable } from "langsmith/traceable";

export const main = traceable(async function streamingMain(
  outputVersion?: "v0" | "v1"
) {
  console.log("=== OpenAI Streaming ===");
  const oai = new ChatOpenAI({
    model: "gpt-5-2025-08-07",
    outputVersion,
  });

  const oaiStream = await oai.stream("Write a haiku about programming.");
  for await (const chunk of oaiStream) {
    console.log(chunk.content);
  }
  console.log("\n");

  console.log("=== Anthropic Streaming ===");
  const anthro = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
    outputVersion,
  });

  const anthroStream = await anthro.stream("Write a haiku about programming.");
  for await (const chunk of anthroStream) {
    console.log(chunk.content);
  }
  console.log("\n");
});
