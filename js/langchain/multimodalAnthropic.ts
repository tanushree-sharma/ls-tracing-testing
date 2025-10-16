import { ChatAnthropic } from "@langchain/anthropic";
import "dotenv/config";
import { getCurrentRunTree, traceable } from "langsmith/traceable";
import {
  getGenerateImageMessage,
  getImageBase64Message,
  getImageUrlMessage,
} from "./multimodalMessages";

export const main = traceable(async function multimodalAnthropicMain(
  outputVersion?: "v0" | "v1"
) {
  const runTree = getCurrentRunTree();
  if (runTree) {
    runTree.name = `multimodal_anthropic_example${
      outputVersion ? `_${outputVersion}` : ""
    }`;
  }

  const claude = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
    outputVersion,
  });

  await claude.invoke([getImageUrlMessage()]);
  await claude.invoke([getImageBase64Message()]);
  await claude.invoke([getGenerateImageMessage()]);
  // await claude.invoke([getPDFInputMessage()]);
});
