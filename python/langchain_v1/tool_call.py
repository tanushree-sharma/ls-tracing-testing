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


@traceable(name="LangChain v1 Tool Call - OpenAI")
def tool_call_openai():
    """Tool call with OpenAI."""
    model = init_chat_model("gpt-4.1", model_provider="openai", output_version="v1")

    tools = [Add, Multiply]
    llm_with_tools = model.bind_tools(tools)

    query = "What is 3 * 12? Please use the tools to answer the question."
    response = llm_with_tools.invoke(query)

    print(f"OpenAI tool call response: {response}")
    return response


@traceable(name="LangChain v1 Tool Call - Anthropic")
def tool_call_anthropic():
    """Tool call with Anthropic."""
    model = init_chat_model("anthropic:claude-3-7-sonnet-latest", output_version="v1")

    model_with_tools = model.bind_tools([get_weather])
    response = model_with_tools.invoke("What's the weather like in Boston?")

    print(f"Anthropic tool call response: {response}")
    return response


@traceable(name="LangChain v1 Tool Message")
def tool_message_example():
    """Tool message example."""
    model = init_chat_model("gpt-4.1", model_provider="openai", output_version="v1")

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


def main():
    print("Running LangChain v1 tool call examples...")
    tool_call_openai()
    tool_call_anthropic()
    tool_message_example()
    return {"tool_call": "complete"}
