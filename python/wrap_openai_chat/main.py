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
        multimodal,
        reasoning,
        streaming,
        structured_outputs,
        tool_calls,
    )
except ImportError:
    import wrap_openai_chat.message as message
    import wrap_openai_chat.multimodal as multimodal
    import wrap_openai_chat.reasoning as reasoning
    import wrap_openai_chat.streaming as streaming
    import wrap_openai_chat.structured_outputs as structured_outputs
    import wrap_openai_chat.tool_calls as tool_calls


@traceable(name="wrap_openai_chat Main")
def wrap_openai_chat_main():
    """Run all wrap_openai chat completion examples."""
    print("=== Running wrap_openai Chat Completion Examples ===\n")

    print("--- Message Example ---")
    message.main()

    print("\n--- Reasoning Example ---")
    reasoning.main()

    print("\n--- Streaming Example ---")
    streaming.main()

    print("\n--- Structured Outputs Example ---")
    structured_outputs.main()

    print("\n--- Tool Calls Example ---")
    tool_calls.main()

    print("\n--- Multimodal Example ---")
    multimodal.main()

    print("\n=== All wrap_openai Chat Completion Examples Complete ===")
    return {"status": "complete"}


def main():
    return wrap_openai_chat_main()


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    main()
