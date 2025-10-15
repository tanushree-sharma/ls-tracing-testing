import anthropic
from langsmith import traceable
from langsmith.wrappers import wrap_anthropic

client = wrap_anthropic(anthropic.Anthropic())


@traceable(name="Streaming Message")
def streaming_message():
    """Stream a message response."""
    print("Starting streaming...")

    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": "Write a short poem about artificial intelligence.",
            }
        ],
    ) as stream:
        for text in stream.text_stream:
            print(text, end="", flush=True)

    print("\n\nStreaming complete!")
    return stream.get_final_message()


def main():
    print("Running wrap_anthropic streaming example...")
    streaming_message()
    return {"streaming": "complete"}
