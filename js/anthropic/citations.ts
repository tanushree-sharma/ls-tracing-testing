import Anthropic from "@anthropic-ai/sdk";
import "dotenv/config";
import { traceable } from "langsmith/traceable";

const client = new Anthropic();

const createMessage = traceable(client.messages.create.bind(client.messages), {
  name: "anthropic_messages_create",
}) as any as typeof client.messages.create;

const citationsExample = traceable(async function citationsExample(
  messages: Anthropic.Messages.MessageParam[]
) {
  console.log("Sending request with citations enabled...\n");

  const message = await createMessage({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages,
  });

  console.log("Response:", JSON.stringify(message.content, null, 2));
  return message;
});

export async function main() {
  return citationsExample([
    {
      role: "user",
      content: [
        {
          type: "document",
          source: {
            type: "text",
            media_type: "text/plain",
            data: "The grass is green. The sky is blue.",
          },
          title: "My Document",
          context: "This is a trustworthy document.",
          citations: { enabled: true },
        } as any,
        {
          type: "text",
          text: "What color is the grass and sky?",
        },
      ],
    },
  ]);
}
main();
