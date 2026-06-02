# 002 - JSX And Components

## JSX

JSX is JavaScript syntax that looks like HTML.

```jsx
function Greeting() {
  return <h1>Hello React</h1>;
}
```

JSX lets us write UI inside JavaScript.

## Important JSX Rules

Use `className`, not `class`:

```jsx
<div className="card">Contact</div>
```

Use `htmlFor`, not `for`:

```jsx
<label htmlFor="email">Email</label>
<input id="email" />
```

Use braces for JavaScript values:

```jsx
const name = "Asha";
return <h1>Hello {name}</h1>;
```

Return one parent element:

```jsx
function Card() {
  return (
    <article>
      <h2>Title</h2>
      <p>Description</p>
    </article>
  );
}
```

## Components

A component is a JavaScript function that returns UI.

```jsx
function ContactCard() {
  return (
    <article>
      <h2>Asha Mehta</h2>
      <p>asha@example.com</p>
    </article>
  );
}
```

Component names must start with capital letters.

Good:

```jsx
function ContactCard() {}
```

Bad:

```jsx
function contactCard() {}
```

