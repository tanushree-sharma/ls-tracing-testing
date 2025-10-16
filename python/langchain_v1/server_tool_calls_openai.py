import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langsmith import traceable
from openai import OpenAI

reasoning = {
    "effort": "medium",
    "summary": "auto",
}


@traceable(name="OpenAI Reasoning")
def reasoning_example(output_version: str = "v1", use_responses_api: bool = False):
    """Reasoning with OpenAI."""
    model = init_chat_model(
        "openai:gpt-5-nano",
        output_version=output_version,
        use_responses_api=use_responses_api,
        reasoning=reasoning,
    )

    inputs = [
        HumanMessage(
            content_blocks=[
                {"type": "text", "text": "What is in this image?"},
                {
                    "type": "image",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            ]
        )
    ]

    response = model.invoke(inputs)
    print(f"Reasoning response: {response.content[:100]}...")
    return response


@traceable(name="OpenAI Files API")
def files_api_example(output_version: str = "v1", use_responses_api: bool = False):
    """Files API with OpenAI."""
    client = OpenAI()

    try:
        with open("/Users/erichan/ls-tracing-testing/python/document.pdf", "rb") as f:
            file = client.files.create(file=f, purpose="assistants")

        model = init_chat_model(
            "openai:gpt-4.1-mini",
            output_version=output_version,
            use_responses_api=use_responses_api,
        )

        input_message = {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this document."},
                {"type": "file", "file_id": file.id},
            ],
        }

        response = model.invoke([input_message])
        print(f"Files API response: {response.content[:100]}...")
        return response
    except Exception as e:
        print(f"Files API example skipped: {e}")
        return None


@traceable(name="OpenAI Web Search")
def web_search_example(output_version: str = "v1", use_responses_api: bool = False):
    """Web search with OpenAI."""
    model = init_chat_model(
        "openai:gpt-4.1-mini",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )

    tool = {"type": "web_search"}
    model_with_tools = model.bind_tools([tool])

    response = model_with_tools.invoke("What was a positive news story from today?")
    print(f"Web search response: {response}")
    return response


@traceable(name="OpenAI Image Generation")
def image_generation_example(
    output_version: str = "v1", use_responses_api: bool = False
):
    """Image generation with OpenAI."""
    model = init_chat_model(
        "openai:gpt-4.1-mini",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )

    tool = {"type": "image_generation", "quality": "low"}
    llm_with_tools = model.bind_tools([tool])

    response = llm_with_tools.invoke(
        "Draw a picture of a cute fuzzy cat with an umbrella"
    )
    print(f"Image generation response: {response}")
    return response


@traceable(name="OpenAI Code Interpreter")
def code_interpreter_example(
    output_version: str = "v1", use_responses_api: bool = False
):
    """Code interpreter with OpenAI."""
    model = init_chat_model(
        "openai:gpt-4.1-mini",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )

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


@traceable
def main(output_version: str = "v1", use_responses_api: bool = False, run_tree=None):
    if run_tree:
        api_suffix = " + Responses API" if use_responses_api else ""
        run_tree.name = (
            f"LangChain OpenAI server tool calls ({output_version}{api_suffix})"
        )
    print("Running LangChain v1 OpenAI server tool calls examples...")
    if use_responses_api:
        reasoning_example(output_version, use_responses_api)
        files_api_example(output_version, use_responses_api)
        web_search_example(output_version, use_responses_api)
        image_generation_example(output_version, use_responses_api)
        code_interpreter_example(output_version, use_responses_api)
    return {"multimodal_openai": "complete"}
