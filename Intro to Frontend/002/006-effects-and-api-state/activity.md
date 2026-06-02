# Activity - Effects And API State

## Goal

Practice `useEffect`, loading state, and API-style state.

## Task 1: Document Title Effect

Update the browser tab title when contact count changes.

Example:

```jsx
useEffect(() => {
  document.title = `Contacts (${contacts.length})`;
}, [contacts.length]);
```

## Task 2: Simulated Initial Load

Start with:

```jsx
const [contacts, setContacts] = useState([]);
const [loading, setLoading] = useState(true);
```

Use `useEffect` and `setTimeout` to simulate loading contacts after 800ms.

Show:

- loading message
- contact list after load
- empty state if loaded list is empty

## Task 3: Fake API Button

Add a button that simulates a request with success/failure.

Must show:

- loading
- success
- error

## Demo Questions

```text
Why is useEffect used for initial load?
Why is the button request handled by an event handler?
Which state controls loading and error UI?
```

