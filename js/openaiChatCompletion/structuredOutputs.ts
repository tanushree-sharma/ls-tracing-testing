import "dotenv/config";
import { wrapOpenAI } from "langsmith/wrappers";
import { OpenAI } from "openai";
import { zodResponseFormat } from "openai/helpers/zod";
import { z } from "zod";

const client = wrapOpenAI(new OpenAI());

const PersonSchema = z.object({
  name: z.string(),
  age: z.number(),
  occupation: z.string(),
  hobbies: z.array(z.string()),
});

async function main() {
  const response = await client.chat.completions.create({
    model: "gpt-5-2025-08-07",
    messages: [
      {
        role: "user",
        content:
          "Tell me about a fictional software engineer named Alice who is 28 years old.",
      },
    ],
    response_format: zodResponseFormat(PersonSchema, "person"),
  });

  const person = JSON.parse(response.choices[0].message.content!);

  console.log("Structured output response:");
  console.log(person);
}

main();
