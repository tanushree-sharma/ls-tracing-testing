import openai
from langsmith import traceable
from langsmith.wrappers import wrap_openai

client = wrap_openai(openai.Client())


@traceable(name="Server-Side Tool - Web Search")
def web_search_tool():
    """Example of web search tool."""
    response = client.responses.create(
        model="gpt-4o",
        input="What's the latest news about AI?",
        tools=[{"type": "web_search"}],
    )

    print(f"Web search response: {response.output_text[:100]}...")
    return response


@traceable(name="Server-Side Tool - Image Generation")
def image_generation_tool():
    """Example of image generation tool."""
    response = client.responses.create(
        model="gpt-5",
        input="Draw a picture of a cute fuzzy cat with an umbrella",
        tools=[{"type": "image_generation", "quality": "low"}],
    )

    print("Image generation response: Generated image")
    return response


@traceable(name="Server-Side Tool - Code Interpreter")
def code_interpreter_tool():
    """Example of code interpreter tool."""
    instructions = """
    You are a personal math tutor. When asked a math question, 
    write and run code using the python tool to answer the question.
    """

    response = client.responses.create(
        model="gpt-4.1",
        tools=[{"type": "code_interpreter", "container": {"type": "auto"}}],
        instructions=instructions,
        input="I need to solve the equation 3x + 11 = 14. Can you help me?",
    )

    print(f"Code interpreter response: {response.output_text[:100]}...")
    return response


@traceable(name="Server-Side Tool - MCP")
def mcp_tool():
    """Example of MCP (Model Context Protocol)."""
    try:
        response = client.responses.create(
            model="gpt-5",
            tools=[
                {
                    "type": "mcp",
                    "server_label": "dmcp",
                    "server_description": "A Dungeons and Dragons MCP server to assist with dice rolling.",
                    "server_url": "https://dmcp-server.deno.dev/sse",
                    "require_approval": "never",
                },
            ],
            input="Roll 2d4+1",
        )

        print(f"MCP response: {response.output_text}")
        return response
    except Exception as e:
        print(f"MCP example error: {e}")
        return None


def main():
    print("Running wrap_openai responses API server-side tools examples...")
    web_search_tool()
    image_generation_tool()
    code_interpreter_tool()
    mcp_tool()
    return {"serverside_tools": "complete"}
