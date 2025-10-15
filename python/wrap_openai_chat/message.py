import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())


@traceable(name="Chat Completion Message")
def chat_completion_message():
    """Simple chat completion message."""
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": "What is the capital of France?",
            },
        ],
    )

    response_message = response.choices[0].message
    print(f"Chat completion response: {response_message.content}")
    return response


def main():
    print("Running wrap_openai chat completion message example...")
    chat_completion_message()
    return {"message": "complete"}
