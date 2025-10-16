import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from helpers import read_local_pdf_base64
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage
from langsmith import traceable


@traceable(name="LangChain v1 Image Input")
def image_input_example():
    """Image input using content_blocks."""
    model = init_chat_model("gpt-4o", model_provider="openai", output_version="v1")

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


@traceable(name="LangChain v1 PDF base64")
def pdf_input_example():
    """PDF input using content_blocks."""
    model = init_chat_model(
        "gpt-5-mini", model_provider="openai", output_version="responses/v1"
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


@traceable(name="LangChain v1 PDF url")
def pdf_url_example():
    """PDF input using content_blocks."""
    model = init_chat_model(
        "gpt-5-mini", model_provider="openai", output_version="responses/v1"
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


@traceable(name="LangChain v1 Image Input Base64 Anthropic")
def image_base64_anthropic_example():
    """Image input as base64 with Anthropic."""
    model = init_chat_model(
        "claude-sonnet-4-20250514", model_provider="anthropic", output_version="v1"
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


@traceable(name="LangChain v1 PDF Input Base64 Anthropic")
def pdf_base64_anthropic_example():
    """PDF input as base64 with Anthropic."""
    model = init_chat_model(
        "claude-sonnet-4-20250514", model_provider="anthropic", output_version="v1"
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


@traceable(name="LangChain v1 Multimodal messages")
def main():
    print("Running LangChain v1 multimodal messages examples...")
    image_input_example()
    pdf_input_example()
    pdf_url_example()
    image_base64_anthropic_example()
    pdf_base64_anthropic_example()
    return {"multimodal_messages": "complete"}
