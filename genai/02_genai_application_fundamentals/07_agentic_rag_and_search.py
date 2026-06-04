"""Runnable examples for Part 7: agentic RAG and search.

Read `07_agentic_rag_and_search.md` first for the theory.
"""


INTERNAL_DOCS = [
    "The refund policy allows enterprise refunds only after finance approval.",
    "API authentication uses bearer tokens.",
]


def should_retrieve(question: str) -> bool:
    keywords = ["policy", "internal", "docs", "authentication"]
    return any(keyword in question.lower() for keyword in keywords)


def retrieve_internal_docs(question: str) -> str:
    for document in INTERNAL_DOCS:
        if "policy" in question.lower() and "policy" in document.lower():
            return document
        if "authentication" in question.lower() and "authentication" in document.lower():
            return document
    return ""


def web_search_stub(question: str) -> str:
    return f"Pretend web search result for: {question}"


def grade_context(question: str, context: str) -> bool:
    question_words = set(question.lower().split())
    context_words = set(context.lower().split())
    return bool(question_words & context_words)


def rewrite_question(question: str) -> str:
    return f"Provide a more specific answer for: {question}"


def generate_answer(question: str, context: str) -> str:
    if not context:
        return "I do not have enough context to answer reliably."
    return f"Using the retrieved context, the answer is: {context}"


def run_agentic_rag(question: str):
    print("--- Agentic RAG Flow ---")
    print(f"Question: {question}")
    if should_retrieve(question):
        print("Decision: retrieve internal context")
        context = retrieve_internal_docs(question)
        if not grade_context(question, context):
            question = rewrite_question(question)
            print(f"Rewritten question: {question}")
            context = retrieve_internal_docs(question)
    else:
        print("Decision: use web search or direct answer")
        context = web_search_stub(question)

    answer = generate_answer(question, context)
    print(f"Context: {context}")
    print(f"Answer: {answer}")
    print()


def show_langgraph_style_note():
    print("--- LangGraph-Style Mental Model ---")
    print("A graph-based agent often has nodes such as:")
    print("- decide whether to retrieve")
    print("- call retriever tool")
    print("- grade retrieved content")
    print("- rewrite question")
    print("- generate final answer")
    print()


if __name__ == "__main__":
    run_agentic_rag("What is the refund policy for enterprise customers?")
    run_agentic_rag("What happened in AI news today?")
    show_langgraph_style_note()