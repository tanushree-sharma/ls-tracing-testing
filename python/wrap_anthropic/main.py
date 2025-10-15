import os
import sys

# Add parent directory to path for direct execution
if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from langsmith import traceable

# Use try/except to handle both direct execution and module import
try:
    from . import (
        citations,
        image_input,
        message,
        pdf_input,
        serverside_tools,
        streaming,
        structured_outputs,
        tool_call,
    )
except ImportError:
    import wrap_anthropic.citations as citations
    import wrap_anthropic.image_input as image_input
    import wrap_anthropic.message as message
    import wrap_anthropic.pdf_input as pdf_input
    import wrap_anthropic.serverside_tools as serverside_tools
    import wrap_anthropic.streaming as streaming
    import wrap_anthropic.structured_outputs as structured_outputs
    import wrap_anthropic.tool_call as tool_call


@traceable(name="wrap_anthropic Main")
def wrap_anthropic_main():
    """Run all wrap_anthropic examples."""
    print("=== Running wrap_anthropic Examples ===\n")

    print("--- Message Example ---")
    message.main()

    print("\n--- Streaming Example ---")
    streaming.main()

    print("\n--- Tool Call Example ---")
    tool_call.main()

    print("\n--- Structured Outputs Example ---")
    structured_outputs.main()

    print("\n--- Image Input Example ---")
    image_input.main()

    print("\n--- PDF Input Example ---")
    pdf_input.main()

    print("\n--- Citations Example ---")
    citations.main()

    print("\n--- Server-Side Tools Example ---")
    serverside_tools.main()

    print("\n=== All wrap_anthropic Examples Complete ===")
    return {"status": "complete"}


def main():
    return wrap_anthropic_main()


if __name__ == "__main__":
    from dotenv import load_dotenv

    load_dotenv()
    main()
