import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from langchain.chat_models import init_chat_model
from langsmith import traceable
from pydantic import BaseModel, Field


class Movie(BaseModel):
    """A movie with details."""

    title: str = Field(..., description="The title of the movie")
    year: int = Field(..., description="The year the movie was released")
    director: str = Field(..., description="The director of the movie")
    rating: float = Field(..., description="The movie's rating out of 10")


@traceable(name="OpenAI Structured Output")
def structured_output_openai(
    output_version: str = "v1", use_responses_api: bool = False
):
    """Structured output with OpenAI."""
    model = init_chat_model(
        "gpt-4.1",
        model_provider="openai",
        output_version=output_version,
        use_responses_api=use_responses_api,
    )

    model_with_structure = model.with_structured_output(Movie, include_raw=True)
    response = model_with_structure.invoke("Provide details about the movie Inception")

    print(f"OpenAI structured output: {response['parsed']}")
    return response


@traceable(name="Anthropic Structured Output")
def structured_output_anthropic(output_version: str = "v1"):
    """Structured output with Anthropic."""
    model = init_chat_model(
        "anthropic:claude-3-7-sonnet-latest", output_version=output_version
    )

    model_with_structure = model.with_structured_output(Movie, include_raw=True)
    response = model_with_structure.invoke("Provide details about the movie Inception")

    print(f"Anthropic structured output: {response['parsed']}")
    return response


@traceable
def main(output_version: str = "v1", use_responses_api: bool = False, run_tree=None):
    if run_tree:
        api_suffix = " + Responses API" if use_responses_api else ""
        run_tree.name = f"LangChain Structured Outputs ({output_version}{api_suffix})"
    print("Running LangChain v1 structured output examples...")
    structured_output_openai(output_version, use_responses_api)
    if not use_responses_api:
        structured_output_anthropic(output_version)
    return {"structured_output": "complete"}
