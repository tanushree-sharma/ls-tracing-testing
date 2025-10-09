import { ChatAnthropic } from "@langchain/anthropic";
import { ChatOpenAI } from "@langchain/openai";
import "dotenv/config";
import { z } from "zod";

const Movie = z.object({
  title: z.string().describe("The title of the movie"),
  year: z.number().describe("The year the movie was released"),
  rating: z.number().describe("The rating of the movie"),
});

async function main() {
  const oai = new ChatOpenAI({
    model: "gpt-4o-mini",
  });

  const oaiWithStructuredOutput = oai.withStructuredOutput(Movie);
  const oaiResponse = await oaiWithStructuredOutput.invoke(
    "Tell me about the movie The Matrix"
  );
  console.log(oaiResponse);

  const anthro = new ChatAnthropic({
    model: "claude-3-5-sonnet-latest",
  });

  const anthroWithStructuredOutput = anthro.withStructuredOutput(Movie);
  const anthroResponse = await anthroWithStructuredOutput.invoke(
    "Tell me about the movie The Matrix"
  );
  console.log(anthroResponse);
}

main();
