import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";
import { traceable } from "langsmith/traceable";
import {
  getGenerateImageMessage,
  getImageBase64Message,
  getImageUrlMessage,
} from "./multimodalMessages";

const imageUrlInput = traceable(async function imageUrlInput(oai: ChatOpenAI) {
  const response = await oai.invoke([getImageUrlMessage()]);
  console.log(response);
});

const imageBase64Input = traceable(async function imageBase64Input(
  oai: ChatOpenAI
) {
  const response = await oai.invoke([getImageBase64Message()]);
  console.log(response);
});

const imageGeneration = traceable(async function imageGeneration(
  oai: ChatOpenAI
) {
  const response = await oai.invoke([getGenerateImageMessage()]);
  console.log(response);
});

export const main = traceable(async function multimodalOpenAIMain(
  outputVersion?: "v0" | "v1"
) {
  const oai = new ChatOpenAI({
    model: "gpt-5-2025-08-07",
    outputVersion,
  });

  await imageUrlInput(oai);
  await imageBase64Input(oai);
  await imageGeneration(oai);
  // await oai.invoke([getPDFInputMessage()]);
});
