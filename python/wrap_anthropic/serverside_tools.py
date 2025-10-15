import anthropic
from langsmith import traceable
from langsmith.wrappers import wrap_anthropic

client = wrap_anthropic(anthropic.Anthropic())


@traceable(name="Server-Side Tool - Web Search")
def web_search_tool():
    """Example of web search tool."""
    response = client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": "What's the weather in NYC?"}],
        tools=[{"type": "web_search_20250305", "name": "web_search", "max_uses": 5}],
    )

    print(
        f"Web search response: {response.content[-1] if response.content else 'No content'}"
    )
    return response


@traceable(name="Server-Side Tool - Code Execution")
def code_execution_tool():
    """Example of code execution tool."""
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        betas=["code-execution-2025-08-25"],
        max_tokens=4096,
        messages=[
            {
                "role": "user",
                "content": "Calculate the mean and standard deviation of [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]",
            }
        ],
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    )

    print(
        f"Code execution response: {response.content[-1] if response.content else 'No content'}"
    )
    return response


@traceable(name="Server-Side Tool - Files API")
def files_api_tool():
    """Example of Files API."""
    # Upload a file
    with open("/Users/erichan/ls-tracing-testing/python/Blog.jpg", "rb") as f:
        file_upload = client.beta.files.upload(file=("Blog.jpg", f, "image/jpeg"))

    # Use the uploaded file in a message
    message = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        betas=["files-api-2025-04-14"],
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "source": {"type": "file", "file_id": file_upload.id},
                    },
                    {"type": "text", "text": "Describe this image."},
                ],
            }
        ],
    )

    print(f"Files API response: {message.content[0].text[:100]}...")
    return message


@traceable(name="Server-Side Tool - MCP")
def mcp_tool():
    """Example of MCP (Model Context Protocol)."""
    try:
        response = client.beta.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1000,
            messages=[
                {"role": "user", "content": "Get the last 5 tickets from linear"}
            ],
            mcp_servers=[
                {
                    "type": "url",
                    "url": "https://mcp.linear.app/sse",
                    "name": "linear-mcp",
                    "authorization_token": "test_token",
                    "tool_configuration": {
                        "enabled": True,
                        "allowed_tools": ["list_issues", "get_issue"],
                    },
                }
            ],
            betas=["mcp-client-2025-04-04"],
        )

        print(
            f"MCP response: {response.content[0] if response.content else 'No content'}"
        )
        return response
    except Exception as e:
        print(f"MCP example skipped (requires valid token): {e}")
        return None


def main():
    print("Running wrap_anthropic server-side tools examples...")
    web_search_tool()
    code_execution_tool()
    try:
        files_api_tool()
    except Exception as e:
        print(f"Files API example skipped: {e}")
    mcp_tool()
    return {"serverside_tools": "complete"}
