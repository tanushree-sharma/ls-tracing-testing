import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langsmith import traceable


@traceable(name="OpenAI Message")
def message_openai(output_version: str = "v1", use_responses_api: bool = False):
    """Simple message with OpenAI."""
    model = init_chat_model(
        "gpt-5-mini",
        model_provider="openai",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )
    messages = [
        SystemMessage(content="Translate the following from English into Italian"),
        HumanMessage(content="hi!"),
    ]

    response = model.invoke(messages)
    print(f"OpenAI response: {response.content}")
    return response


@traceable(name="Anthropic Message")
def message_anthropic(output_version: str = "v1"):
    """Simple message with Anthropic."""
    model = init_chat_model(
        "anthropic:claude-3-7-sonnet-latest", output_version=output_version
    )
    messages = [HumanMessage(content="Why do parrots talk?")]

    response = model.invoke(messages)
    print(f"Anthropic response: {response.content}")
    return response


@traceable
def main(output_version: str = "v1", use_responses_api: bool = False, run_tree=None):
    if run_tree:
        api_suffix = " + Responses API" if use_responses_api else ""
        run_tree.name = f"LangChain Simple messages ({output_version}{api_suffix})"
    print("Running LangChain v1 message examples...")
    message_openai(output_version, use_responses_api)
    if use_responses_api:
        return {"message": "complete"}
    message_anthropic(output_version)
    return {"message": "complete"}
