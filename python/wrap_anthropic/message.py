import anthropic
from langsmith import traceable
from langsmith.wrappers import wrap_anthropic

client = wrap_anthropic(anthropic.Anthropic())


@traceable(name="Normal Message")
def normal_message():
    """Simple text message."""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        messages=[
            {
                "role": "user",
                "content": "Question: Can you summarize this morning's meetings?\nContext: During this morning's meeting, we solved all world conflict.",
            }
        ],
        max_tokens=1024,
        system="You are a helpful assistant. Please respond to the user's request only based on the given context.",
    )
    print(f"Normal message response: {response.content[0].text[:100]}...")
    return response


@traceable(name="Extended Thinking Message")
def extended_thinking_message():
    """Message with extended thinking enabled."""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        messages=[
            {
                "role": "user",
                "content": "What is the meaning of life? Think deeply about this.",
            }
        ],
        max_tokens=4096,
        thinking={"type": "enabled", "budget_tokens": 2000},
    )
    print(f"Extended thinking response: {response.content[-1].text[:100]}...")
    return response


def main():
    print("Running wrap_anthropic message examples...")
    normal_message()
    extended_thinking_message()
    return {"normal": "complete", "thinking": "complete"}
