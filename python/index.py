from dotenv import load_dotenv
from langsmith import traceable

# Load environment variables
load_dotenv()

from langchain_v1.main import langchain_v1_main
from wrap_anthropic.main import wrap_anthropic_main
from wrap_openai_chat.main import wrap_openai_chat_main
from wrap_openai_responses.main import wrap_openai_responses_main


@traceable(name="Python Tracing Main")
def main():
    """Run all Python tracing examples."""
    print("=== Starting Python Tracing Examples ===\n")

    print("\n" + "=" * 60)
    print("WRAP_ANTHROPIC")
    print("=" * 60 + "\n")
    try:
        wrap_anthropic_main()
    except Exception as e:
        print(f"Error in wrap_anthropic: {e}")

    print("\n" + "=" * 60)
    print("WRAP_OPENAI_CHAT")
    print("=" * 60 + "\n")
    try:
        wrap_openai_chat_main()
    except Exception as e:
        print(f"Error in wrap_openai_chat: {e}")

    print("\n" + "=" * 60)
    print("WRAP_OPENAI_RESPONSES")
    print("=" * 60 + "\n")
    try:
        wrap_openai_responses_main()
    except Exception as e:
        print(f"Error in wrap_openai_responses: {e}")

    print("\n" + "=" * 60)
    print("LANGCHAIN_V1")
    print("=" * 60 + "\n")
    try:
        langchain_v1_main()
    except Exception as e:
        print(f"Error in langchain_v1: {e}")

    print("\n" + "=" * 60)
    print("=== All Python Tracing Examples Complete ===")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
