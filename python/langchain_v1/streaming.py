import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from langchain.chat_models import init_chat_model
from langsmith import traceable


@traceable(name="OpenAI Streaming")
def streaming_example_openai(
    output_version: str = "v1", use_responses_api: bool = False
):
    """Stream LangChain v1 response with OpenAI."""
    model = init_chat_model(
        "gpt-4o",
        model_provider="openai",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )

    print("Starting OpenAI streaming...")
    for chunk in model.stream("Write a short poem about artificial intelligence."):
        print(chunk.content, end="", flush=True)

    print("\n\nOpenAI streaming complete!")
    return {"streaming": "complete"}


@traceable(name="Anthropic Streaming")
def streaming_example_anthropic(output_version: str = "v1"):
    """Stream LangChain v1 response with Anthropic."""
    model = init_chat_model(
        "claude-3-5-sonnet-20241022",
        model_provider="anthropic",
        output_version=output_version,
    )

    print("Starting Anthropic streaming...")
    for chunk in model.stream("Write a short poem about artificial intelligence."):
        print(chunk.content, end="", flush=True)

    print("\n\nAnthropic streaming complete!")
    return {"streaming": "complete"}


@traceable
def main(output_version: str = "v1", use_responses_api: bool = False, run_tree=None):
    if run_tree:
        api_suffix = " + Responses API" if use_responses_api else ""
        run_tree.name = f"LangChain Streaming ({output_version}{api_suffix})"
    print("Running LangChain v1 streaming examples...\n")
    streaming_example_openai(output_version, use_responses_api)
    print("\n" + "=" * 50 + "\n")
    if not use_responses_api:
        streaming_example_anthropic(output_version)
    return {"streaming": "complete"}
