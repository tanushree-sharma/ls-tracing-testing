import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import anthropic
from helpers import fetch_image_base64
from langsmith import traceable
from langsmith.wrappers import wrap_anthropic

client = wrap_anthropic(anthropic.Anthropic())


@traceable(name="Image Input - Base64")
def image_input_base64():
    """Image input using base64 encoding."""
    image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
    image_data = fetch_image_base64(image_url)

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {
                            "type": "base64",
                            "media_type": "image/jpeg",
                            "data": image_data,
                        },
                    },
                    {"type": "text", "text": "What is in this image?"},
                ],
            }
        ],
    )

    print(f"Image base64 response: {response.content[0].text[:100]}...")
    return response


@traceable(name="Image Input - URL")
def image_input_url():
    """Image input using URL."""
    image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"

    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "image", "source": {"type": "url", "url": image_url}},
                    {"type": "text", "text": "What is in this image?"},
                ],
            }
        ],
    )

    print(f"Image URL response: {response.content[0].text[:100]}...")
    return response


def main():
    print("Running wrap_anthropic image input examples...")
    image_input_base64()
    image_input_url()
    return {"image_base64": "complete", "image_url": "complete"}
