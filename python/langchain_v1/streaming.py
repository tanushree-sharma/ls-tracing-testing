from langchain.chat_models import init_chat_model
from langsmith import traceable


@traceable(name="OpenAI Streaming")
def streaming_example_openai():
    """Stream LangChain v1 response with OpenAI."""
    model = init_chat_model("gpt-4o", model_provider="openai", output_version="v1")

    print("Starting OpenAI streaming...")
    for chunk in model.stream("Write a short poem about artificial intelligence."):
        print(chunk.content, end="", flush=True)

    print("\n\nOpenAI streaming complete!")
    return {"streaming": "complete"}


@traceable(name="Anthropic Streaming")
def streaming_example_anthropic():
    """Stream LangChain v1 response with Anthropic."""
    model = init_chat_model(
        "claude-3-5-sonnet-20241022", model_provider="anthropic", output_version="v1"
    )

    print("Starting Anthropic streaming...")
    for chunk in model.stream("Write a short poem about artificial intelligence."):
        print(chunk.content, end="", flush=True)

    print("\n\nAnthropic streaming complete!")
    return {"streaming": "complete"}


@traceable(name="LangChain v1 Streaming")
def main():
    print("Running LangChain v1 streaming examples...\n")
    streaming_example_openai()
    print("\n" + "=" * 50 + "\n")
    streaming_example_anthropic()
    return {"streaming": "complete"}
