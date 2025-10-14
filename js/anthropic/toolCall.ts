import Anthropic from "@anthropic-ai/sdk";
import "dotenv/config";
import { traceable } from "langsmith/traceable";

const client = new Anthropic();

function getWeather(location: string): string {
  return JSON.stringify({
    location,
    temperature: 72,
    condition: "sunny",
    humidity: 45,
  });
}

const toolCallExample = traceable(async function toolCallExample(
  messages: Anthropic.Messages.MessageParam[]
) {
  const tools: Anthropic.Messages.Tool[] = [
    {
      name: "get_weather",
      description:
        "Get the current weather in a given location. Returns temperature in Fahrenheit.",
      input_schema: {
        type: "object",
        properties: {
          location: {
            type: "string",
            description: "The city and state, e.g. San Francisco, CA",
          },
        },
        required: ["location"],
      },
    },
  ];

  console.log("Sending initial request with tool definition...\n");

  const message = await client.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    tools,
    messages,
  });

  console.log("Initial response:", JSON.stringify(message.content, null, 2));

  if (message.stop_reason === "tool_use") {
    const toolUseBlock = message.content.find(
      (block) => block.type === "tool_use"
    ) as Anthropic.Messages.ToolUseBlock | undefined;

    if (toolUseBlock && toolUseBlock.name === "get_weather") {
      const location = (toolUseBlock.input as { location: string }).location;
      console.log(`\nExecuting tool: get_weather("${location}")`);

      const weatherData = getWeather(location);
      console.log("Weather data:", weatherData);

      const followUpMessage = await client.messages.create({
        model: "claude-sonnet-4-5",
        max_tokens: 1024,
        tools,
        messages: [
          ...messages,
          {
            role: "assistant",
            content: message.content,
          },
          {
            role: "user",
            content: [
              {
                type: "tool_result",
                tool_use_id: toolUseBlock.id,
                content: weatherData,
              },
            ],
          },
        ],
      });

      console.log(
        "\nFinal response:",
        JSON.stringify(followUpMessage.content, null, 2)
      );
      return followUpMessage;
    }
  }

  return message;
});

export async function main() {
  return toolCallExample([
    {
      role: "user",
      content: "What's the weather like in San Francisco?",
    },
  ]);
}

export { toolCallExample };
