import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import anthropic
from helpers import fetch_pdf_base64
from langsmith import traceable
from langsmith.wrappers import wrap_anthropic

client = wrap_anthropic(anthropic.Anthropic())


@traceable(name="Citations - Text/Plain")
def citations_text():
    """Citations with text/plain document."""
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
        ],
    )

    print(f"Text citations response: {response.content[0].text[:100]}...")
    return response


@traceable(name="Citations - PDF")
def citations_pdf():
    """Citations with PDF document."""
    pdf_url = "https://www.princexml.com/samples/invoice-colorful/invoicesample.pdf"
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
                        "title": "Invoice Document",
                        "context": "This is a trustworthy document.",
                        "citations": {"enabled": True},
                    },
                    {"type": "text", "text": "How much are Mangoes?"},
                ],
            }
        ],
    )

    print(f"PDF citations response: {response.content[0].text[:100]}...")
    return response


def main():
    print("Running wrap_anthropic citations examples...")
    citations_text()
    citations_pdf()
    return {"citations_text": "complete", "citations_pdf": "complete"}
