import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import anthropic
from helpers import fetch_pdf_base64
from langsmith import traceable
from langsmith.wrappers import wrap_anthropic

client = wrap_anthropic(anthropic.Anthropic())


@traceable(name="PDF Input - Base64")
def pdf_input_base64():
    """PDF input using base64 encoding."""
    pdf_url = "https://pdfobject.com/pdf/sample.pdf"
    pdf_data = fetch_pdf_base64(pdf_url)

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": pdf_data,
                        },
                    },
                    {"type": "text", "text": "What is in this PDF?"},
                ],
            }
        ],
    )

    print(f"PDF base64 response: {response.content[0].text[:100]}...")
    return response


def main():
    print("Running wrap_anthropic PDF input example...")
    pdf_input_base64()
    return {"pdf_input": "complete"}
