import { traceable } from "langsmith/traceable";
import { main as messageMain } from "./message";
import { main as multimodalAnthropicMain } from "./multimodalAnthropic";
import { main as multimodalOpenAIMain } from "./multimodalOpenAI";
import { main as streamingMain } from "./streaming";
import { main as toolcallMain } from "./toolcall";

export const langchainv1Main = traceable(async function langchainv1Main() {
  console.log("=== Running LangChain v1 Examples ===\n");

  console.log("--- Message Example ---");
  await messageMain();

  console.log("\n--- Streaming Example ---");
  await streamingMain();

  console.log("\n--- Tool Call Example ---");
  await toolcallMain();

  console.log("\n--- Structured Outputs Example ---");
  // await structuredOutputsMain();

  console.log("\n--- Multimodal OpenAI Example ---");
  await multimodalOpenAIMain();
  console.log("\n--- Multimodal Anthropic Example ---");
  await multimodalAnthropicMain();

  console.log("\n=== All LangChain v1 Examples Complete ===");
});

langchainv1Main();
export const main = langchainv1Main;
