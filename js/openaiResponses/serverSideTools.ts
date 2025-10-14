import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";

const client = wrapOpenAI(new OpenAI());

async function imageGenerationExample() {
  const response = await client.responses.create({
    model: "gpt-4.1-mini",
    input:
      "Generate an image of gray tabby cat hugging an otter with an orange scarf",
    tools: [{ type: "image_generation" }],
  });
  console.log(response.output_text);
}

async function webSearchExample() {
  const response = await client.responses.create({
    model: "gpt-4.1-mini",
    input: "When is Lincoln's birthday?",
    tools: [{ type: "web_search" }],
  });
  console.log(response.output_text);
}

async function codeExecutionExample() {
  const response = await client.responses.create({
    model: "gpt-4.1-mini",
    input: "Calculate the sum of [1, 2, 3, 4, 5]",
    tools: [{ type: "code_interpreter", container: { type: "auto" } }],
  });
  console.log(response.output_text);
}

export async function main() {
  imageGenerationExample();
  webSearchExample();
  codeExecutionExample();
}
