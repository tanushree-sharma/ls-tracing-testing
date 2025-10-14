import Anthropic from "@anthropic-ai/sdk";
import "dotenv/config";
import { traceable } from "langsmith/traceable";

const client = new Anthropic();

const normalMessage = traceable(async function normalMessage(
  messages: Anthropic.Messages.MessageParam[]
) {
  const message = await client.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages,
  });

  console.log("Response:", message.content);
  return message;
});

export async function main() {
  return normalMessage([
    {
      role: "user",
      content: "Hello, Claude! Can you tell me about the weather?",
    },
  ]);
}

export { normalMessage };
