import "dotenv/config";
import { initChatModel, tool } from "langchain";
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

async function main() {
  const oai = await initChatModel("openai:gpt-5-nano", {
    outputVersion: "v1",
  });
  const oaiWithTools = oai.bindTools([getWeather]);

  const oaiResponse = await oaiWithTools.invoke("What's the weather in Tokyo?");
  console.log(oaiResponse.tool_calls);

  const anthro = await initChatModel("anthropic:claude-sonnet-4-20250514", {
    outputVersion: "v1",
  });
  const anthroWithTools = anthro.bindTools([getWeather]);
  const anthroResponse = await anthroWithTools.invoke(
    "What's the weather in Tokyo?"
  );
  console.log(anthroResponse.tool_calls);
}

main();
