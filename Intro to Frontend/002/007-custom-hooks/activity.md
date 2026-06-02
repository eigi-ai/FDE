# Activity - Extract A Custom Hook

## Goal

Practice moving reusable stateful logic into a custom hook.

## Choose One

### Option A: `useToggle`

Use it for show/hide help panel.

Expected use:

```jsx
const { value: showHelp, toggle } = useToggle(false);
```

### Option B: `useLocalStorage`

Save search text in local storage.

Expected use:

```jsx
const [search, setSearch] = useLocalStorage("contact-search", "");
```

### Option C: `useDebouncedValue`

Delay search filtering while user types.

Expected use:

```jsx
const debouncedSearch = useDebouncedValue(search, 300);
```

## Requirements

- hook name starts with `use`
- hook uses at least one React hook
- component imports and uses the custom hook
- candidate can explain why the hook exists

## Demo Questions

```text
What logic did you move into the custom hook?
Which component uses it?
Does the hook improve reuse or readability?
```

