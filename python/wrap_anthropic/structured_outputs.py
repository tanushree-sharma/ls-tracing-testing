import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import anthropic
from helpers import fetch_image_base64
from langsmith import traceable
from langsmith.wrappers import wrap_anthropic

client = wrap_anthropic(anthropic.Anthropic())


@traceable(name="Structured Output - JSON Mode")
def structured_output_example():
    """Example of structured outputs using JSON mode."""
    image_url = "https://upload.wikimedia.org/wikipedia/commons/a/a7/Camponotus_flavomarginatus_ant.jpg"
    image_data = fetch_image_base64(image_url)

    message = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        tools=[
            {
                "name": "record_summary",
                "description": "Record summary of an image using well-structured JSON.",
                "input_schema": {
                    "type": "object",
                    "properties": {
                        "key_colors": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "r": {
                                        "type": "number",
                                        "description": "red value [0.0, 1.0]",
                                    },
                                    "g": {
                                        "type": "number",
                                        "description": "green value [0.0, 1.0]",
                                    },
                                    "b": {
                                        "type": "number",
                                        "description": "blue value [0.0, 1.0]",
                                    },
                                    "name": {
                                        "type": "string",
                                        "description": "Human-readable color name in snake_case, e.g. 'olive_green' or 'turquoise'",
                                    },
                                },
                                "required": ["r", "g", "b", "name"],
                            },
                            "description": "Key colors in the image. Limit to less than four.",
                        },
                        "description": {
                            "type": "string",
                            "description": "Image description. One to two sentences max.",
                        },
                        "estimated_year": {
                            "type": "integer",
                            "description": "Estimated year that the image was taken, if it is a photo.",
                        },
                    },
                    "required": ["key_colors", "description"],
                },
            }
        ],
        tool_choice={"type": "tool", "name": "record_summary"},
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
                    {"type": "text", "text": "Describe this image."},
                ],
            }
        ],
    )

    print(f"Structured output: {message.content[0]}")
    return message


def main():
    print("Running wrap_anthropic structured outputs example...")
    structured_output_example()
    return {"structured_output": "complete"}
