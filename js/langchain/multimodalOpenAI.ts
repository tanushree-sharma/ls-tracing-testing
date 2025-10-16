import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";
import { getCurrentRunTree, traceable } from "langsmith/traceable";
import {
  getGenerateImageMessage,
  getImageBase64Message,
  getImageUrlMessage,
} from "./multimodalMessages";

export const main = traceable(async function multimodalOpenAIMain(
  outputVersion?: "v0" | "v1"
) {
  const runTree = getCurrentRunTree();
  if (runTree) {
    runTree.name = `multimodal_openai_example${
      outputVersion ? `_${outputVersion}` : ""
    }`;
  }

  const oai = new ChatOpenAI({
    model: "gpt-5-2025-08-07",
    outputVersion,
  });

  await oai.invoke([getImageUrlMessage()]);
  await oai.invoke([getImageBase64Message()]);
  await oai.invoke([getGenerateImageMessage()]);
  // await oai.invoke([getPDFInputMessage()]);
});
