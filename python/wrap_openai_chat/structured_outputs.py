import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai
from pydantic import BaseModel

client = wrap_openai(openai.Client())


class Person(BaseModel):
    name: str
    age: int
    occupation: str
    hobbies: list[str]


@traceable(name="Chat Completion Structured Output")
def chat_completion_structured_output():
    """Chat completion with structured output."""
    response = client.beta.chat.completions.parse(
        model="gpt-5-2025-08-07",
        messages=[
            {
                "role": "user",
                "content": "Tell me about a fictional software engineer named Alice who is 28 years old.",
            },
        ],
        response_format=Person,
    )

    person = response.choices[0].message.parsed
    print(f"Structured output response: {person}")
    return response


def main():
    print("Running wrap_openai chat completion structured output example...")
    chat_completion_structured_output()
    return {"structured_output": "complete"}
