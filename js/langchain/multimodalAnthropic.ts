import { ChatAnthropic } from "@langchain/anthropic";
import "dotenv/config";
import { HumanMessage } from "langchain";
import { image } from "../resources/base64BufoApproval";

async function inputImageUrl(claude: ChatAnthropic) {
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
  await claude.invoke([messageWithImageUrl]);
}

async function inputImageBase64(claude: ChatAnthropic) {
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
  await claude.invoke([messageWithImageBase64]);
}

async function generateImage(claude: ChatAnthropic) {
  const messageWithImage = new HumanMessage({
    content: [
      {
        type: "text",
        text: "Generate an image of a cartoon cat and return it as multimodal png block",
      },
    ],
  });
  await claude.invoke([messageWithImage]);
}

async function main() {
  const claude = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
  });

  // await inputImageUrl(oai);
  // await inputImageBase64(oai);
  await generateImage(claude);
}

main();
