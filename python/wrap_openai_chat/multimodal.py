import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import openai
from helpers import fetch_image_base64, fetch_pdf_base64
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())


@traceable(name="Chat Completion Image URL")
def image_url_example():
    """Image input using URL."""
    response = client.chat.completions.create(
        model="gpt-5-2025-08-07",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What's in this image?",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                        },
                    },
                ],
            },
        ],
    )

    print(f"Image URL response: {response.choices[0].message.content[:100]}...")
    return response


@traceable(name="Chat Completion Image Base64")
def image_base64_example():
    """Image input using base64."""
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
    image_data = fetch_image_base64(image_url)

    response = client.chat.completions.create(
        model="gpt-5-2025-08-07",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Describe this image in detail.",
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}",
                        },
                    },
                ],
            },
        ],
    )

    print(f"Image base64 response: {response.choices[0].message.content[:100]}...")
    return response


@traceable(name="Chat Completion PDF Base64")
def pdf_base64_example():
    """PDF input using base64."""
    pdf_url = "https://pdfobject.com/pdf/sample.pdf"
    pdf_data = fetch_pdf_base64(pdf_url)

    response = client.chat.completions.create(
        model="gpt-5-2025-08-07",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Please summarize this PDF document.",
                    },
                    {
                        "type": "file",
                        "file": {
                            "filename": "sample.pdf",
                            "file_data": f"data:application/pdf;base64,{pdf_data}",
                        },
                    },
                ],
            },
        ],
    )

    print(f"PDF response: {response.choices[0].message.content[:100]}...")
    return response


def main():
    print("Running wrap_openai chat completion multimodal examples...")
    image_url_example()
    image_base64_example()
    pdf_base64_example()
    return {"multimodal": "complete"}
