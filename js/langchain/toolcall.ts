import { ChatAnthropic } from "@langchain/anthropic";
import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";
import { tool } from "langchain";
import { getCurrentRunTree, traceable } from "langsmith/traceable";
import { z } from "zod";

// @ts-ignore
const getWeather = tool(
  (input: { location: string }) => {
    return `It's sunny in ${input.location}.`;
  },
  {
    name: "get_weather",
    description: "Get the weather at a location.",
    schema: z.object({
      location: z.string().describe("The location to get the weather for"),
    }),
  }
);

export const main = traceable(async function toolCallMain(
  outputVersion?: "v0" | "v1"
) {
  const runTree = getCurrentRunTree();
  if (runTree) {
    runTree.name = `toolcall_example${
      outputVersion ? `_${outputVersion}` : ""
    }`;
  }

  const oai = new ChatOpenAI({
    model: "gpt-5-2025-08-07",
    outputVersion,
  });
  const oaiWithTools = oai.bindTools([getWeather]);

  const oaiResponse = await oaiWithTools.invoke("What's the weather in Tokyo?");
  console.log(oaiResponse.tool_calls);

  const anthro = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
    outputVersion,
  });
  const anthroWithTools = anthro.bindTools([getWeather]);
  const anthroResponse = await anthroWithTools.invoke(
    "What's the weather in Tokyo?"
  );
  console.log(anthroResponse.tool_calls);
});
