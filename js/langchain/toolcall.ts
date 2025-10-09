import { ChatAnthropic } from "@langchain/anthropic";
import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";
import { tool } from "langchain";
import { z } from "zod";

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

async function main() {
  const oai = new ChatOpenAI({
    model: "gpt-4o-mini",
  });
  const oaiWithTools = oai.bindTools([getWeather]);

  const oaiResponse = await oaiWithTools.invoke("What's the weather in Tokyo?");
  console.log(oaiResponse.tool_calls);

  const anthro = new ChatAnthropic({
    model: "claude-3-5-sonnet-latest",
  });
  const anthroWithTools = anthro.bindTools([getWeather]);
  const anthroResponse = await anthroWithTools.invoke(
    "What's the weather in Tokyo?"
  );
  console.log(anthroResponse.tool_calls);
}

main();
