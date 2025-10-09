import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";
import { HumanMessage } from "langchain";
import { image } from "../resources/base64BufoApproval";

async function inputImageUrl(oai: ChatOpenAI) {
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
  await oai.invoke([messageWithImageUrl]);
}

async function inputImageBase64(oai: ChatOpenAI) {
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
  await oai.invoke([messageWithImageBase64]);
}

async function generateImage(oai: ChatOpenAI) {
  const messageWithImage = new HumanMessage({
    content: [
      {
        type: "text",
        text: "Generate an image of a cartoon cat and return it as multimodal png block",
      },
    ],
  });
  await oai.invoke([messageWithImage]);
}

async function main() {
  const oai = new ChatOpenAI({
    model: "gpt-5-2025-08-07",
  });

  // await inputImageUrl(oai);
  // await inputImageBase64(oai);
  await generateImage(oai);
}

main();
