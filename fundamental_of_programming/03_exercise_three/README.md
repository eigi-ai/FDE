# Exercise Three: API Fundamentals Before FastAPI

This exercise introduces the core concepts a beginner should understand before
starting FastAPI.

FastAPI is a framework for building APIs, but before learning framework syntax,
it is important to understand what an API is, how requests and responses work,
how JSON is used, how headers and status codes behave, how backend systems call
other APIs, how webhooks work, and how Python handles imports and exceptions.

## How To Read This Module

Each topic is split into two parts:

- `.md` files contain the full theory and conceptual explanation
- `.py` files contain runnable examples and code-focused explanation

Recommended way to learn:

1. Read the `.md` file first.
2. Then open the matching `.py` file.
3. Run the `.py` file and observe the output.

## Learning Order

1. `01_api_fundamentals.md`
   Read the theory for API basics, HTTP structure, request body formats, parameters, and status codes.

2. `01_api_fundamentals.py`
   Run the API examples and inspect the code.

3. `02_python_backend_basics.md`
   Read the theory for imports and Python exception handling.

4. `02_python_backend_basics.py`
   Run the import and exception-handling examples.

5. `03_api_calls_sdk_async.md`
   Read the theory for backend-to-backend communication, webhooks, cURL, SDKs, sync, and async.

6. `03_api_calls_sdk_async.py`
   Run the API integration examples and inspect the code.

## Important Terms

- API: Application Programming Interface
- HTTP: the protocol used by most web APIs
- JSON: the most common format for sending and receiving API data
- Backend-to-backend communication: one server calling another server
- Server-to-server communication: another common name for backend-to-backend
- Service-to-service communication: common term in larger systems
- Webhook: an event-driven callback from one server to another server
- SDK: Software Development Kit

## Real API Reference Used In This Exercise

This exercise uses the eigi.ai API documentation as a real reference for how
an API is documented:

- `https://docs.eigi.ai/api-reference/introduction`

Useful things visible in that documentation:

- base URL: `https://api.eigi.ai`
- authentication through the `X-API-Key` header
- JSON request and response format
- common HTTP status codes
- error response shape
- rate limiting details

## Beginner Notes

- In Python, we use `try` and `except`, not `try` and `catch`.
- Webhooks are also server-to-server communication, but they are event-driven.
- `import` lets one file use code from another file or module.
- Do not hardcode secret API keys into source files.
- Use environment variables for keys and tokens.

## Suggested Next Step After This Exercise

After completing these files, the learner should be ready to start FastAPI with:

- routes
- request bodies
- query parameters
- path parameters
- validation
- async route handlers
