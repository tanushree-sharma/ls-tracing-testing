import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";
import { zodTextFormat } from "openai/helpers/zod";
import { z } from "zod";

const client = wrapOpenAI(new OpenAI());

const PersonSchema = z.object({
  name: z.string(),
  age: z.number(),
  occupation: z.string(),
  hobbies: z.array(z.string()),
});

async function main() {
  const response = await client.responses.create({
    model: "gpt-4o",
    input:
      "Tell me about a fictional software engineer named Alice who is 28 years old.",
    text: {
      format: zodTextFormat(PersonSchema, "person"),
    },
  });

  const person = JSON.parse(response.output_text);

  console.log("Structured output response:");
  console.log(person);
}

main();
