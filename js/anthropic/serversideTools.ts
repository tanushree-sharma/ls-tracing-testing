import Anthropic from "@anthropic-ai/sdk";
import "dotenv/config";
import { traceable } from "langsmith/traceable";

const client = new Anthropic();

const codeExecutionExample = traceable(async function codeExecutionExample(
  messages: Anthropic.Messages.MessageParam[],
  tools: any[]
) {
  console.log("=== Code Execution Tool ===");
  console.log("Messages:", JSON.stringify(messages, null, 2));
  console.log("Tools:", JSON.stringify(tools, null, 2));

  const response = await client.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    tools,
    messages,
    betas: ["code-execution-2025-08-25"],
  });

  console.log("Response:", JSON.stringify(response, null, 2));
  return response;
});

const webFetchExample = traceable(async function webFetchExample(
  messages: Anthropic.Messages.MessageParam[],
  tools: any[]
) {
  console.log("=== Web Fetch Tool ===");
  console.log("Messages:", JSON.stringify(messages, null, 2));
  console.log("Tools:", JSON.stringify(tools, null, 2));

  const response = await client.beta.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    tools,
    messages,
    betas: ["web-fetch-2025-09-10"],
  });

  console.log("Response:", JSON.stringify(response, null, 2));
  return response;
});

const webSearchExample = traceable(async function webSearchExample(
  messages: Anthropic.Messages.MessageParam[],
  tools: any[]
) {
  console.log("=== Web Search Tool ===");
  console.log("Messages:", JSON.stringify(messages, null, 2));
  console.log("Tools:", JSON.stringify(tools, null, 2));

  const response = await client.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 4096,
    tools,
    messages,
  });

  console.log("Response:", JSON.stringify(response, null, 2));
  return response;
});

export async function main() {
  console.log("=== Running Server-Side Tools Examples ===\n");

  // Code Execution Example
  console.log("\n--- Code Execution Example ---");
  const codeResult = await codeExecutionExample(
    [
      {
        role: "user",
        content:
          "Calculate the first 10 fibonacci numbers and create a plot showing their growth.",
      },
    ],
    [
      {
        type: "code_execution_20250825",
        name: "code_execution",
      },
    ]
  );

  // Web Fetch Example
  console.log("\n--- Web Fetch Example ---");
  const fetchResult = await webFetchExample(
    [
      {
        role: "user",
        content:
          "Fetch and summarize the content from https://www.anthropic.com/news",
      },
    ],
    [
      {
        type: "web_fetch_20250910",
        name: "web_fetch",
      },
    ]
  );

  // Web Search Example
  console.log("\n--- Web Search Example ---");
  const searchResult = await webSearchExample(
    [
      {
        role: "user",
        content:
          "What are the latest developments in quantum computing in 2025?",
      },
    ],
    [
      {
        type: "web_search_20250305",
        name: "web_search",
        max_uses: 5,
      },
    ]
  );

  console.log("\n=== All Server-Side Tools Examples Complete ===");

  return {
    codeResult,
    fetchResult,
    searchResult,
  };
}

main();
