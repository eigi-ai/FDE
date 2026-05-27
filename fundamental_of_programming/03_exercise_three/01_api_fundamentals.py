"""Runnable examples for Part 1: API fundamentals.

Read `01_api_fundamentals.md` first for the full theory.
This Python file is only for code examples and printed output.
"""


def print_api_summary():
    # Quick output summary of the main request/response model.
    print("--- API Fundamentals Summary ---")
    print("API means one software system can communicate with another.")
    print("A request contains method, URL, headers, and sometimes a body.")
    print("A response contains status code, headers, and response data.")
    print("JSON is the most common format used for API data exchange.")
    print()


def show_parameter_examples():
    # Show the difference between a resource identifier and optional filters.
    print("--- Query Parameter vs Path Parameter ---")
    print("Path parameter identifies a specific resource.")
    print("Example: GET /users/101")
    print("Here 101 is the path parameter.")
    print()
    print("Query parameter changes filtering, searching, sorting, or pagination.")
    print("Example: GET /users?city=Mumbai&page=2")
    print("Here city and page are query parameters.")
    print()


def show_body_examples():
    # Compare the most common request body formats used by APIs.
    print("--- Request Body Examples ---")

    json_body = {
        "content_type": "application/json",
        "body": {
            "name": "Nisha",
            "email": "nisha@example.com",
        },
    }

    form_body = {
        "content_type": "application/x-www-form-urlencoded",
        "body": "name=Nisha&email=nisha@example.com",
    }

    multipart_body = {
        "content_type": "multipart/form-data",
        "body": "file=<resume.pdf>&name=Nisha",
    }

    print("JSON body is most common for backend APIs:")
    print(json_body)
    print()
    print("Form data is common for simple HTML-style form submissions:")
    print(form_body)
    print()
    print("Multipart form data is used when files are uploaded:")
    print(multipart_body)
    print()


def show_status_code_guide():
    # Print a small cheat sheet of common HTTP responses.
    print("--- Important Status Codes ---")

    status_guide = [
        (200, "OK", "Use for successful read or update requests."),
        (201, "Created", "Use when a new resource is created."),
        (202, "Accepted", "Use when work will finish later, such as a background job."),
        (204, "No Content", "Use when the action succeeds but no body is returned."),
        (400, "Bad Request", "Use when request data is invalid or malformed."),
        (401, "Unauthorized", "Use when authentication is missing or invalid."),
        (403, "Forbidden", "Use when the user is authenticated but not allowed."),
        (404, "Not Found", "Use when the requested resource does not exist."),
        (
            405,
            "Method Not Allowed",
            "Use when the endpoint does not allow that HTTP method.",
        ),
        (409, "Conflict", "Use when the request conflicts with existing state."),
        (415, "Unsupported Media Type", "Use when the request body format is wrong."),
        (
            422,
            "Unprocessable Entity",
            "Use when validation fails on otherwise well-formed data.",
        ),
        (429, "Too Many Requests", "Use when rate limits are exceeded."),
        (500, "Internal Server Error", "Use for unexpected server-side failures."),
        (
            502,
            "Bad Gateway",
            "Use when one server gets a bad response from another server.",
        ),
        (
            503,
            "Service Unavailable",
            "Use when the service is temporarily down or overloaded.",
        ),
    ]

    for code, title, meaning in status_guide:
        print(f"{code} {title}: {meaning}")

    print()
    print("Quick rule:")
    print("4xx -> client-side problem")
    print("5xx -> server-side problem")
    print()


def show_example_request_response():
    # Show one complete POST request example and its matching response.
    request_example = {
        "method": "POST",
        "url": "https://api.example.com/v1/users",
        "headers": {
            "Content-Type": "application/json",
            "Authorization": "Bearer <token>",
        },
        "body": {
            "name": "Nisha",
            "email": "nisha@example.com",
        },
    }

    response_example = {
        "status_code": 201,
        "body": {
            "message": "User created successfully",
            "user_id": "USR-1001",
        },
    }

    print("--- Example Request ---")
    print(request_example)
    print()
    print("--- Example Response ---")
    print(response_example)
    print()


if __name__ == "__main__":
    print_api_summary()
    show_parameter_examples()
    show_body_examples()
    show_example_request_response()
    show_status_code_guide()
