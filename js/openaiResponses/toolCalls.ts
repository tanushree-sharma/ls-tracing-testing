import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";

const client = wrapOpenAI(new OpenAI());

const tools = [
  {
    type: "function" as const,
    name: "get_weather",
    description: "Get the current weather in a given location",
    parameters: {
      type: "object" as const,
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
    strict: false,
  },
];

export async function main() {
  const response = await client.responses.create({
    model: "gpt-4o",
    input: "What's the weather like in San Francisco?",
    tools,
  });

  console.log("Response with automatic tool execution:");
  console.log(response.output_text);

  if (response.output) {
    console.log("\nTool calls made:");
    for (const output of response.output) {
      if (output.type === "function_call") {
        console.log(`- ${output.name}(${JSON.stringify(output.arguments)})`);
      }
    }
  }
}
