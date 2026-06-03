# Part 4: Prompting, Safety, and Evaluation

This lesson explains how to use Generative AI more effectively and responsibly.

## 1. Why Prompting Matters

The prompt strongly affects the quality of the output.

A weak prompt often creates weak output.
A clear prompt usually creates better output.

## 2. Simple Prompt Pattern

A useful beginner prompt pattern is:

- task
- context
- constraints
- output format

Example:

"Explain JWT authentication to a beginner. Use simple words. Give 5 bullet
points and one small example."

Why this works:

- it tells the model what to do
- it gives the audience level
- it gives format guidance

## 3. Ways To Improve a Prompt

- be specific about the task
- mention the audience level
- include important context
- ask for a clear format
- mention what to avoid
- ask for examples when helpful

Weak prompt:

"Explain APIs"

Better prompt:

"Explain APIs to a first-year engineering student in simple language. Use one
real-world analogy and one JSON example."

## 4. Ask for Structured Output

Structured output is easier to review.

Examples:

- bullet points
- tables
- JSON
- step-by-step explanation
- pros and cons

Example prompt:

"Summarize this document in 5 bullet points. Then list 3 risks and 3 next steps."

## 5. Verify the Output

Never assume the first answer is correct.

Check for:

- factual correctness
- missing details
- unsafe advice
- invented references
- broken code
- outdated information

For code, run and test it.
For facts, verify with trusted sources.
For business content, review with domain experts.

## 6. Common Risks

### Hallucination

The model may generate false information confidently.

### Bias

The output may reflect unfair patterns present in training data.

### Privacy Risk

Sensitive company or personal data should not be shared in tools unless the
tool and workflow are approved for that data.

### Copyright and Ownership Questions

Generated content may still require review for legal and policy reasons,
especially in commercial settings.

### Over-Reliance

People may stop thinking critically if they trust AI too much.

## 7. How To Reduce Risk

- use approved tools
- avoid sharing secrets or private data
- provide clear context
- ask the model to cite or stay within supplied material when possible
- use RAG for domain-specific answers
- add human review before final use
- test generated code and verify generated facts

## 8. Evaluating a GenAI Output

You can evaluate output using simple questions:

- Is it correct?
- Is it relevant to the question?
- Is it complete enough?
- Is it easy to understand?
- Is it safe and appropriate?
- Does it follow the requested format?

In production systems, teams may also measure:

- accuracy
- latency
- cost
- user satisfaction
- groundedness
- failure rate

## 9. Good Beginner Habit

Treat AI output as a first draft.

That mindset helps you:

- review carefully
- improve the result
- avoid blind trust

## 10. Short Summary

- better prompts usually create better outputs
- structured prompts are easier to review
- AI output must be verified
- privacy, bias, hallucination, and misuse are real risks
- responsible usage is part of learning GenAI
