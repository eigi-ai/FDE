"""Runnable examples for Part 5: structured output, tokens, and pricing.

Read `05_structured_output_tokens_and_pricing.md` first for the full theory.
This file shows schema-shaped output and a simple token-cost calculation.
"""

import json


def show_structured_output_example():
    print("--- Structured Output Example ---")
    schema = {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "sentiment": {"type": "string", "enum": ["positive", "neutral", "negative"]},
            "summary": {"type": "string"},
        },
        "required": ["title", "sentiment", "summary"],
    }
    print("Requested schema:")
    print(json.dumps(schema, indent=2))
    print()

    sample_response = {
        "title": "Billing Issue Report",
        "sentiment": "negative",
        "summary": "The user reports a duplicate charge and wants a refund review.",
    }
    print("Example structured response:")
    print(json.dumps(sample_response, indent=2))
    print()


def validate_structured_output(raw_json: str):
    data = json.loads(raw_json)
    required_keys = ["title", "sentiment", "summary"]
    missing = [key for key in required_keys if key not in data]
    if missing:
        raise ValueError(f"Missing required keys: {missing}")
    return data


def estimate_request_cost(
    input_tokens: int,
    output_tokens: int,
    input_price_per_million: float,
    output_price_per_million: float,
) -> float:
    input_cost = (input_tokens / 1_000_000) * input_price_per_million
    output_cost = (output_tokens / 1_000_000) * output_price_per_million
    return input_cost + output_cost


def show_validation_example():
    print("--- Structured Output Validation ---")
    raw_json = json.dumps(
        {
            "title": "Billing Issue Report",
            "sentiment": "negative",
            "summary": "The user reports a duplicate charge and wants a refund review.",
        }
    )
    parsed = validate_structured_output(raw_json)
    print(parsed)
    print()


def show_token_pricing_example():
    print("--- Token Pricing Example ---")
    input_tokens = 20_000
    output_tokens = 2_000
    cost = estimate_request_cost(
        input_tokens=input_tokens,
        output_tokens=output_tokens,
        input_price_per_million=5,
        output_price_per_million=15,
    )
    print(f"Input tokens: {input_tokens}")
    print(f"Output tokens: {output_tokens}")
    print(f"Estimated request cost: ${cost:.2f}")
    print()


def show_practical_cost_controls():
    print("--- Practical Cost Controls ---")
    print("- keep system prompts short")
    print("- trim old chat history")
    print("- limit tool output before reinserting it into the prompt")
    print("- request structured output only when the workflow needs it")
    print("- set output token limits intentionally")
    print()


if __name__ == "__main__":
    show_structured_output_example()
    show_validation_example()
    show_token_pricing_example()
    show_practical_cost_controls()