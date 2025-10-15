from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langsmith import traceable

reasoning = {
    "effort": "medium",
    "summary": "auto",
}


@traceable(name="LangChain v1 OpenAI Reasoning")
def reasoning_example():
    """Reasoning with OpenAI."""
    model = init_chat_model(
        "openai:gpt-5-nano", output_version="v1", reasoning=reasoning
    )

    inputs = [
        HumanMessage(
            content_blocks=[
                {"type": "text", "text": "What is in this image?"},
                {
                    "type": "image",
                    "url": "https://fastly.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U",
                },
            ]
        )
    ]

    response = model.invoke(inputs)
    print(f"Reasoning response: {response.content[:100]}...")
    return response


@traceable(name="LangChain v1 OpenAI Web Search")
def web_search_example():
    """Web search with OpenAI."""
    model = init_chat_model("openai:gpt-4.1-mini", output_version="v1")

    tool = {"type": "web_search"}
    model_with_tools = model.bind_tools([tool])

    response = model_with_tools.invoke("What was a positive news story from today?")
    print(f"Web search response: {response}")
    return response


@traceable(name="LangChain v1 OpenAI Image Generation")
def image_generation_example():
    """Image generation with OpenAI."""
    model = init_chat_model("openai:gpt-4.1-mini", output_version="v1")

    tool = {"type": "image_generation", "quality": "low"}
    llm_with_tools = model.bind_tools([tool])

    response = llm_with_tools.invoke(
        "Draw a picture of a cute fuzzy cat with an umbrella"
    )
    print(f"Image generation response: {response}")
    return response


@traceable(name="LangChain v1 OpenAI Code Interpreter")
def code_interpreter_example():
    """Code interpreter with OpenAI."""
    model = init_chat_model("openai:gpt-4.1-mini", output_version="v1")

    llm_with_tools = model.bind_tools(
        [
            {
                "type": "code_interpreter",
                "container": {"type": "auto"},
            }
        ]
    )

    response = llm_with_tools.invoke(
        "Write and run code to answer the question: what is 3^3?"
    )
    print(f"Code interpreter response: {response}")
    return response


def main():
    print("Running LangChain v1 OpenAI multimodal examples...")
    reasoning_example()
    web_search_example()
    image_generation_example()
    code_interpreter_example()
    return {"multimodal_openai": "complete"}
