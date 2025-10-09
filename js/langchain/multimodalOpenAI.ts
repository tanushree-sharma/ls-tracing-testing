import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";
import { getGenerateImageMessage } from "./multimodalMessages";

async function main() {
  const oai = new ChatOpenAI({
    model: "gpt-5-2025-08-07",
  });

  // await oai.invoke([getImageUrlMessage()]);
  // await oai.invoke([getImageBase64Message()]);
  await oai.invoke([getGenerateImageMessage()]);
}

main();
