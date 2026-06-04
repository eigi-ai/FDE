"""Runnable examples for Part 6: documents, embeddings, and RAG.

Read `06_documents_embeddings_and_rag.md` first for the theory.
This file uses a tiny local retrieval demo instead of external libraries.
"""

import math
from collections import Counter


DOCUMENTS = [
    "Bearer token authentication is required for protected API routes.",
    "Webhook retries should use exponential backoff to avoid overload.",
    "Embeddings convert text into vectors that support semantic search.",
]


def tokenize(text: str) -> list[str]:
    cleaned = text.lower().replace(".", "")
    return cleaned.split()


def text_to_vector(text: str) -> Counter:
    return Counter(tokenize(text))


def cosine_similarity(left: Counter, right: Counter) -> float:
    common_tokens = set(left) & set(right)
    numerator = sum(left[token] * right[token] for token in common_tokens)
    left_size = math.sqrt(sum(value * value for value in left.values()))
    right_size = math.sqrt(sum(value * value for value in right.values()))
    if not left_size or not right_size:
        return 0.0
    return numerator / (left_size * right_size)


def retrieve(query: str, documents: list[str], top_k: int = 2) -> list[tuple[float, str]]:
    query_vector = text_to_vector(query)
    scored = []
    for document in documents:
        score = cosine_similarity(query_vector, text_to_vector(document))
        scored.append((score, document))
    scored.sort(key=lambda item: item[0], reverse=True)
    return scored[:top_k]


def show_document_pipeline():
    print("--- Document Pipeline ---")
    print("1. load documents")
    print("2. tokenize and vectorize them")
    print("3. store vectors in an index")
    print("4. vectorize the query")
    print("5. retrieve similar chunks")
    print()


def show_retrieval_example():
    print("--- Retrieval Example ---")
    query = "How do embeddings help search?"
    print(f"Query: {query}")
    results = retrieve(query, DOCUMENTS, top_k=2)
    for score, document in results:
        print(f"score={score:.3f} | document={document}")
    print()


def show_rag_answer_example():
    print("--- Simple RAG Answer Example ---")
    query = "What are embeddings used for?"
    results = retrieve(query, DOCUMENTS, top_k=1)
    context = results[0][1]
    answer = (
        "Embeddings convert text into vectors, which helps systems perform semantic "
        "search and retrieve meaningfully related content."
    )
    print(f"Retrieved context: {context}")
    print(f"Generated answer: {answer}")
    print()


if __name__ == "__main__":
    show_document_pipeline()
    show_retrieval_example()
    show_rag_answer_example()