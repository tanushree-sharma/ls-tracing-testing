import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())


@traceable(name="Chat Completion Streaming")
def chat_completion_streaming():
    """Stream chat completion response."""
    print("Starting streaming...")

    stream = client.chat.completions.create(
        model="gpt-5-2025-08-07",
        messages=[
            {
                "role": "user",
                "content": "Write a short poem about artificial intelligence.",
            },
        ],
        stream=True,
    )

    for chunk in stream:
        content = (
            chunk.choices[0].delta.content if chunk.choices[0].delta.content else ""
        )
        if content:
            print(content, end="", flush=True)

    print("\n\nStreaming complete!")
    return {"streaming": "complete"}


def main():
    print("Running wrap_openai chat completion streaming example...")
    chat_completion_streaming()
    return {"streaming": "complete"}
