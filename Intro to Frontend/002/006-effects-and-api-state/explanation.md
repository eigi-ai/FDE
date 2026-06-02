# 006 - Effects And API State

## `useEffect`

`useEffect` runs code after React renders.

Use it to synchronize with something outside React:

- document title
- initial data load
- timers
- subscriptions
- browser APIs

Example:

```jsx
useEffect(() => {
  document.title = `Contacts (${contacts.length})`;
}, [contacts.length]);
```

The effect runs when `contacts.length` changes.

## When To Use `useEffect`

Good use:

```text
Load initial data when page opens.
Update document title when state changes.
Set up and clean up timers.
```

Bad use:

```text
Putting every user action inside useEffect.
```

User-triggered API calls usually belong in event handlers.

## API State

API screens usually need:

```jsx
const [data, setData] = useState(null);
const [loading, setLoading] = useState(false);
const [error, setError] = useState("");
```

API flow:

```text
set loading true
clear old error
call API
store response or error
set loading false
re-render UI
```

