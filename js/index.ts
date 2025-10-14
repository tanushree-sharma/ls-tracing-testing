import "dotenv/config";
import { anthropicMain } from "./anthropic/main";
import { langchainMain } from "./langchain/main";
import { langchainv1Main } from "./langchainv1/main";
import { openaiChatCompletionMain } from "./openaiChatCompletion/main";
import { openaiResponsesMain } from "./openaiResponses/main";

langchainv1Main();
anthropicMain();
langchainMain();
openaiResponsesMain();
openaiChatCompletionMain();
