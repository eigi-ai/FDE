# 007 - Custom Hooks

## What Is A Custom Hook?

A custom hook is a reusable function that uses React hooks.

Custom hook names start with `use`.

Example:

```jsx
function useToggle(initialValue = false) {
  const [value, setValue] = useState(initialValue);

  function toggle() {
    setValue((currentValue) => !currentValue);
  }

  return { value, toggle };
}
```

Use it:

```jsx
const { value: isOpen, toggle } = useToggle(false);
```

## Why Use Custom Hooks?

Use custom hooks when logic is:

- repeated
- hard to read inside a component
- useful across components
- a clear behavior by itself

Examples:

```text
useToggle
useLocalStorage
useDebouncedValue
useApiSearch
```

Do not create custom hooks too early. First build the logic. Extract a hook when it improves clarity or reuse.

