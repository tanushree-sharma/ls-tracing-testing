import { ChatAnthropic } from "@langchain/anthropic";
import "dotenv/config";
import { HumanMessage } from "langchain";
import { traceable } from "langsmith/traceable";

const webSearch = traceable(async function webSearch(claude: ChatAnthropic) {
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
});

const webFetching = traceable(async function webFetching(
  claude: ChatAnthropic
) {
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
});

const codeExecution = traceable(async function codeExecution(
  claude: ChatAnthropic
) {
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
});

export const main = traceable(async function serverSideToolsAnthropicMain(
  outputVersion?: "v0" | "v1"
) {
  // Web Search
  const claudeWithWebSearch = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
    outputVersion,
  });
  await webSearch(claudeWithWebSearch);
  // Web Fetching
  const claudeWithWebFetch = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
    outputVersion,
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
    outputVersion,
    clientOptions: {
      defaultHeaders: {
        "anthropic-beta": "code-execution-2025-08-25",
      },
    },
  });
  await codeExecution(claudeWithCodeExec);
});
