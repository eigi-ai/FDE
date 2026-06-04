"""Runnable examples for Part 4: tools, plugins, and tool calling.

Read `04_tools_plugins_and_tool_calling.md` first for the full theory.
This file demonstrates the schema and a simple end-to-end tool flow.
"""

import json


def build_search_docs_tool_schema():
    return {
        "type": "function",
        "function": {
            "name": "search_docs",
            "description": (
                "Search internal product and engineering documentation. "
                "Use this for setup, API, or architecture questions. "
                "Do not use this for live account actions."
            ),
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "Natural-language search query for the docs.",
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Maximum number of results to return.",
                        "minimum": 1,
                        "maximum": 10,
                    },
                },
                "required": ["query"],
            },
        },
    }


def show_tool_schema_example():
    print("--- Tool Schema Example ---")
    print(json.dumps(build_search_docs_tool_schema(), indent=2))
    print()


def simulate_model_tool_call():
    print("--- Simulated Model Tool Call ---")
    tool_call = {
        "id": "call_123",
        "type": "function",
        "function": {
            "name": "search_docs",
            "arguments": json.dumps(
                {"query": "How does JWT authentication work in our backend?", "top_k": 3}
            ),
        },
    }
    print(json.dumps(tool_call, indent=2))
    print()
    return tool_call


def run_fake_tool(arguments_json):
    arguments = json.loads(arguments_json)
    fake_results = [
        "JWT authentication uses a signed token sent in the Authorization header.",
        "The backend verifies the signature and extracts the user claims.",
        "Expired or malformed tokens should return 401 Unauthorized.",
    ]
    return {
        "query": arguments["query"],
        "results": fake_results[: arguments.get("top_k", 3)],
    }


def show_tool_result_cycle():
    print("--- Tool Result Cycle ---")
    tool_call = simulate_model_tool_call()
    tool_result = run_fake_tool(tool_call["function"]["arguments"])
    tool_message = {
        "role": "tool",
        "tool_call_id": tool_call["id"],
        "content": json.dumps(tool_result),
    }
    print("Tool result sent back to the model:")
    print(json.dumps(tool_message, indent=2))
    print()
    print("Important rule: tool output is data, not high-trust instructions.")
    print()


def show_plugin_vs_tool_note():
    print("--- Plugin vs Tool ---")
    print("Plugin is often an older product-specific packaging term.")
    print("Tool is the broader modern concept used in most API designs.")
    print()


if __name__ == "__main__":
    show_tool_schema_example()
    show_tool_result_cycle()
    show_plugin_vs_tool_note()