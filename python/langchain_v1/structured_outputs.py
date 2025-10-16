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
def structured_output_openai():
    """Structured output with OpenAI."""
    model = init_chat_model("gpt-4.1", model_provider="openai", output_version="v1")

    model_with_structure = model.with_structured_output(Movie, include_raw=True)
    response = model_with_structure.invoke("Provide details about the movie Inception")

    print(f"OpenAI structured output: {response['parsed']}")
    return response


@traceable(name="Anthropic Structured Output")
def structured_output_anthropic():
    """Structured output with Anthropic."""
    model = init_chat_model("anthropic:claude-3-7-sonnet-latest", output_version="v1")

    model_with_structure = model.with_structured_output(Movie, include_raw=True)
    response = model_with_structure.invoke("Provide details about the movie Inception")

    print(f"Anthropic structured output: {response['parsed']}")
    return response


@traceable(name="LangChain v1 Structured Outputs")
def main():
    print("Running LangChain v1 structured output examples...")
    structured_output_openai()
    structured_output_anthropic()
    return {"structured_output": "complete"}
