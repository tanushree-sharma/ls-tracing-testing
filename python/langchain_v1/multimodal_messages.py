import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from helpers import fetch_pdf_base64
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
                {"type": "text", "text": "Hello, how are you?"},
                {
                    "type": "image",
                    "url": "https://fastly.picsum.photos/id/237/200/300.jpg?hmac=TmmQSbShHz9CdQm0NkEjx1Dyh_Y984R9LpNrpvH2D_U",
                },
            ]
        )
    ]

    response = model.invoke(messages)
    print(f"Image input response: {response.content[:100]}...")
    return response


@traceable(name="LangChain v1 PDF Input")
def pdf_input_example():
    """PDF input using content_blocks."""
    model = init_chat_model("gpt-4o", model_provider="openai", output_version="v1")

    pdf_url = "https://pdfobject.com/pdf/sample.pdf"
    pdf_base64 = fetch_pdf_base64(pdf_url)

    inputs = {
        "role": "user",
        "content": [
            {"type": "text", "text": "Describe the content of this document."},
            {
                "type": "file",
                "base64": pdf_base64,
                "mime_type": "application/pdf",
            },
        ],
    }

    response = model.invoke([inputs])
    print(f"PDF input response: {response.content[:100]}...")
    return response


def main():
    print("Running LangChain v1 multimodal messages examples...")
    image_input_example()
    pdf_input_example()
    return {"multimodal_messages": "complete"}
