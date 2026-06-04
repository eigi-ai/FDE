"""Runnable examples for Part 1: how GenAI applications are built.

Read `01_how_genai_apps_are_built.md` first for the full theory.
This Python file focuses on small examples and printed payloads.
"""


def show_basic_genai_pipeline():
    print("--- A Basic GenAI Application Pipeline ---")
    steps = [
        "1. accept input from the user",
        "2. build messages and instructions",
        "3. attach useful context",
        "4. call the model API",
        "5. optionally call tools",
        "6. store the result in session history",
        "7. return the final answer",
    ]
    for step in steps:
        print(step)
    print()


def show_text_to_text_example():
    print("--- Text-To-Text Example ---")
    messages = [
        {"role": "system", "content": "You are a concise study assistant."},
        {"role": "user", "content": "Summarize this article in 3 bullet points."},
    ]
    print("Messages sent to the model:")
    print(messages)
    print()


def show_deepgram_stt_example():
    print("--- Speech-To-Text Example (Deepgram) ---")
    print("The code below is an example pattern. It is not executed automatically.")
    print()
    code = """
import os
import requests

audio_bytes = b"...raw wav or mp3 bytes..."

response = requests.post(
    "https://api.deepgram.com/v1/listen?model=nova-3&smart_format=true",
    headers={
        "Authorization": f"Token {os.getenv('DEEPGRAM_API_KEY')}",
        "Content-Type": "audio/wav",
    },
    data=audio_bytes,
    timeout=60,
)

response.raise_for_status()
transcript = response.json()["results"]["channels"][0]["alternatives"][0]["transcript"]
print(transcript)
"""
    print(code)
    print()


def show_openai_tts_example():
    print("--- Text-To-Speech Example (OpenAI) ---")
    print("The code below is an example pattern. It is not executed automatically.")
    print()
    code = """
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

speech = client.audio.speech.create(
    model="gpt-4o-mini-tts",
    voice="alloy",
    input="Hello, your meeting starts in 10 minutes.",
)

with open("speech.mp3", "wb") as file:
    file.write(speech.read())
"""
    print(code)
    print()


def show_cartesia_tts_example():
    print("--- Text-To-Speech Example (Cartesia) ---")
    print("The code below is an example pattern. It is not executed automatically.")
    print()
    code = """
import os
import requests

payload = {
    "model_id": "sonic-2",
    "voice": {"mode": "id", "id": "f9836c6e-a0bd-460e-9d3c-f7299fa60f94"},
    "transcript": "Welcome to the voice demo.",
    "output_format": {"container": "mp3", "bit_rate": 128000, "sample_rate": 44100},
}

response = requests.post(
    "https://api.cartesia.ai/tts/bytes",
    headers={
        "Cartesia-Version": "2024-06-10",
        "X-API-Key": os.getenv("CARTESIA_API_KEY"),
        "Content-Type": "application/json",
    },
    json=payload,
    timeout=60,
)

response.raise_for_status()

with open("cartesia_speech.mp3", "wb") as file:
    file.write(response.content)
"""
    print(code)
    print()


def show_speech_to_speech_flow():
    print("--- Speech-To-Speech Flow ---")
    print("A practical speech-to-speech application often looks like this:")
    print("1. receive microphone audio")
    print("2. send audio to an STT provider such as Deepgram")
    print("3. send the transcript to an LLM")
    print("4. generate a text response")
    print("5. send the text response to a TTS provider such as OpenAI or Cartesia")
    print("6. stream or play back the audio")
    print()


if __name__ == "__main__":
    show_basic_genai_pipeline()
    show_text_to_text_example()
    show_deepgram_stt_example()
    show_openai_tts_example()
    show_cartesia_tts_example()
    show_speech_to_speech_flow()