import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import anthropic
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langsmith import traceable

thinking = {"type": "enabled", "budget_tokens": 2000}


@traceable(name="LangChain v1 Anthropic Reasoning")
def reasoning_example():
    """Reasoning/thinking with Anthropic."""
    model = init_chat_model(
        "anthropic:claude-3-7-sonnet-latest", output_version="v1", thinking=thinking
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


@traceable(name="LangChain v1 Anthropic Files API")
def files_api_example():
    """Files API with Anthropic."""
    client = anthropic.Anthropic()

    # Upload a file
    try:
        with open("/Users/erichan/ls-tracing-testing/python/document.pdf", "rb") as f:
            file = client.beta.files.upload(file=("document.pdf", f, "application/pdf"))

        model = init_chat_model(
            "anthropic:claude-3-7-sonnet-latest",
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


@traceable(name="LangChain v1 Anthropic Citations")
def citations_example():
    """Citations with Anthropic."""
    model = init_chat_model("anthropic:claude-3-7-sonnet-latest", output_version="v1")

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


@traceable(name="LangChain v1 Anthropic Web Fetch")
def web_fetch_example():
    """Web fetch with Anthropic."""
    model = init_chat_model(
        "anthropic:claude-3-7-sonnet-latest",
        output_version="v1",
        thinking=thinking,
        betas=["web-fetch-2025-09-10"],
    )

    tool = {"type": "web_fetch_20250910", "name": "web_fetch", "max_uses": 3}
    llm_with_tools = model.bind_tools([tool])

    response = llm_with_tools.invoke(
        "Please analyze the content at https://example.com/article"
    )
    print(f"Web fetch response: {response}")
    return response


def main():
    print("Running LangChain v1 Anthropic multimodal examples...")
    reasoning_example()
    files_api_example()
    citations_example()
    web_fetch_example()
    return {"multimodal_anthropic": "complete"}
