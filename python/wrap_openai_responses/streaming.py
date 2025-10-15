import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())


@traceable(name="Responses API Streaming")
def responses_api_streaming():
    """Stream responses API response."""
    print("Starting streaming...")

    stream = client.responses.create(
        model="gpt-5",
        input="Write a short poem about artificial intelligence in 4 lines.",
        stream=True,
    )

    for chunk in stream:
        if chunk.type == "response.output_text.delta":
            print(chunk.delta, end="", flush=True)

    print("\n\nStreaming complete!")
    return {"streaming": "complete"}


def main():
    print("Running wrap_openai responses API streaming example...")
    responses_api_streaming()
    return {"streaming": "complete"}
