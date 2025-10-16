import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, HumanMessage, ToolMessage
from langchain_core.tools import tool
from langsmith import traceable
from pydantic import BaseModel, Field


class Add(BaseModel):
    """Add two integers."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")


class Multiply(BaseModel):
    """Multiply two integers."""

    a: int = Field(..., description="First integer")
    b: int = Field(..., description="Second integer")


@tool
def get_weather(location: str) -> str:
    """Get the weather at a location."""
    return f"It's sunny in {location}."


@traceable(name="OpenAI Tool Call")
def tool_call_openai(output_version: str = "v1", use_responses_api: bool = False):
    """Tool call with OpenAI."""
    model = init_chat_model(
        "gpt-4.1",
        model_provider="openai",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )

    tools = [Add, Multiply]
    llm_with_tools = model.bind_tools(tools)

    query = "What is 3 * 12? Please use the tools to answer the question."
    response = llm_with_tools.invoke(query)

    print(f"OpenAI tool call response: {response}")
    return response


@traceable(name="Anthropic Tool Call")
def tool_call_anthropic(output_version: str = "v1"):
    """Tool call with Anthropic."""
    model = init_chat_model(
        "anthropic:claude-3-7-sonnet-latest", output_version=output_version
    )

    model_with_tools = model.bind_tools([get_weather])
    response = model_with_tools.invoke("What's the weather like in Boston?")

    print(f"Anthropic tool call response: {response}")
    return response


@traceable(name="OpenAI Tool Message")
def tool_message_example(output_version: str = "v1", use_responses_api: bool = False):
    """Tool message example."""
    model = init_chat_model(
        "gpt-4.1",
        model_provider="openai",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )

    # After a model makes a tool call
    ai_message = AIMessage(
        content=[],
        tool_calls=[
            {
                "name": "get_weather",
                "args": {"location": "San Francisco"},
                "id": "call_123",
            }
        ],
    )

    # Execute tool and create result message
    weather_result = "Sunny, 72°F"
    tool_message = ToolMessage(content=weather_result, tool_call_id="call_123")

    # Continue conversation
    messages = [
        HumanMessage("What's the weather in San Francisco?"),
        ai_message,
        tool_message,
    ]
    response = model.invoke(messages)

    print(f"Tool message response: {response.content}")
    return response


@traceable
def main(output_version: str = "v1", use_responses_api: bool = False, run_tree=None):
    if run_tree:
        api_suffix = " + Responses API" if use_responses_api else ""
        run_tree.name = f"LangChain Tool Call ({output_version}{api_suffix})"
    print("Running LangChain v1 tool call examples...")
    tool_call_openai(output_version, use_responses_api)
    tool_message_example(output_version, use_responses_api)
    if not use_responses_api:
        tool_call_anthropic(output_version)

    return {"tool_call": "complete"}
