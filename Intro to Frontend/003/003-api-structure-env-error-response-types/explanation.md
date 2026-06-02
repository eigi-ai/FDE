# 003 - API Structure, Env Variables, Error Handling, And Response Types

## Goal

Learn how to organize API code outside page components.

Core idea:

```text
page component handles UI
service file handles API request
Axios client handles common request config
types describe API data
env variables configure the API URL
```

## Why Move API Code Out Of Pages?

This works for a small demo:

```tsx
async function loadData() {
  const response = await fetch("https://api.example.com/candidates");
  const data = await response.json();
  setCandidates(data.items);
}
```

But in a larger app, this becomes hard to manage.

Better structure:

```text
src/
  services/
    apiClient.ts
    candidateService.ts
  types/
    candidate.ts
  features/
    api-lab/
      ApiLabPage.tsx
```

## What Is Axios?

Axios is a JavaScript HTTP client.

That means:

```text
Axios helps your frontend send requests to APIs and receive responses.
```

Axios is not a backend.

Axios is not an API.

Axios is not a database.

Axios is a helper library you use inside your React app when you need to talk to another server.

Example:

```text
React app needs candidate data
-> Axios sends request to API
-> API sends response
-> Axios gives data back to React
-> React updates the UI
```

Install it:

```bash
npm install axios
```

## How Axios Works

When you write:

```ts
const response = await axios.get("/api/candidates");
```

this means:

```text
Send a GET request to /api/candidates.
Wait for the API response.
Store the Axios response object in response.
```

The Axios response object usually contains:

```ts
response.data; // response body
response.status; // HTTP status code, such as 200 or 404
response.headers; // response headers
```

Most of the time in frontend work, you mainly use:

```ts
response.data;
```

because that is the actual JSON data your UI needs to render.

## Axios Request Flow In React

Use this mental model:

```text
user clicks button
-> event handler runs
-> page calls service function
-> service function calls Axios
-> Axios sends request
-> API returns response
-> Axios gives response.data
-> React state updates
-> UI re-renders
```

You can call APIs with `fetch` or Axios.

With `fetch`:

```ts
const response = await fetch("/api/candidates");

if (!response.ok) {
  throw new Error("Request failed");
}

const data = await response.json();
```

With Axios:

```ts
const response = await axios.get("/api/candidates");
const data = response.data;
```

Beginner-friendly difference:

```text
fetch gives you a Response object.
You manually check response.ok and parse response.json().

Axios gives you response.data.
Axios rejects failed status codes like 404 and 500 by default.
```

Axios does not remove the need for good structure. You should still keep API logic in service files.

## Common Axios Methods

Use `get` to read data:

```ts
const response = await axios.get("/api/candidates");
```

Use `post` to create data:

```ts
const response = await axios.post("/api/candidates", {
  name: "Asha",
  role: "Frontend Developer",
});
```

Use `put` to replace or update data:

```ts
const response = await axios.put("/api/candidates/123", {
  status: "interview",
});
```

Use `delete` to delete data:

```ts
await axios.delete("/api/candidates/123");
```

## Query Params With Axios

For URLs like:

```text
/api/candidates?status=interview&page=1
```

write:

```ts
const response = await axios.get("/api/candidates", {
  params: {
    status: "interview",
    page: 1,
  },
});
```

Axios turns `params` into query parameters.

## Headers With Axios

Some APIs need headers.

Example:

```ts
const response = await axios.get("/api/candidates", {
  headers: {
    "X-Api-Key": "demo-key",
  },
});
```

But do not repeat headers in every component. Put shared headers in an Axios client.

## Vite Env Variables

In Vite, frontend env variables must start with:

```text
VITE_
```

Example `.env`:

```text
VITE_API_BASE_URL=https://api.example.com
VITE_API_KEY=demo-key
```

Example `.env.example`:

```text
VITE_API_BASE_URL=https://api.example.com
VITE_API_KEY=replace-with-demo-key
```

Read env variables:

```ts
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
```

Important:

```text
Frontend env variables are visible in browser code after build.
Do not put private secrets in frontend env files.
```

## API Client

Create one reusable Axios client for common request behavior.

```ts
import axios from "axios";

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
const API_KEY = import.meta.env.VITE_API_KEY;

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: API_KEY
    ? {
        "X-Api-Key": API_KEY,
      }
    : {},
});

export async function apiGet<T>(path: string): Promise<T> {
  try {
    const response = await apiClient.get<T>(path);
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error)) {
      const status = error.response?.status;
      const message = status
        ? `Request failed with status ${status}`
        : "Request failed before the server responded.";

      throw new Error(message);
    }

    throw error;
  }
}
```

What this does:

- builds full API URL
- sends request
- uses shared headers
- handles failed Axios requests
- returns `response.data`
- returns typed data

## Response Types

Example:

```ts
export type Candidate = {
  id: string;
  name: string;
  role: string;
  status: "applied" | "interview" | "selected";
};

export type CandidateListResponse = {
  items: Candidate[];
};
```

## Feature Service

```ts
import { apiGet } from "./apiClient";
import type { CandidateListResponse } from "../types/candidate";

export function getCandidates() {
  return apiGet<CandidateListResponse>("/candidates");
}
```

## API State In UI

```ts
type ApiState<T> = {
  data: T | null;
  loading: boolean;
  error: string;
};
```

Use it:

```tsx
const [candidateState, setCandidateState] = useState<ApiState<CandidateListResponse>>({
  data: null,
  loading: false,
  error: "",
});
```

## User-Facing Error Handling

The app needs both:

```text
Console error -> helps developer debug
UI error -> helps user understand what happened
```

Example:

```tsx
try {
  setCandidateState({ data: null, loading: true, error: "" });
  const data = await getCandidates();
  console.log("Candidates response", data);
  setCandidateState({ data, loading: false, error: "" });
} catch (error) {
  console.error("Candidates request failed", error);
  setCandidateState({
    data: null,
    loading: false,
    error: "Could not load candidates. Please try again.",
  });
}
```

## Where Axios Should Live

Good:

```text
Page component -> candidateService.ts -> apiClient.ts -> Axios
```

Avoid:

```text
Page component -> Axios directly everywhere
```

If every page imports Axios directly, API logic becomes scattered.

## Key Line

```text
API service files keep network logic separate from UI logic, and Axios keeps request code cleaner than raw fetch.
```
