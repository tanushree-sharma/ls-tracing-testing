import Anthropic from "@anthropic-ai/sdk";
import "dotenv/config";
import { traceable } from "langsmith/traceable";
import { milwaukeeArtMuseumPDFBase64 } from "../resources/Milwaukee Art Museum PDF";

const client = new Anthropic();

const pdfInput = traceable(async function pdfInput(
  messages: Anthropic.Messages.MessageParam[]
) {
  console.log("Analyzing PDF document...\n");

  const message = await client.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 2048,
    messages,
  });

  console.log("Response:", message.content);
  return message;
});

export async function main() {
  return pdfInput([
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "Please summarize this PDF document:",
        },
        {
          type: "document",
          source: {
            type: "base64",
            media_type: "application/pdf",
            data: milwaukeeArtMuseumPDFBase64,
          },
        },
      ],
    },
  ]);
}

export { pdfInput };
