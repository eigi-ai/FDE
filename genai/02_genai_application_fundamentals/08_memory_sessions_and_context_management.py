"""Runnable examples for Part 8: memory, sessions, and context management.

Read `08_memory_sessions_and_context_management.md` first for the theory.
"""

import uuid


SESSION_STORE = {}


def create_session() -> str:
    session_id = str(uuid.uuid4())
    SESSION_STORE[session_id] = {"history": [], "summary": ""}
    return session_id


def add_message(session_id: str, role: str, content: str):
    SESSION_STORE[session_id]["history"].append({"role": role, "content": content})


def approximate_token_count(text: str) -> int:
    return len(text.split())


def summarize_history(history: list[dict]) -> str:
    recent_text = " ".join(item["content"] for item in history[-3:])
    words = recent_text.split()[:25]
    return " ".join(words)


def build_prompt(session_id: str, new_user_message: str, token_limit: int = 40):
    session = SESSION_STORE[session_id]
    history_text = " ".join(item["content"] for item in session["history"])
    combined = f"{session['summary']} {history_text} {new_user_message}".strip()

    if approximate_token_count(combined) > token_limit:
        session["summary"] = summarize_history(session["history"])
        prompt = [
            {"role": "system", "content": f"Conversation summary: {session['summary']}"},
            {"role": "user", "content": new_user_message},
        ]
    else:
        prompt = session["history"] + [{"role": "user", "content": new_user_message}]

    return prompt


def show_session_example():
    print("--- Session and Memory Example ---")
    session_id = create_session()
    print(f"Session ID: {session_id}")

    add_message(session_id, "user", "Help me set up the billing API.")
    add_message(session_id, "assistant", "Sure. Start with the API key and account ID.")
    add_message(session_id, "user", "Now explain webhooks and retries too.")
    add_message(session_id, "assistant", "Use signed webhooks and retry with backoff.")

    prompt = build_prompt(session_id, "What headers are required for authentication?")
    print("Prompt sent to the model:")
    for message in prompt:
        print(message)
    print()


if __name__ == "__main__":
    show_session_example()