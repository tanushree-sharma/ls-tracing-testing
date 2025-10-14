import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";

const client = wrapOpenAI(new OpenAI());

const tools = [
  {
    type: "function" as const,
    function: {
      name: "get_weather",
      description: "Get the current weather in a given location",
      parameters: {
        type: "object",
        properties: {
          location: {
            type: "string",
            description: "The city and state, e.g. San Francisco, CA",
          },
          unit: {
            type: "string",
            enum: ["celsius", "fahrenheit"],
            description: "The temperature unit to use",
          },
        },
        required: ["location"],
      },
    },
  },
];

function getWeather(location: string, unit: string = "fahrenheit") {
  return JSON.stringify({
    location,
    temperature: unit === "celsius" ? "22" : "72",
    unit,
    forecast: "sunny",
  });
}

export async function main() {
  const messages: OpenAI.Chat.ChatCompletionMessageParam[] = [
    {
      role: "user",
      content: "What's the weather like in San Francisco?",
    },
  ];

  const response = await client.chat.completions.create({
    model: "gpt-5-2025-08-07",
    messages,
    tools,
  });

  const responseMessage = response.choices[0].message;
  messages.push(responseMessage);

  const toolCalls = responseMessage.tool_calls;

  if (toolCalls) {
    for (const toolCall of toolCalls) {
      const functionName = toolCall.id;
      // @ts-ignore
      const functionArgs = JSON.parse(toolCall.function.arguments);

      let functionResponse = "";
      if (functionName === "get_weather") {
        functionResponse = getWeather(functionArgs.location, functionArgs.unit);
      }

      messages.push({
        role: "tool",
        tool_call_id: toolCall.id,
        content: functionResponse,
      });
    }

    const secondResponse = await client.chat.completions.create({
      model: "gpt-5-2025-08-07",
      messages,
    });

    console.log("Tool call response:");
    console.log(secondResponse.choices[0].message.content);
  }
}
