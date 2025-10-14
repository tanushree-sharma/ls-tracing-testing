import Anthropic from "@anthropic-ai/sdk";
import "dotenv/config";
import { traceable } from "langsmith/traceable";

const client = new Anthropic();

const streamingMessage = traceable(async function streamingMessage(
  messages: Anthropic.Messages.MessageParam[]
) {
  console.log("Starting streaming...\n");

  const stream = await client.messages.stream({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages,
  });

  for await (const event of stream) {
    if (
      event.type === "content_block_delta" &&
      event.delta.type === "text_delta"
    ) {
      process.stdout.write(event.delta.text);
    }
  }

  console.log("\n\nStreaming complete!");

  const finalMessage = await stream.finalMessage();
  return finalMessage;
});

export async function main() {
  return streamingMessage([
    {
      role: "user",
      content: "Write a short poem about artificial intelligence.",
    },
  ]);
}

export { streamingMessage };
