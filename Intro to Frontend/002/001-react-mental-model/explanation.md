# 001 - React Mental Model

## Core Idea

React helps us build frontend UI using components and state.

```text
State changes -> React re-renders UI
```

React does not replace frontend fundamentals. The browser is still the runtime, and the app still uses HTML, CSS, JavaScript, events, APIs, and state.

React gives structure to this flow:

```text
User action -> state change -> UI re-render
```

## Why React Exists

In plain JavaScript, we manually find DOM elements and update them:

```js
const message = document.querySelector("#message");
message.textContent = "Updated";
```

That works for small pages.

But large apps have:

- forms
- tables
- filters
- API calls
- loading states
- error states
- modals
- repeated UI pieces

Manual DOM updates become hard to manage.

React helps by letting us describe UI from state.

```text
Current state -> current UI
```

## React App Thinking

Think of a screen as smaller parts:

```text
ContactsPage
  PageHeader
  SearchBar
  ContactList
  ContactCard
  EmptyState
```

Each part is a component.

## Key Line

```text
React is a structured way to build UI from state.
```

