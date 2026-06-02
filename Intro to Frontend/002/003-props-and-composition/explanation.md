# 003 - Props And Composition

## Props

Props are inputs passed from a parent component to a child component.

```jsx
function ContactCard({ name, email }) {
  return (
    <article>
      <h2>{name}</h2>
      <p>{email}</p>
    </article>
  );
}
```

Use it:

```jsx
<ContactCard name="Asha Mehta" email="asha@example.com" />
```

## Why Props Matter

Without props, components are hardcoded.

With props, components are reusable.

```jsx
<ContactCard name="Asha" email="asha@example.com" />
<ContactCard name="Rohit" email="rohit@example.com" />
```

## Composition

Composition means building larger UI by combining smaller components.

```jsx
function ContactsPage() {
  return (
    <main>
      <PageHeader title="Contacts" />
      <ContactList contacts={contacts} />
    </main>
  );
}
```

## Key Rule

```text
Props are read-only inside the child component.
```

The child receives props and renders UI. It should not mutate props.

