import { traceable } from "langsmith/traceable";
import { main as messageMain } from "./message";
import { main as multimodalMain } from "./multimodal";
import { main as reasoningMain } from "./reasoning";
import { main as serverSideToolsMain } from "./serverSideTools";
import { main as streamingMain } from "./streaming";
import { main as structuredOutputsMain } from "./structuredOutputs";
import { main as toolCallsMain } from "./toolCalls";

export const openaiResponsesMain = traceable(
  async function openaiResponsesMain() {
    console.log("=== Running OpenAI Responses API Examples ===\n");

    console.log("--- Message Example ---");
    await messageMain();

    console.log("\n--- Reasoning Example ---");
    await reasoningMain();

    console.log("\n--- Streaming Example ---");
    await streamingMain();

    console.log("\n--- Structured Outputs Example ---");
    await structuredOutputsMain();

    console.log("\n--- Tool Calls Example ---");
    await toolCallsMain();

    console.log("\n--- Multimodal Example ---");
    await multimodalMain();

    console.log("\n--- Server Side Tools Example ---");
    await serverSideToolsMain();

    console.log("\n=== All OpenAI Responses API Examples Complete ===");
  }
);

openaiResponsesMain();
export const main = openaiResponsesMain;
