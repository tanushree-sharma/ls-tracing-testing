import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())


@traceable(name="Responses API Message")
def responses_api_message():
    """Simple responses API message."""
    response = client.responses.create(
        model="gpt-4.1", input="Tell me a three sentence bedtime story about a unicorn."
    )

    print(f"Responses API output: {response.output_text}")
    return response


def main():
    print("Running wrap_openai responses API message example...")
    responses_api_message()
    return {"message": "complete"}
