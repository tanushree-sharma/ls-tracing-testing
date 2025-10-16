import os
import sys

# Add parent directory to path for direct execution
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


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
    import message  # noqa: F401
    import multimodal_messages  # noqa: F401
    import server_tool_calls_anthropic  # noqa: F401
    import server_tool_calls_openai  # noqa: F401
    import streaming  # noqa: F401
    import structured_outputs  # noqa: F401
    import tool_call  # noqa: F401


def langchain_v1_main():
    """Run all LangChain v1 examples."""
    print("=== Running LangChain v1 Examples ===\n")

    print("--- Message Example ---")
    message.main()

    print("\n--- Streaming Example ---")
    streaming.main()

    print("\n--- Tool Call Example ---")
    tool_call.main()

    print("\n--- Structured Outputs Example ---")
    structured_outputs.main()

    print("\n--- Multimodal Messages Example ---")
    multimodal_messages.main()

    print("\n--- server tool calls Anthropic Example ---")
    server_tool_calls_anthropic.main()

    print("\n--- server tool calls OpenAI Example ---")
    server_tool_calls_openai.main()

    print("\n=== All LangChain v1 Examples Complete ===")
    return {"status": "complete"}


def main():
    return langchain_v1_main()


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    main()
