# 008 - Final React API Activity

## Goal

Build a small React app using any one API endpoint from API Ninjas.

This final activity combines:

- components
- JSX
- props
- `useState`
- events
- controlled inputs
- conditional rendering
- lists and keys if needed
- `useEffect` where appropriate
- API state
- one custom hook
- browser Developer Tools

## Required Flow

Your app should clearly show this:

```text
User action -> state change -> API request -> response -> re-render
```

## API Choice

Choose any suitable API from API Ninjas.

Before coding, inspect:

1. endpoint URL
2. query parameters
3. headers
4. response shape
5. fields to display
6. possible failure cases

## Required UI States

Your app must show:

- idle state
- loading state
- success/result state
- error state
- empty state if applicable

## Required Custom Hook

Create one hook for API behavior.

Suggested name:

```text
useApiNinjasSearch
```

Suggested return shape:

```jsx
return {
  data,
  loading,
  error,
  search,
  reset,
};
```

## Required DevTools Check

Use browser DevTools during the activity.

You must inspect:

- Console for JavaScript errors/logs
- Network for API request URL, headers, status code, and response body
- Application for local storage, session storage, and cookies if your app uses storage

For API Ninjas, confirm the request includes:

```http
X-Api-Key: YOUR_API_KEY
```
