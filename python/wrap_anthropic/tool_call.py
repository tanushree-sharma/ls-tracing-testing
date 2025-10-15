import anthropic
from langsmith import traceable
from langsmith.wrappers import wrap_anthropic

client = wrap_anthropic(anthropic.Anthropic())


@traceable(name="Tool Call")
def tool_call_example():
    """Example of calling tools."""
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        tools=[
            {
                "name": "get_weather",
                "description": "Get the current weather in a given location",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "The city and state, e.g. San Francisco, CA",
                        }
                    },
                    "required": ["location"],
                },
            }
        ],
        messages=[
            {"role": "user", "content": "What's the weather like in San Francisco?"}
        ],
    )

    if response.content and len(response.content) > 0:
        print(f"Tool call response: {response.content[0]}")
    return response


def main():
    print("Running wrap_anthropic tool call example...")
    tool_call_example()
    return {"tool_call": "complete"}
