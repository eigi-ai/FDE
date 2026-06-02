# 004 - State, Events, And Conditional Rendering

## State With `useState`

State is data that changes and affects the UI.

```jsx
import { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <section>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increase</button>
    </section>
  );
}
```

Flow:

```text
User clicks button
-> setCount updates state
-> React re-renders component
-> UI shows new count
```

## Events

React events are written in JSX:

```jsx
<button onClick={handleClick}>Save</button>
```

Input event:

```jsx
<input value={query} onChange={(event) => setQuery(event.target.value)} />
```

## Conditional Rendering

Conditional rendering means showing UI based on current state.

```jsx
{loading && <p>Loading...</p>}
{error && <p role="alert">{error}</p>}
{result && <ResultCard result={result} />}
```

Common UI states:

```text
idle
loading
success
error
empty
```

## Key Line

```text
State decides what the user sees.
```

