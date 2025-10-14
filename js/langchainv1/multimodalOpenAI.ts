import "dotenv/config";
import { initChatModel } from "langchain";
import { getPDFInputMessage } from "./multimodalMessages";

async function generateImage() {
  const oai = await initChatModel("openai:gpt-5-nano", {
    outputVersion: "v1",
  });
  const oaiWithTools = oai.bindTools([
    {
      type: "image_generation",
      quality: "low",
    },
  ]);

  const oaiResponse = await oaiWithTools.invoke(
    "Generate an image of a tubby cat in a yellow sweater in oil painting style"
  );
  console.log(oaiResponse.tool_calls);
}

export async function main() {
  const oai = await initChatModel("openai:gpt-5-nano", {
    outputVersion: "v1",
  });

  // await oai.invoke([getImageUrlMessage()]);
  // await oai.invoke([getImageBase64Message()]);
  // await generateImage();
  await oai.invoke([getPDFInputMessage()]);
}
