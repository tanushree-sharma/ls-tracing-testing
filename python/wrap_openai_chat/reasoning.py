import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())


@traceable(name="Chat Completion Reasoning")
def chat_completion_reasoning():
    """Chat completion with reasoning model."""
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[
            {
                "role": "user",
                "content": "What is the capital of France?",
            },
        ],
        reasoning_effort="high",
    )

    response_message = response.choices[0].message
    print(f"Reasoning response: {response_message.content}")
    return response


def main():
    print("Running wrap_openai chat completion reasoning example...")
    chat_completion_reasoning()
    return {"reasoning": "complete"}
