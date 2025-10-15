import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import openai
from helpers import fetch_image_base64, fetch_pdf_base64
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())


@traceable(name="Responses API Image URL")
def image_url_example():
    """Image input using URL."""
    response = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Come up with keywords related to the image, and search on the web using the search tool for any news related to the keywords, summarize the findings and cite the sources.",
                    },
                    {
                        "type": "input_image",
                        "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/Cat_August_2010-4.jpg/2880px-Cat_August_2010-4.jpg",
                    },
                ],
            }
        ],
        tools=[{"type": "web_search"}],
    )

    print(f"Image URL response: {response.output_text[:100]}...")
    return response


@traceable(name="Responses API Image Base64")
def image_base64_example():
    """Image input using base64."""
    image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg"
    image_data = fetch_image_base64(image_url)

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "what's in this image?"},
                    {
                        "detail": "auto",
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{image_data}",
                    },
                ],
            }
        ],
    )

    print(f"Image base64 response: {response.output_text[:100]}...")
    return response


@traceable(name="Responses API PDF Base64")
def pdf_base64_example():
    """PDF input using base64."""
    pdf_url = "https://pdfobject.com/pdf/sample.pdf"
    pdf_data = fetch_pdf_base64(pdf_url)

    response = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": "what's in this pdf?"},
                    {
                        "type": "input_file",
                        "filename": "sample.pdf",
                        "file_data": f"data:application/pdf;base64,{pdf_data}",
                    },
                ],
            }
        ],
    )

    print(f"PDF response: {response.output_text[:100]}...")
    return response


def main():
    print("Running wrap_openai responses API multimodal examples...")
    image_url_example()
    image_base64_example()
    pdf_base64_example()
    return {"multimodal": "complete"}
