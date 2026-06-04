"""Runnable examples for Part 3: chat completion, parameters, and context.

Read `03_chat_completion_temperature_and_context.md` first for the full theory.
This file shows how to build a chat completion request cleanly.
"""

import json


def build_gemini_openai_compatible_payload():
    return {
        "model": "gemini-2.0-flash",
        "messages": [
            {"role": "system", "content": "You are a concise backend tutor."},
            {"role": "user", "content": "Explain embeddings with one API example."},
        ],
        "temperature": 0.2,
        "top_p": 0.95,
        "seed": 42,
        "max_tokens": 300,
        "stream": False,
    }


def show_gemini_chat_completion_example():
    print("--- Gemini Chat Completion Through The OpenAI-Compatible API ---")
    print("The code below is an example pattern. It is not executed automatically.")
    print()
    code = """
import json
import os
import urllib.request

url = "https://generativelanguage.googleapis.com/v1beta/openai/chat/completions"

payload = {
    "model": "gemini-2.0-flash",
    "messages": [
        {"role": "system", "content": "You are a concise backend tutor."},
        {"role": "user", "content": "Explain embeddings with one API example."}
    ],
    "temperature": 0.2,
    "top_p": 0.95,
    "max_tokens": 300,
}

request = urllib.request.Request(
    url,
    data=json.dumps(payload).encode("utf-8"),
    headers={
        "Authorization": f"Bearer {os.getenv('GEMINI_API_KEY')}",
        "Content-Type": "application/json",
    },
    method="POST",
)

with urllib.request.urlopen(request, timeout=60) as response:
    body = json.loads(response.read().decode("utf-8"))
    print(body["choices"][0]["message"]["content"])
"""
    print(code)
    print()


def show_payload_and_parameter_explanation():
    print("--- Important Parameters ---")
    payload = build_gemini_openai_compatible_payload()
    print(json.dumps(payload, indent=2))
    print()
    print("What each important field does:")
    print("- model: selects the model")
    print("- messages: provides role-based conversation context")
    print("- temperature: controls randomness")
    print("- top_p: alternative sampling control")
    print("- seed: helps repeatability when the provider supports it")
    print("- max_tokens: limits the answer length")
    print("- stream: returns tokens incrementally when true")
    print()


def show_openai_sdk_style_for_gemini():
    print("--- OpenAI SDK Style Example For Gemini ---")
    print("Some providers expose an OpenAI-compatible base URL.")
    print("The code below is an example pattern. It is not executed automatically.")
    print()
    code = """
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

response = client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role": "system", "content": "You are a concise backend tutor."},
        {"role": "user", "content": "Explain embeddings with one API example."},
    ],
    temperature=0.2,
    top_p=0.95,
    max_tokens=300,
)

print(response.choices[0].message.content)
"""
    print(code)
    print()


def show_context_window_note():
    print("--- Context Window Reminder ---")
    print("The context window includes:")
    print("- system instructions")
    print("- developer instructions")
    print("- user messages")
    print("- assistant history")
    print("- tool outputs")
    print("- retrieved documents")
    print("- newly generated output tokens")
    print()


if __name__ == "__main__":
    show_gemini_chat_completion_example()
    show_payload_and_parameter_explanation()
    show_openai_sdk_style_for_gemini()
    show_context_window_note()