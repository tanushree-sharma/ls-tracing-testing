import { ChatAnthropic } from "@langchain/anthropic";
import "dotenv/config";
import { HumanMessage } from "langchain";

export async function main() {
  const claude = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
  });

  const messages = [
    new HumanMessage({
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
        },
        { type: "text", text: "What color is the grass and sky?" },
      ],
    }),
  ];

  const response = await claude.invoke(messages);

  console.log("Response:", response);
}

main();
