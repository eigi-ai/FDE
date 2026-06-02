# 005 - Lists, Keys, And Forms

## Lists

Use `.map()` to render arrays.

```jsx
const contacts = [
  { id: 1, name: "Asha" },
  { id: 2, name: "Rohit" },
];

function ContactList() {
  return (
    <ul>
      {contacts.map((contact) => (
        <li key={contact.id}>{contact.name}</li>
      ))}
    </ul>
  );
}
```

## Keys

`key` helps React track list items across renders.

Good:

```jsx
key={contact.id}
```

Avoid index keys if list items can be added, removed, or reordered.

## Controlled Forms

A controlled input is controlled by React state.

```jsx
const [name, setName] = useState("");

<input value={name} onChange={(event) => setName(event.target.value)} />
```

Form submit:

```jsx
function handleSubmit(event) {
  event.preventDefault();
}
```

Why controlled forms matter:

- validation
- clearing fields
- disabling submit
- sending values to APIs
- showing errors

