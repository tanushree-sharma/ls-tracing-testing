import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";
import { getPDFInputMessage } from "./multimodalMessages";

export async function main() {
  const oai = new ChatOpenAI({
    model: "gpt-5-2025-08-07",
  });

  // await oai.invoke([getImageUrlMessage()]);
  // await oai.invoke([getImageBase64Message()]);
  // await oai.invoke([getGenerateImageMessage()]);
  await oai.invoke([getPDFInputMessage()]);
}
