"""Runnable examples for Part 3: API calls, webhooks, SDK, sync, and async.

Read `03_api_calls_sdk_async.md` first for the full theory.
This Python file is only for code examples and printed output.
"""


def show_server_to_server_example():
    # Introduce the common names used for backend integrations.
    print("--- Backend-to-Backend Communication ---")
    print("Term: backend-to-backend communication")
    print("Also called: server-to-server or service-to-service communication")
    print("Example: your backend calls the eigi.ai API to fetch or send data.")
    print()


def show_webhook_explanation():
    # Contrast event-driven callbacks with request-driven polling.
    print("--- Webhook Explanation ---")
    print("A webhook is an event-based server-to-server callback.")
    print(
        "Your backend provides a URL, and another platform sends data to that URL when an event happens."
    )
    print("Example: a payment platform sends a webhook after a successful payment.")
    print(
        "This is different from polling, where your backend keeps checking status again and again."
    )
    print()


def show_curl_example():
    # Print a simple terminal example for testing an API.
    print("--- cURL Example ---")
    curl_command = (
        "curl https://api.eigi.ai/v1/public/conversations "
        '-H "X-API-Key: vk_your_api_key_here"'
    )
    print(curl_command)
    print()


def show_python_api_example():
    # Show a typical backend pattern for calling an external API safely.
    print("--- Python API Call Example (requests style) ---")
    print("The code below is an example pattern. It is not executed automatically.")
    print()

    example_code = """
import os
import requests

url = "https://api.eigi.ai/v1/public/conversations"
headers = {
    "X-API-Key": os.getenv("EIGI_API_KEY"),
    "Content-Type": "application/json",
}

try:
    response = requests.get(url, headers=headers, timeout=30)
    response.raise_for_status()
    data = response.json()
    print(data)
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as error:
    print(f"HTTP error: {error}")
except requests.exceptions.RequestException as error:
    print(f"Request failed: {error}")
"""
    print(example_code)
    print()


def show_async_example():
    # Show the smallest possible async/await example.
    print("--- Sync vs Async ---")
    print("Sync: tasks run one by one.")
    print("Async: waiting work can be handled more efficiently.")
    print()

    async_example = """
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    return "data received"
"""
    print(async_example)
    print()


def show_sdk_explanation():
    # Summarize why SDKs are often easier than writing raw HTTP calls every time.
    print("--- SDK Explanation ---")
    print("SDK means Software Development Kit.")
    print(
        "An SDK usually wraps raw HTTP calls into easier Python functions or classes."
    )
    print(
        "First learn raw API calls clearly. Then SDKs will be much easier to understand."
    )
    print()


if __name__ == "__main__":
    show_server_to_server_example()
    show_webhook_explanation()
    show_curl_example()
    show_python_api_example()
    show_async_example()
    show_sdk_explanation()
