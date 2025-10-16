import { ChatAnthropic } from "@langchain/anthropic";
import "dotenv/config";
import { traceable } from "langsmith/traceable";
import {
  getGenerateImageMessage,
  getImageBase64Message,
  getImageUrlMessage,
} from "./multimodalMessages";

const imageUrlInput = traceable(async function imageUrlInput(
  claude: ChatAnthropic
) {
  const response = await claude.invoke([getImageUrlMessage()]);
  console.log(response);
});

const imageBase64Input = traceable(async function imageBase64Input(
  claude: ChatAnthropic
) {
  const response = await claude.invoke([getImageBase64Message()]);
  console.log(response);
});

const imageGeneration = traceable(async function imageGeneration(
  claude: ChatAnthropic
) {
  const response = await claude.invoke([getGenerateImageMessage()]);
  console.log(response);
});

export const main = traceable(async function multimodalAnthropicMain(
  outputVersion?: "v0" | "v1"
) {
  const claude = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
    outputVersion,
  });

  await imageUrlInput(claude);
  await imageBase64Input(claude);
  await imageGeneration(claude);
  // await claude.invoke([getPDFInputMessage()]);
});
