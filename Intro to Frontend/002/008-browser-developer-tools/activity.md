# Activity - Inspect And Debug A React App

## Goal

Practice using browser Developer Tools to debug frontend behavior.

## Task 1: Console

In your React app, add a temporary log inside a button or form handler:

```js
console.log("Search submitted");
console.log("Query:", query);
```

Open:

```text
Inspect -> Console
```

Verify:

- log appears when action happens
- no unexpected JavaScript errors appear

Demo question:

```text
How did you confirm the event handler ran?
```

---

## Task 2: Network

Trigger your API request.

Open:

```text
Inspect -> Network
```

Click the API request and inspect:

- request URL
- query parameters
- request headers
- `X-Api-Key` header
- status code
- response body

Demo question:

```text
How did you confirm the API request was sent correctly?
```

---

## Task 3: API Failure

Temporarily break the API key or endpoint.

Then check:

- Console error
- Network status code
- response body
- app error message

Requirement:

```text
The app must show a user-facing error, not only a console error.
```

Demo question:

```text
What status code did you get and what did your UI show?
```

---

## Task 4: Local Storage

Save one simple value to local storage, such as last search text or theme.

Example:

```js
localStorage.setItem("lastSearch", query);
```

Open:

```text
Inspect -> Application -> Local Storage
```

Verify the value exists.

Refresh the page and confirm the value is still there.

Demo question:

```text
What is the difference between local storage and React state?
```

---

## Task 5: Session Storage

Save one temporary value to session storage:

```js
sessionStorage.setItem("sessionSearch", query);
```

Open:

```text
Inspect -> Application -> Session Storage
```

Verify the value exists.

Close the tab and reopen the app to discuss whether the value remains.

---

## Task 6: Cookies

Open:

```text
Inspect -> Application -> Cookies
```

Check whether any cookies exist for your local app or API domain.

You do not need to build auth.

Just explain:

```text
Cookies can be sent automatically with matching requests.
Local storage and session storage are not automatically sent to the server.
```

---

## Final Debugging Report

Write a short `devtools-debug-report.md`:

```md
# DevTools Debug Report

## Console
What did you check?

## Network
Which API request did you inspect?
What status code came back?

## Application Storage
What did you find in local storage/session storage/cookies?

## One bug you can now debug better
Explain one issue DevTools helped you understand.
```

