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
        multimodal_anthropic,
        multimodal_messages,
        multimodal_openai,
        streaming,
        structured_outputs,
        tool_call,
    )
except ImportError:
    import langchain_v1.message as message
    import langchain_v1.multimodal_anthropic as multimodal_anthropic
    import langchain_v1.multimodal_messages as multimodal_messages
    import langchain_v1.multimodal_openai as multimodal_openai
    import langchain_v1.streaming as streaming
    import langchain_v1.structured_outputs as structured_outputs
    import langchain_v1.tool_call as tool_call


@traceable(name="langchain_v1 Main")
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

    print("\n--- Multimodal Anthropic Example ---")
    multimodal_anthropic.main()

    print("\n--- Multimodal OpenAI Example ---")
    multimodal_openai.main()

    print("\n=== All LangChain v1 Examples Complete ===")
    return {"status": "complete"}


def main():
    return langchain_v1_main()


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    main()
