import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from helpers import read_local_pdf_base64
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langsmith import traceable


@traceable(name="OpenAI Image Input")
def image_input_example(output_version: str = "v1", use_responses_api: bool = False):
    """Image input using content_blocks."""
    model = init_chat_model(
        "gpt-4o",
        model_provider="openai",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )

    messages = [
        HumanMessage(
            content_blocks=[
                {"type": "text", "text": "what is in this image?"},
                {
                    "type": "image",
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
            ]
        )
    ]

    response = model.invoke(messages)
    print(f"Image input response: {response.content[:100]}...")
    return response


@traceable(name="OpenAI PDF base64")
def pdf_input_example(output_version: str = "v1", use_responses_api: bool = True):
    """PDF input using content_blocks."""
    model = init_chat_model(
        "gpt-5-mini",
        model_provider="openai",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )

    pdf_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "resources",
        "Milwaukee Art Museum Summary.pdf",
    )
    pdf_base64 = read_local_pdf_base64(pdf_path)

    inputs = {
        "role": "user",
        "content": [
            {"type": "text", "text": "Describe the content of this document."},
            {
                "type": "file",
                "base64": pdf_base64,
                "mime_type": "application/pdf",
                "filename": "milwaukeeArtMuseum.pdf",
            },
        ],
    }

    response = model.invoke([inputs])
    print(f"PDF input response: {response.content[:100]}...")
    return response


@traceable(name="OpenAI PDF url")
def pdf_url_example(output_version: str = "v1", use_responses_api: bool = True):
    """PDF input using content_blocks."""
    model = init_chat_model(
        "gpt-5-mini",
        model_provider="openai",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )

    inputs = {
        "role": "user",
        "content": [
            {"type": "text", "text": "Describe the content of this document."},
            {
                "type": "file",
                "url": "https://drive.google.com/uc?export=download&id=1m0_e3dOKrbLY3VNjnTehQ3hR-4t5V4FB",
            },
        ],
    }

    response = model.invoke([inputs])
    print(f"PDF input response: {response.content[:100]}...")
    return response


@traceable(name="Anthropic Image Input Base64")
def image_base64_anthropic_example(output_version: str = "v1"):
    """Image input as base64 with Anthropic."""
    model = init_chat_model(
        "claude-sonnet-4-20250514",
        model_provider="anthropic",
        output_version=output_version,
    )

    messages = [
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

    response = model.invoke(messages)
    print(f"Image base64 Anthropic response: {response.content[:100]}...")
    return response


@traceable(name="Anthropic PDF Input Base64")
def pdf_base64_anthropic_example(output_version: str = "v1"):
    """PDF input as base64 with Anthropic."""
    model = init_chat_model(
        "claude-sonnet-4-20250514",
        model_provider="anthropic",
        output_version=output_version,
        use_responses_api=True,
    )

    pdf_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "resources",
        "Milwaukee Art Museum Summary.pdf",
    )
    pdf_base64 = read_local_pdf_base64(pdf_path)

    print(f"PDF base64: {pdf_base64}")
    inputs = {
        "role": "user",
        "content": [
            {"type": "text", "text": "Describe the content of this document."},
            {
                "type": "file",
                "base64": f"{pdf_base64}",
                "mime_type": "application/pdf",
                "filename": "milwaukeeArtMuseum.pdf",
            },
        ],
    }

    response = model.invoke([inputs])
    print(f"PDF base64 Anthropic response: {response.content[:100]}...")
    return response


@traceable
def main(output_version: str = "v1", use_responses_api: bool = False, run_tree=None):
    if run_tree:
        api_suffix = " + Responses API" if use_responses_api else ""
        run_tree.name = f"LangChain Multimodal messages ({output_version}{api_suffix})"
    print("Running LangChain v1 multimodal messages examples...")
    image_input_example(output_version, use_responses_api)
    pdf_input_example(output_version, use_responses_api)
    if use_responses_api:
        pdf_url_example(output_version, use_responses_api)
        return {"multimodal_messages": "complete"}
    image_base64_anthropic_example(output_version)
    pdf_base64_anthropic_example(output_version)
    return {"multimodal_messages": "complete"}
