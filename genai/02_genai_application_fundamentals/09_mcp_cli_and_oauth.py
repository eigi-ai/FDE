"""Runnable examples for Part 9: MCP, CLI, and OAuth.

Read `09_mcp_cli_and_oauth.md` first for the theory.
This file prints MCP examples instead of running a real server.
"""


def explain_why_mcp_exists():
    print("--- Why MCP Exists ---")
    print(
        "MCP gives one standard way to expose tools, resources, and prompts to AI clients instead of building a custom adapter for every client."
    )
    print(
        "That makes it easier to connect your internal tool layer to MCP-capable editors, agent platforms, and other AI clients."
    )
    print()


def show_small_mcp_server_example():
    print("--- Small MCP Server Example ---")
    code = '''
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("docs-server")


@mcp.tool()
def search_docs(query: str) -> str:
    """Search internal docs by query."""
    return f"Results for: {query}"


@mcp.resource("docs://getting-started")
def getting_started() -> str:
    return "Start by creating an API key and configuring your base URL."


@mcp.prompt()
def support_prompt(topic: str) -> str:
    return f"You are a support assistant. Help with: {topic}"


if __name__ == "__main__":
    mcp.run()
'''
    print(code)
    print()


def show_stdio_client_config_example():
    print("--- Example stdio MCP Client Config ---")
    config = '''
{
  "mcpServers": {
    "docs-server": {
      "command": "python",
            "args": ["path/to/your_mcp_server.py"]
    }
  }
}
'''
    print(config)
    print()


def show_oauth_example():
    print("--- Remote MCP OAuth Example ---")
    print("For remote HTTP MCP, the client may need an OAuth access token.")
    print("Example request header:")
    print("Authorization: Bearer <access-token>")
    print()
    print("Important rule: stdio/local MCP usually does not use this HTTP OAuth flow.")
    print()


def show_mcp_flow():
    print("--- Very Small MCP Flow ---")
    print("1. client connects to the MCP server")
    print("2. client discovers tools/resources/prompts")
    print("3. the user or model selects one")
    print("4. the server returns data or runs the action")
    print("5. the result is used inside the GenAI application")
    print()


if __name__ == "__main__":
    explain_why_mcp_exists()
    show_small_mcp_server_example()
    show_stdio_client_config_example()
    show_oauth_example()
    show_mcp_flow()