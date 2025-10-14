import Anthropic from "@anthropic-ai/sdk";
import "dotenv/config";
import { traceable } from "langsmith/traceable";
import { image } from "../resources/base64BufoApproval";

const client = new Anthropic();

const imageInputFromUrl = traceable(async function imageInputFromUrl(
  messages: Anthropic.Messages.MessageParam[]
) {
  console.log(
    "Analyzing image from URL (fetching and converting to base64)...\n"
  );

  const message = await client.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages,
  });

  console.log("Response:", message.content);
  return message;
});

const imageInputFromBase64 = traceable(async function imageInputFromBase64(
  messages: Anthropic.Messages.MessageParam[]
) {
  console.log("Analyzing image from base64...\n");

  const message = await client.messages.create({
    model: "claude-sonnet-4-5",
    max_tokens: 1024,
    messages,
  });

  console.log("Response:", message.content);
  return message;
});

const mainExample = traceable(async function mainExample() {
  const imageUrl =
    "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg";

  await imageInputFromUrl([
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "Describe this image in detail:",
        },
        {
          type: "image",
          source: {
            // @ts-ignore
            type: "url",
            url: imageUrl,
          },
        },
      ],
    },
  ]);

  console.log("\n" + "=".repeat(50) + "\n");

  const base64Data = image.replace(/^data:image\/\w+;base64,/, "");

  await imageInputFromBase64([
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "What do you see in this image? Describe it in detail.",
        },
        {
          type: "image",
          source: {
            type: "base64",
            media_type: "image/png",
            data: base64Data,
          },
        },
      ],
    },
  ]);
});

export async function main() {
  return mainExample();
}

export { imageInputFromBase64, imageInputFromUrl };
