# Part 2: Python Backend Basics

This lesson focuses on Python basics needed before calling APIs from backend code.

## 1. What Is `import`?

`import` allows one Python file to use code from another file or module.

Example:

```python
import math
print(math.sqrt(16))
```

If you have your own file like `helper.py`, you can also import from it.

## 2. Why Imports Matter In Backend Development

Backend applications are usually split into multiple files:

- routes
- services
- models
- utilities
- config files

`import` lets these files reuse each other cleanly.

## 3. Common Import Styles

```python
import math
from math import sqrt
from package.module import function_name
```

## 4. Exception Handling

Many beginners say try-catch, but in Python the correct structure is:

- `try`
- `except`
- `else`
- `finally`

Important note:

In languages like JavaScript, Java, or C#, people often say try-catch.
In Python, we do not use the word `catch`.
Python uses `except` instead.

So the Python version of try-catch is `try-except`.

## 5. Why Exception Handling Matters

When calling APIs, many things can fail:

- internet or network issue
- timeout
- invalid JSON
- missing key in data
- wrong data type

Instead of crashing the whole program, we handle errors gracefully.

## 6. Python Exception Blocks

- `try`: code that may fail
- `except`: what to do if an error happens
- `else`: runs if no error happens
- `finally`: runs no matter what

## 7. Detailed Meaning Of Each Block

### `try`

Put risky code here. This is code that may raise an error.

### `except`

If an error happens in the try block, Python jumps here.

You can catch specific errors like:

- `ValueError`
- `KeyError`
- `ZeroDivisionError`
- `TimeoutError`

### `else`

This runs only if the try block succeeds without any exception.

It is useful for success-only logic.

### `finally`

This always runs whether the code succeeds or fails.

It is useful for cleanup work like:

- closing files
- releasing resources
- logging final actions

## 8. Why Catching The Right Exception Matters

Good code catches specific exceptions when possible.

Better:

```python
except ValueError:
```

Too broad for most cases:

```python
except Exception:
```

Catching everything too early can hide the real problem.

## 9. API-Related Exception Examples

In backend work, exception handling is heavily used for:

- timeout handling
- invalid response parsing
- missing fields in JSON
- bad user input
- database failures
- external API failures
