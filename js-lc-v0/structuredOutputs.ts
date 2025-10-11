import "dotenv/config";
import { initChatModel } from "langchain/chat_models/universal";
import { z } from "zod";

const Movie = z.object({
  title: z.string().describe("The title of the movie"),
  year: z.number().describe("The year the movie was released"),
  rating: z.number().describe("The rating of the movie"),
});

async function main() {
  const oai = await initChatModel("openai:gpt-5-nano", {
    outputVersion: "v1",
  });

  const oaiWithStructuredOutput = oai.withStructuredOutput(Movie);
  const oaiResponse = await oaiWithStructuredOutput.invoke(
    "Tell me about the movie The Matrix"
  );
  console.log(oaiResponse);
}

main();
