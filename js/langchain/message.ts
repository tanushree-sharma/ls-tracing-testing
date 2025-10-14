import { ChatAnthropic } from "@langchain/anthropic";
import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";

export async function main() {
  const oai = new ChatOpenAI({
    model: "gpt-4o-mini",
  });

  const oaiResponse = await oai.invoke("Why do parrots talk?");
  console.log(oaiResponse);

  const anthro = new ChatAnthropic({
    model: "claude-3-5-sonnet-latest",
  });

  const anthroResponse = await anthro.invoke("Why do parrots talk?");
  console.log(anthroResponse);
}
