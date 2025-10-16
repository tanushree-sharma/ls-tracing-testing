import os
import sys

# Add parent directory to path for direct execution
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from langsmith import traceable

# Use try/except to handle both direct execution and module import
try:
    from . import (
        message,
        multimodal_messages,
        server_tool_calls_anthropic,
        server_tool_calls_openai,
        streaming,
        structured_outputs,
        tool_call,
    )
except ImportError:
    import message
    import multimodal_messages
    import server_tool_calls_anthropic
    import server_tool_calls_openai
    import streaming
    import structured_outputs
    import tool_call


def langchain_v1_main(output_version: str = "v1", use_responses_api: bool = False):
    """Run all LangChain v1 examples."""
    print("=== Running LangChain v1 Examples ===\n")

    print("--- Message Example ---")
    message.main(output_version, use_responses_api)

    print("\n--- Streaming Example ---")
    streaming.main(output_version, use_responses_api)

    print("\n--- Tool Call Example ---")
    tool_call.main(output_version, use_responses_api)

    print("\n--- Structured Outputs Example ---")
    structured_outputs.main(output_version, use_responses_api)

    print("\n--- Multimodal Messages Example ---")
    multimodal_messages.main(output_version, use_responses_api)

    if not use_responses_api:
        print("\n--- server tool calls Anthropic Example ---")
        server_tool_calls_anthropic.main(output_version)

    print("\n--- server tool calls OpenAI Example ---")
    server_tool_calls_openai.main(output_version, use_responses_api)

    print("\n=== All LangChain v1 Examples Complete ===")
    return {"status": "complete"}


@traceable
def main(output_version: str = "v1", use_responses_api: bool = False, run_tree=None):
    if run_tree:
        api_suffix = " + Responses API" if use_responses_api else ""
        run_tree.name = f"LangChain ({output_version}{api_suffix})"
    return langchain_v1_main(output_version, use_responses_api)


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    main(output_version="v1")
