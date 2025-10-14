import { traceable } from "langsmith/traceable";
import { main as imageInputMain } from "./imageInput";
import { main as messageMain } from "./message";
import { main as pdfInputMain } from "./pdfInput";
import { main as streamingMain } from "./streaming";
import { main as structuredOutputsMain } from "./structuredOutputs";
import { main as toolCallMain } from "./toolCall";

export const anthropicMain = traceable(async function anthropicMain() {
  console.log("=== Running Anthropic Examples ===\n");

  console.log("--- Message Example ---");
  await messageMain();

  console.log("\n--- Streaming Example ---");
  await streamingMain();

  console.log("\n--- Tool Call Example ---");
  await toolCallMain();

  console.log("\n--- Structured Outputs Example ---");
  await structuredOutputsMain();

  console.log("\n--- Image Input Example ---");
  await imageInputMain();

  console.log("\n--- PDF Input Example ---");
  await pdfInputMain();

  console.log("\n=== All Anthropic Examples Complete ===");
});

anthropicMain();

export const main = anthropicMain;
