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
        serverside_tools,
        streaming,
        structured_outputs,
        tool_calls,
    )
except ImportError:
    import wrap_openai_responses.message as message
    import wrap_openai_responses.multimodal as multimodal
    import wrap_openai_responses.reasoning as reasoning
    import wrap_openai_responses.serverside_tools as serverside_tools
    import wrap_openai_responses.streaming as streaming
    import wrap_openai_responses.structured_outputs as structured_outputs
    import wrap_openai_responses.tool_calls as tool_calls


@traceable(name="wrap_openai_responses Main")
def wrap_openai_responses_main():
    """Run all wrap_openai responses API examples."""
    print("=== Running wrap_openai Responses API Examples ===\n")

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

    print("\n--- Server-Side Tools Example ---")
    serverside_tools.main()

    print("\n=== All wrap_openai Responses API Examples Complete ===")
    return {"status": "complete"}


def main():
    return wrap_openai_responses_main()


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    main()
