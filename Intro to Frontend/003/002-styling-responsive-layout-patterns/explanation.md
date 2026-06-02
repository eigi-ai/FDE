# 002 - Styling, Responsive Layout, And Reusable UI Patterns

## Goal

Learn how to make a React app readable, responsive, and reusable.

Core idea:

```text
layout controls structure
components control repeated UI
CSS controls spacing, alignment, and responsive behavior
```

## What Good App UI Needs

A frontend app should not only work. It should also be easy to scan and use.

Focus on:

- spacing
- alignment
- page width
- readable forms
- responsive grids
- reusable cards
- reusable form fields
- clear loading/error/success states
- keyboard focus styles

Do not start with decoration. Start with structure.

## Page Layout

A common app layout looks like this:

```text
AppShell
  Header
  Navigation
  Main page area
    PageHeader
    Page sections
    Cards/forms/lists
```

Example:

```tsx
export function PageHeader() {
  return (
    <div className="page-header">
      <p className="eyebrow">Dashboard</p>
      <h1>Candidate Overview</h1>
      <p>Track profile status, API data, and settings.</p>
    </div>
  );
}
```

## Responsive Page Width

```css
.page {
  width: min(1120px, 100%);
  margin: 0 auto;
  padding: 24px;
}
```

This means:

```text
Use 1120px max width on large screens.
Use full width on smaller screens.
Keep 24px padding inside the page.
```

## Responsive Grid

```css
.metric-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 16px;
}
```

This creates a grid that adapts to screen size.

On wide screens:

```text
cards can sit side by side
```

On narrow screens:

```text
cards stack automatically
```

## Reusable Card Component

```tsx
type StatCardProps = {
  label: string;
  value: string | number;
  helperText?: string;
};

export function StatCard({ label, value, helperText }: StatCardProps) {
  return (
    <article className="stat-card">
      <span>{label}</span>
      <strong>{value}</strong>
      {helperText ? <small>{helperText}</small> : null}
    </article>
  );
}
```

Use it like:

```tsx
<StatCard label="Applications" value={24} helperText="This month" />
<StatCard label="Interviews" value={6} helperText="Scheduled" />
```

## Reusable Form Field

```tsx
type TextFieldProps = {
  id: string;
  label: string;
  value: string;
  error?: string;
  onChange: (value: string) => void;
};

export function TextField({ id, label, value, error, onChange }: TextFieldProps) {
  return (
    <div className="field">
      <label htmlFor={id}>{label}</label>
      <input
        id={id}
        value={value}
        aria-invalid={Boolean(error)}
        onChange={(event) => onChange(event.target.value)}
      />
      {error ? <p className="field-error">{error}</p> : null}
    </div>
  );
}
```

Visible labels matter because:

- users know what the field is for
- screen readers can identify the field
- tests can find fields by label
- placeholders disappear when users type

## Focus Styles

Keyboard users need visible focus.

```css
button:focus-visible,
a:focus-visible,
input:focus-visible {
  outline: 3px solid #2563eb;
  outline-offset: 2px;
}
```

## Key Line

```text
Reusable UI means repeated structure becomes a component, and repeated spacing becomes a CSS pattern.
```

