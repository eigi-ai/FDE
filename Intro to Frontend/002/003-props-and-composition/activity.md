# Activity - Make Components Reusable With Props

## Goal

Practice passing data from parent to child components.

## Task

Take the static contact screen from the previous activity and remove hardcoded contact data from `ContactCard`.

## Required Data

Use this array in the parent component:

```js
const contacts = [
  { id: 1, name: "Asha Mehta", email: "asha@example.com", status: "Lead" },
  { id: 2, name: "Rohit Sharma", email: "rohit@example.com", status: "Customer" },
  { id: 3, name: "Neha Verma", email: "neha@example.com", status: "Follow-up" },
];
```

## Requirements

- `ContactList` receives `contacts` as a prop.
- `ContactCard` receives one contact as props.
- Render all contacts.
- Do not hardcode names inside `ContactCard`.

## Demo Questions

```text
Which component owns the contacts array?
Which component receives the data?
Why are props useful here?
```

