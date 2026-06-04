"""Runnable examples for Part 10: agent frameworks and real-time AI.

Read `10_agent_frameworks_and_real_time_ai.md` first for the theory.
"""


def show_framework_selection():
    print("--- When to Use Which Framework ---")
    print("- plain API calls: simple single-step tasks")
    print("- LangGraph: explicit routing, state, and tool loops")
    print("- CrewAI: multiple agent roles working together")
    print("- Pipecat: low-latency real-time voice pipelines")
    print("- LiveKit: real-time audio/video transport and media apps")
    print()


def show_langgraph_example():
    print("--- Small LangGraph Example ---")
    code = '''
from langgraph.graph import END, START, StateGraph


def decide(state):
    question = state["question"].lower()
    if "policy" in question:
        return {"route": "retrieve"}
    return {"route": "answer"}


workflow = StateGraph(dict)
workflow.add_node("decide", decide)
workflow.add_edge(START, "decide")
workflow.add_edge("decide", END)
graph = workflow.compile()
'''
    print(code)
    print()


def show_real_time_voice_pipeline():
    print("--- Real-Time Voice Pipeline ---")
    print("1. stream microphone audio")
    print("2. run speech-to-text")
    print("3. call the chat model")
    print("4. optionally call tools")
    print("5. run text-to-speech")
    print("6. stream audio back to the user")
    print()


def show_real_time_api_snippet():
    print("--- Voice Agent Pseudocode ---")
    code = '''
def on_audio_chunk(chunk_bytes):
    transcript = stt_provider.transcribe(chunk_bytes)
    response_text = chat_model.reply(transcript)
    audio_bytes = tts_provider.speak(response_text)
    return audio_bytes
'''
    print(code)
    print()


def show_framework_mental_model():
    print("--- Mental Model ---")
    print("Frameworks do not replace the model.")
    print("They help manage routing, state, retries, streaming, and observability.")
    print()


if __name__ == "__main__":
    show_framework_selection()
    show_langgraph_example()
    show_real_time_voice_pipeline()
    show_real_time_api_snippet()
    show_framework_mental_model()