# Activity - Build A Responsive Dashboard Layout

## Goal

Practice responsive layout, reusable UI components, and readable form styling.

## Task

Improve your routed app with a clean dashboard layout.

## Requirements

Create:

- shared `AppShell`
- `PageHeader`
- reusable `StatCard`
- reusable `TextField`
- responsive dashboard grid
- form layout with visible labels
- focus styles for links, buttons, and inputs
- mobile-friendly page behavior

## Suggested Dashboard Content

Add at least 4 dashboard cards:

```text
Applications
Interviews
Selected
Pending Tasks
```

Render them from an array:

```tsx
const stats = [
  { label: "Applications", value: 24, helperText: "This month" },
  { label: "Interviews", value: 6, helperText: "Scheduled" },
  { label: "Selected", value: 2, helperText: "Final round" },
  { label: "Pending Tasks", value: 5, helperText: "Need action" },
];
```

Use `.map()`:

```tsx
{stats.map((stat) => (
  <StatCard
    key={stat.label}
    label={stat.label}
    value={stat.value}
    helperText={stat.helperText}
  />
))}
```

## CSS Requirements

Your CSS should include:

- page max width
- consistent spacing
- responsive grid using `auto-fit` or media queries
- form field spacing
- button styles
- visible focus styles

## Manual Checks

Check:

- dashboard on desktop width
- dashboard on mobile width
- form labels are visible
- text does not overflow
- keyboard focus is visible
- repeated UI is built from reusable components

## Demo Questions

Be ready to answer:

1. Which component is your reusable card?
2. Which component is your reusable form field?
3. Which CSS rule makes the grid responsive?
4. What changes on mobile width?
5. Why are visible labels important?

