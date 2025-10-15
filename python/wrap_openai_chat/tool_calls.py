import json

import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "The temperature unit to use",
                    },
                },
                "required": ["location"],
            },
        },
    },
]


def get_weather(location: str, unit: str = "fahrenheit"):
    """Mock weather function."""
    return json.dumps(
        {
            "location": location,
            "temperature": "22" if unit == "celsius" else "72",
            "unit": unit,
            "forecast": "sunny",
        }
    )


@traceable(name="Chat Completion Tool Calls")
def chat_completion_tool_calls():
    """Chat completion with tool calls."""
    messages = [
        {
            "role": "user",
            "content": "What's the weather like in San Francisco?",
        },
    ]

    response = client.chat.completions.create(
        model="gpt-5-2025-08-07",
        messages=messages,
        tools=tools,
    )

    response_message = response.choices[0].message
    messages.append(response_message)

    tool_calls = response_message.tool_calls

    if tool_calls:
        for tool_call in tool_calls:
            function_args = json.loads(tool_call.function.arguments)

            function_response = ""
            if tool_call.function.name == "get_weather":
                function_response = get_weather(
                    function_args.get("location", ""),
                    function_args.get("unit", "fahrenheit"),
                )

            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": function_response,
                }
            )

        second_response = client.chat.completions.create(
            model="gpt-5-2025-08-07",
            messages=messages,
        )

        print(f"Tool call response: {second_response.choices[0].message.content}")
        return second_response

    return response


def main():
    print("Running wrap_openai chat completion tool calls example...")
    chat_completion_tool_calls()
    return {"tool_calls": "complete"}
