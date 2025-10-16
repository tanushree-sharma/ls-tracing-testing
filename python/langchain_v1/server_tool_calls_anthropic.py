import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import anthropic
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langsmith import traceable

thinking = {"type": "enabled", "budget_tokens": 2000}


@traceable(name="Anthropic Reasoning")
def reasoning_example():
    """Reasoning/thinking with Anthropic."""
    model = init_chat_model(
        "anthropic:claude-sonnet-4-20250514", output_version="v1", thinking=thinking
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


@traceable(name="Anthropic Files API")
def files_api_example():
    """Files API with Anthropic."""
    client = anthropic.Anthropic()

    # Upload a file
    try:
        with open("/Users/erichan/ls-tracing-testing/python/document.pdf", "rb") as f:
            file = client.beta.files.upload(file=("document.pdf", f, "application/pdf"))

        model = init_chat_model(
            "anthropic:claude-sonnet-4-20250514",
            output_version="v1",
            thinking=thinking,
            betas=["files-api-2025-04-14"],
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


@traceable(name="Anthropic Citations")
def citations_example():
    """Citations with Anthropic."""
    model = init_chat_model("anthropic:claude-sonnet-4-20250514", output_version="v1")

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "document",
                    "source": {
                        "type": "text",
                        "media_type": "text/plain",
                        "data": "The grass is green. The sky is blue.",
                    },
                    "title": "My Document",
                    "context": "This is a trustworthy document.",
                    "citations": {"enabled": True},
                },
                {"type": "text", "text": "What color is the grass and sky?"},
            ],
        }
    ]

    response = model.invoke(messages)
    print(f"Citations response: {response.content[:100]}...")
    return response


@traceable(name="Anthropic Code Execution")
def code_execution_example():
    """Code execution with Anthropic."""
    model = init_chat_model(
        "anthropic:claude-sonnet-4-20250514",
        output_version="v1",
        thinking=thinking,
        betas=["code-execution-2025-08-25"],
    )

    tool = {"type": "code_execution_20250825", "name": "code_execution"}
    llm_with_tools = model.bind_tools([tool])

    response = llm_with_tools.invoke(
        "Calculate the fibonacci sequence up to 10 terms using Python."
    )
    print(f"Code execution response: {response}")
    return response


@traceable(name="Anthropic Web Fetch")
def web_fetch_example():
    """Web fetch with Anthropic."""
    model = init_chat_model(
        "anthropic:claude-sonnet-4-20250514",
        output_version="v1",
        thinking=thinking,
        betas=["web-fetch-2025-09-10"],
    )

    tool = {"type": "web_fetch_20250910", "name": "web_fetch", "max_uses": 3}
    llm_with_tools = model.bind_tools([tool])

    response = llm_with_tools.invoke(
        "Fetch and summarize the content from https://www.anthropic.com/new"
    )
    print(f"Web fetch response: {response}")
    return response


@traceable(name="LangChain v1 Anthropic server tool calls")
def main():
    print("Running LangChain v1 Anthropic server tool calls examples...")
    reasoning_example()
    files_api_example()
    citations_example()
    code_execution_example()
    web_fetch_example()
    return {"multimodal_anthropic": "complete"}
