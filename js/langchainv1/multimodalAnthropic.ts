import { initChatModel } from "langchain";
import {
  getImageBase64Message,
  getImageUrlMessage,
} from "./multimodalMessages";

export async function main() {
  const oai = await initChatModel("anthropic:claude-sonnet-4-20250514", {
    outputVersion: "v1",
  });

  await oai.invoke([getImageUrlMessage()]);
  await oai.invoke([getImageBase64Message()]);
  // await oai.invoke([getPDFInputMessage()]);
}
