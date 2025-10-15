import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())


@traceable(name="Responses API Reasoning")
def responses_api_reasoning():
    """Responses API with reasoning."""
    response = client.responses.create(
        model="gpt-5",
        input="What is the meaning of life? Think deeply about this.",
        reasoning={"effort": "high"},
    )

    print(f"Reasoning response: {response.output_text[:100]}...")
    return response


def main():
    print("Running wrap_openai responses API reasoning example...")
    responses_api_reasoning()
    return {"reasoning": "complete"}
