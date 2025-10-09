import { ChatAnthropic } from "@langchain/anthropic";
import "dotenv/config";
import { HumanMessage } from "langchain";
import { image } from "../resources/base64BufoApproval";

async function main() {
  const anthropic = new ChatAnthropic({
    model: "claude-sonnet-4-5-20250929",
  });

  const messageWithImageUrl = new HumanMessage({
    content: [
      {
        type: "text",
        text: "Describe this image:",
      },
      // Note contentblock doesn't convert human messages yet. so image_url is used instead. as of alpha.1
      {
        type: "image_url",
        image_url: {
          url: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
        },
      },
    ],
  });
  await anthropic.invoke([messageWithImageUrl]);

  const messageWithImageBase64 = new HumanMessage({
    content: [
      {
        type: "text",
        text: "Describe this image, then generate an intense version of it",
      },
      // Note contentblock doesn't convert human messages yet. so image_url is used instead.
      {
        type: "image_url",
        image_url: {
          url: image,
        },
      },
    ],
  });
  await anthropic.invoke([messageWithImageBase64]);
}

main();
