import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai
from pydantic import BaseModel

client = wrap_openai(openai.Client())


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


@traceable(name="Responses API Structured Output")
def responses_api_structured_output():
    """Responses API with structured output."""
    response = client.responses.parse(
        model="gpt-5-2025-08-07",
        input=[
            {"role": "system", "content": "Extract the event information."},
            {
                "role": "user",
                "content": "Alice and Bob are going to a science fair on Friday.",
            },
        ],
        text_format=CalendarEvent,
    )

    event = response.output_parsed
    print(f"Structured output response: {event}")
    return response


def main():
    print("Running wrap_openai responses API structured output example...")
    responses_api_structured_output()
    return {"structured_output": "complete"}
