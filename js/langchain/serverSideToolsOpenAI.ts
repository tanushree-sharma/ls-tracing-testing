import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";
import { HumanMessage } from "langchain";
import { getCurrentRunTree, traceable } from "langsmith/traceable";

async function generateImage(oai: ChatOpenAI) {
  const humanMessage = new HumanMessage({
    content: [
      {
        type: "text",
        text: "Generate an image of a cartoon cat and return it as multimodal png block",
      },
    ],
  });

  const oaiResponse = await oai.invoke([humanMessage], {
    tools: [{ type: "image_generation" }],
  });
  console.log(oaiResponse);
}

async function webSearch(oai: ChatOpenAI) {
  const humanMessage = new HumanMessage({
    content: [
      {
        type: "text",
        text: "When is Lincoln's birthday?",
      },
    ],
  });
  const oaiResponse = await oai.invoke([humanMessage], {
    tools: [{ type: "web_search" }],
  });
  console.log(oaiResponse);
}

async function codeExecution(oai: ChatOpenAI) {
  const humanMessage = new HumanMessage({
    content: [
      {
        type: "text",
        text: "Calculate the sum of [1, 2, 3, 4, 5]",
      },
    ],
  });
  const oaiResponse = await oai.invoke([humanMessage], {
    tools: [{ type: "code_interpreter", container: { type: "auto" } }],
  });
  console.log(oaiResponse);
}

export const main = traceable(async function serverSideToolsOpenAIMain(
  outputVersion?: "v0" | "v1"
) {
  const runTree = getCurrentRunTree();
  if (runTree) {
    runTree.name = `serverside_tools_openai_example${
      outputVersion ? `_${outputVersion}` : ""
    }`;
  }

  const oai = new ChatOpenAI({
    model: "gpt-5-2025-08-07",
    outputVersion: outputVersion || "v1",
  });
  await generateImage(oai);
  await webSearch(oai);
  await codeExecution(oai);
});
