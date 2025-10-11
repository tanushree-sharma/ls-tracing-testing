import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";

async function main() {
  const model = new ChatOpenAI({ model: "gpt-5" });

  model.invoke([{ role: "human", content: [{ type: "text", text: [] }] }]);
  // const oai = await initChatModel("anthropic:claude-sonnet-4-5-20250929", {});

  // const systemMsg = new SystemMessage("You are a helpful assistant.");
  // const humanMsg = new HumanMessage("Hello, how are you?");

  // const messages = [systemMsg, humanMsg];
  // const oaiResponse = await oai.invoke(messages);
  // console.log(oaiResponse);
}

main();
