import { ChatAnthropic } from "@langchain/anthropic";
import "dotenv/config";
import { getGenerateImageMessage } from "./multimodalMessages";

async function main() {
  const claude = new ChatAnthropic({
    model: "claude-sonnet-4-20250514",
  });

  // await claude.invoke([getImageUrlMessage()]);
  // await claude.invoke([getImageBase64Message()]);
  await claude.invoke([getGenerateImageMessage()]);
}

main();
