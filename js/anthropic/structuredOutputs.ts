import Anthropic from "@anthropic-ai/sdk";
import "dotenv/config";
import { traceable } from "langsmith/traceable";

const client = new Anthropic();

interface Recipe {
  recipe_name: string;
  ingredients: string[];
  instructions: string[];
}

const structuredOutputs = traceable(async function structuredOutputs(
  messages: Anthropic.Messages.MessageParam[]
) {
  const message = await client.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages,
  });

  console.log("Response:", JSON.stringify(message.content, null, 2));

  const textContent = message.content.find((block) => block.type === "text");
  if (textContent && textContent.type === "text") {
    try {
      const jsonMatch = textContent.text.match(/\{[\s\S]*\}/);
      if (jsonMatch) {
        const parsedRecipe: Recipe = JSON.parse(jsonMatch[0]);
        console.log("\nParsed Recipe:", parsedRecipe);
        return parsedRecipe;
      }
    } catch (error) {
      console.error("Failed to parse JSON:", error);
    }
  }

  return message;
});

export async function main() {
  return structuredOutputs([
    {
      role: "user",
      content:
        "Please provide a recipe for chocolate chip cookies in JSON format with fields: recipe_name, ingredients (array), and instructions (array).",
    },
  ]);
}

export { structuredOutputs };
