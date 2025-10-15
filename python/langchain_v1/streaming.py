from langchain.chat_models import init_chat_model
from langsmith import traceable


@traceable(name="LangChain v1 Streaming")
def streaming_example():
    """Stream LangChain v1 response."""
    model = init_chat_model("gpt-4o", model_provider="openai", output_version="v1")

    print("Starting streaming...")
    for chunk in model.stream("Write a short poem about artificial intelligence."):
        print(chunk.content, end="", flush=True)

    print("\n\nStreaming complete!")
    return {"streaming": "complete"}


def main():
    print("Running LangChain v1 streaming example...")
    streaming_example()
    return {"streaming": "complete"}
