# Part 1: API Fundamentals

This lesson explains the foundation of API learning before starting FastAPI.

## 1. What Is an API?

API stands for Application Programming Interface.

An API is a way for one software system to talk to another software system.

Simple idea:

- The client sends a request.
- The server processes that request.
- The server sends back a response.

## 2. Where APIs Are Used

APIs are used in many places:

- frontend calling backend
- backend calling another backend
- mobile app calling server
- payment systems
- maps, OTP, email, AI, and weather services

## 3. How an API Works

A typical API flow looks like this:

`Client -> HTTP Request -> Server -> HTTP Response -> Client`

## 4. Main Parts of an API Request

- URL / endpoint
- HTTP method
- headers
- query parameters
- path parameters
- body

### Query Parameter

A query parameter is added after `?` in the URL.

It is usually used for:

- filtering
- searching
- sorting
- pagination
- optional values

Example:

`GET /users?city=Mumbai&page=2`

Here:

- `city=Mumbai` is a query parameter
- `page=2` is a query parameter

### Path Parameter

A path parameter is part of the URL path itself.

It is usually used to identify one specific resource.

Example:

`GET /users/101`

Here:

- `101` is a path parameter
- it usually means "give me the user whose id is 101"

### Easy Difference

- path parameter: identifies a specific resource
- query parameter: changes how data is filtered, searched, or displayed

## 5. Main Parts of an API Response

- status code
- headers
- response body
- error message if something goes wrong

## 6. What Is JSON?

JSON stands for JavaScript Object Notation.

It is a text format used to exchange data.
APIs commonly send and receive JSON because it is simple and readable.

JSON example:

```json
{
  "name": "Aarav",
  "age": 21,
  "is_active": true
}
```

Python dictionary example:

```python
{
    "name": "Aarav",
    "age": 21,
    "is_active": True,
}
```

Notice the difference:

- JSON uses `true`, `false`, `null`
- Python uses `True`, `False`, `None`

## 7. Common HTTP Methods

- `GET`: read data
- `POST`: create data
- `PUT`: replace full data
- `PATCH`: update partial data
- `DELETE`: remove data

## 8. Headers

Headers carry extra information with a request.

Common examples:

- `Content-Type`: tells the format of the body
- `Authorization`: sends token or credentials
- `X-API-Key`: sends an API key

## 9. Request Body and Form Data

The body contains the main data sent to the server.

### JSON Body

Most modern APIs use JSON.

Content-Type is usually `application/json`.

Example:

```json
{
  "name": "Nisha",
  "email": "nisha@example.com"
}
```

### Form Data

Used when data is submitted like an HTML form.

Often used in older systems or login forms.

Common content type: `application/x-www-form-urlencoded`

Example:

```text
name=Nisha&email=nisha@example.com
```

### Multipart Form Data

Used when uploading files along with form fields.

Common content type: `multipart/form-data`

Example use cases:

- profile image upload
- document upload
- CSV upload

### When To Use What

- use JSON for most backend APIs
- use form data for simple form submissions when required by the API
- use multipart form data when files are involved

## 10. Important HTTP Status Codes

- `200 OK`: request succeeded
- `201 Created`: resource created
- `202 Accepted`: request accepted and may finish later
- `204 No Content`: success, but no response body is returned
- `400 Bad Request`: request is invalid
- `401 Unauthorized`: auth failed or missing
- `403 Forbidden`: permission denied
- `404 Not Found`: resource does not exist
- `405 Method Not Allowed`: HTTP method is not supported on this endpoint
- `409 Conflict`: request conflicts with current data state
- `415 Unsupported Media Type`: wrong body format or content type
- `422 Unprocessable Entity`: validation failed
- `429 Too Many Requests`: rate limit exceeded
- `500 Internal Server Error`: server-side issue
- `502 Bad Gateway`: one server got an invalid response from another server
- `503 Service Unavailable`: service is temporarily unavailable

## 11. When To Use Which Status Code

- `200 OK`: use when reading data or updating something successfully
- `201 Created`: use when a new resource is created successfully
- `202 Accepted`: use when the request is received but processing will happen later
- `204 No Content`: use when the action succeeds and nothing needs to be returned
- `400 Bad Request`: use when the client sends malformed or incorrect input
- `401 Unauthorized`: use when authentication is missing or invalid
- `403 Forbidden`: use when the user is authenticated but not allowed
- `404 Not Found`: use when the resource does not exist
- `409 Conflict`: use when the request clashes with the current data state
- `422 Unprocessable Entity`: use when the request shape is correct but validation fails
- `429 Too Many Requests`: use when the client exceeds a rate limit
- `500 Internal Server Error`: use for unexpected server-side failures

Quick backend rule:

- `4xx` means client-side problem
- `5xx` means server-side problem

## 12. Error Message

When an API fails, the response body usually explains why.

Example:

```json
{
  "detail": "Invalid API Key"
}
```

## 13. Real-World Reference

The eigi.ai API reference shows these building blocks clearly:

https://docs.eigi.ai/api-reference/introduction
