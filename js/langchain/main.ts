import { traceable } from "langsmith/traceable";
import { main as citationsAnthropicMain } from "./citationsAnthropic";
import { main as messageMain } from "./message";
import { main as multimodalAnthropicMain } from "./multimodalAnthropic";
import { main as multimodalOpenAIMain } from "./multimodalOpenAI";
import { main as serverSideToolsAnthropicMain } from "./serverSideToolsAnthropic";
import { main as serverSideToolsOpenAIMain } from "./serverSideToolsOpenAI";
import { main as streamingMain } from "./streaming";
import { main as toolcallMain } from "./toolcall";

export const langchainMain = traceable(async function langchainMain(
  outputVersion?: "v0" | "v1"
) {
  console.log("=== Running LangChain Examples ===\n");

  console.log("--- Message Example ---");
  await messageMain(outputVersion);

  console.log("\n--- Streaming Example ---");
  await streamingMain(outputVersion);

  console.log("\n--- Tool Call Example ---");
  await toolcallMain(outputVersion);

  // console.log("\n--- Structured Outputs Example ---");
  // await structuredOutputsMain(outputVersion);

  console.log("\n--- Multimodal OpenAI Example ---");
  await multimodalOpenAIMain(outputVersion);

  console.log("\n--- Multimodal Anthropic Example ---");
  await multimodalAnthropicMain(outputVersion);

  console.log("\n--- Citations Anthropic Example ---");
  await citationsAnthropicMain(outputVersion);

  console.log("\n--- Server-Side Tools OpenAI Example ---");
  await serverSideToolsOpenAIMain(outputVersion);

  console.log("\n--- Server-Side Tools Anthropic Example ---");
  await serverSideToolsAnthropicMain(outputVersion);

  console.log("\n=== All LangChain Examples Complete ===");
});

langchainMain("v1");
export const main = langchainMain;
