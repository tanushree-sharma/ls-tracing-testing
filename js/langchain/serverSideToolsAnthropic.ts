import { ChatAnthropic } from "@langchain/anthropic";
import "dotenv/config";
import { HumanMessage } from "langchain";

async function webSearch(claude: ChatAnthropic) {
  console.log("\n=== Web Search Example ===");

  const message = new HumanMessage({
    content: [
      {
        type: "text",
        text: "Research the latest developments in quantum computing and provide a summary",
      },
    ],
  });

  const response = await claude.invoke([message], {
    tools: [
      {
        type: "web_search_20250305",
        name: "web_search",
        max_uses: 10,
      },
    ],
  });

  console.log(response);
}

async function webFetching(claude: ChatAnthropic) {
  console.log("\n=== Web Fetching Example ===");

  const message = new HumanMessage({
    content: [
      {
        type: "text",
        text: "Please analyze the content at https://www.milwaukeeartmuseum.org/visit/exhibitions/women-who-made-history",
      },
    ],
  });

  const response = await claude.invoke([message], {
    tools: [
      {
        type: "web_fetch_20250910",
        name: "web_fetch",
        max_uses: 3,
      },
    ],
  });

  console.log(response);
}

async function codeExecution(claude: ChatAnthropic) {
  console.log("\n=== Code Execution Example ===");

  const message = new HumanMessage({
    content: [
      {
        type: "text",
        text: "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
      },
    ],
  });
  const tool = { type: "code_execution_20250522", name: "code_execution" };
  const claudeWithTools = claude.bindTools([tool]);

  const response = await claudeWithTools.invoke([message]);

  console.log(response);
}

export async function main() {
  // Web Search
  const claudeWithWebSearch = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
  });
  await webSearch(claudeWithWebSearch);
  // Web Fetching
  const claudeWithWebFetch = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
    clientOptions: {
      defaultHeaders: {
        "anthropic-beta": "web-fetch-2025-09-10",
      },
    },
  });
  await webFetching(claudeWithWebFetch);
  // Code Execution
  const claudeWithCodeExec = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
    clientOptions: {
      defaultHeaders: {
        "anthropic-beta": "code-execution-2025-08-25",
      },
    },
  });
  await codeExecution(claudeWithCodeExec);
}
main();
