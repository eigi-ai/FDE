# 008 - Browser Developer Tools

## What Are Developer Tools?

Browser Developer Tools, usually called DevTools, are built into the browser.

They help frontend engineers inspect, debug, and understand what is happening inside a web app.

Open DevTools:

```text
Right click page -> Inspect
```

Common shortcuts:

```text
Mac: Cmd + Option + I
Windows/Linux: Ctrl + Shift + I
```

## Why DevTools Matter

When a React app does not work, do not guess blindly.

Use DevTools to check:

- what error happened
- whether an API request was sent
- what response came back
- whether a file loaded
- what data is stored in the browser
- whether cookies exist
- whether local storage/session storage has expected values

DevTools help you move from:

```text
I think it is broken
```

to:

```text
The API returned 401 because the key/header is missing.
```

---

## 1. Elements Panel

The Elements panel shows the live DOM and CSS.

Use it to inspect:

- HTML structure
- classes
- styles
- layout spacing
- hidden elements
- responsive behavior

Important:

```text
Elements shows the live DOM, not just the original source HTML.
```

In React, the DOM is generated from components and state. If state changes, React updates the DOM, and you can inspect the result here.

---

## 2. Console Panel

The Console shows:

- JavaScript errors
- warnings
- `console.log()` output
- failed script errors
- debugging messages

Example:

```js
console.log("API data:", data);
```

Use Console to answer:

```text
Did my event handler run?
What value is in state?
What data did the API return?
Is there a JavaScript error?
```

Important:

```text
Console is for developers. It is not a replacement for user-facing error UI.
```

Users should see errors in the app, not only in the console.

---

## 3. Network Panel

The Network panel shows requests made by the browser.

Use it to inspect:

- API calls
- request URL
- request method
- request headers
- query parameters
- response status
- response body
- failed requests
- image/CSS/JS loading

Common status codes:

| Status | Meaning |
| --- | --- |
| 200 | Success |
| 201 | Created |
| 400 | Bad request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not found |
| 429 | Too many requests |
| 500 | Server error |

When API Ninjas does not work, check:

```text
Was the request sent?
Is the URL correct?
Is X-Api-Key present?
What status code came back?
What does the response body say?
```

---

## 4. Application Panel

The Application panel shows browser-side storage and app resources.

Common sections:

- Local Storage
- Session Storage
- Cookies
- IndexedDB
- Cache Storage
- Service Workers

For beginner React apps, focus on:

```text
Local Storage
Session Storage
Cookies
```

---

## 5. Local Storage

Local Storage stores key-value data in the browser with no automatic expiry.

It stays after:

- page refresh
- tab close
- browser restart

Example:

```js
localStorage.setItem("theme", "dark");
const theme = localStorage.getItem("theme");
```

Use cases:

- theme preference
- saved filters
- draft form value
- simple app preference

Do not store sensitive secrets in local storage.

---

## 6. Session Storage

Session Storage also stores key-value data, but only for the current browser tab session.

It usually clears when the tab is closed.

Example:

```js
sessionStorage.setItem("lastSearch", "weather");
```

Use cases:

- temporary search state
- one-tab workflow state
- temporary form progress

---

## 7. Cookies

Cookies are small pieces of data stored by the browser and often sent with requests to the same site.

Common uses:

- login/session tokens
- user preferences
- tracking/analytics

Important cookie concepts:

| Concept | Meaning |
| --- | --- |
| Expiry | When cookie is removed |
| Domain | Which domain can use it |
| Path | Which URL path can use it |
| HttpOnly | JavaScript cannot read it |
| Secure | Sent only over HTTPS |
| SameSite | Controls cross-site sending |

For auth, secure apps often use HttpOnly cookies because frontend JavaScript cannot read them directly.

---

## 8. Storage Difference Summary

| Storage | Persists after tab close? | Sent automatically to server? | Common use |
| --- | --- | --- | --- |
| Local Storage | Yes | No | preferences, drafts |
| Session Storage | No | No | temporary tab state |
| Cookies | Depends on expiry | Yes, for matching domain/path | sessions, auth, preferences |

Rule:

```text
Do not store secrets casually in browser storage.
```

---

## 9. React Developer Tools

React Developer Tools is a browser extension.

It helps inspect:

- React component tree
- props
- state
- component re-renders

Use it when you need to answer:

```text
Which component rendered?
What props did it receive?
What state does it currently have?
```

DevTools built into the browser and React Developer Tools are different:

```text
Browser DevTools -> DOM, Console, Network, Storage
React DevTools -> React components, props, state
```

---

## 10. Debugging Flow

When your React API app is broken, use this order:

1. Check the UI.
2. Check Console for errors.
3. Check Network for the API request.
4. Check request URL, headers, and status code.
5. Check response body.
6. Check Application storage/cookies if auth or saved state is involved.
7. Check React state/props if using React Developer Tools.

Good debugging question:

```text
Is the problem in user input, state, API request, API response, storage, or rendering?
```

