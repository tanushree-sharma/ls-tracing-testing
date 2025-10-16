from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, SystemMessage
from langsmith import traceable


@traceable(name="OpenAI Message")
def message_openai():
    """Simple message with OpenAI."""
    model = init_chat_model("gpt-5-mini", model_provider="openai", output_version="v1")
    messages = [
        SystemMessage(content="Translate the following from English into Italian"),
        HumanMessage(content="hi!"),
    ]

    response = model.invoke(messages)
    print(f"OpenAI response: {response.content}")
    return response


@traceable(name="Anthropic Message")
def message_anthropic():
    """Simple message with Anthropic."""
    model = init_chat_model("anthropic:claude-3-7-sonnet-latest", output_version="v1")
    messages = [HumanMessage(content="Why do parrots talk?")]

    response = model.invoke(messages)
    print(f"Anthropic response: {response.content}")
    return response


@traceable(name="LangChain v1 Simple messages")
def main():
    print("Running LangChain v1 message examples...")
    message_openai()
    message_anthropic()
    return {"message": "complete"}
