import "dotenv/config";
import { HumanMessage, initChatModel, SystemMessage } from "langchain";

async function main() {
  const oai = await initChatModel("openai:gpt-5-nano", {
    outputVersion: "v1",
  });

  const systemMsg = new SystemMessage("You are a helpful assistant.");
  const humanMsg = new HumanMessage("Hello, how are you?");

  const messages = [systemMsg, humanMsg];
  const oaiResponse = await oai.invoke(messages);
  console.log(oaiResponse);

  const anthro = await initChatModel("anthropic:claude-sonnet-4-20250514", {
    outputVersion: "v1",
  });

  const anthroResponse = await anthro.invoke(messages);
  console.log(anthroResponse);
}

main();
