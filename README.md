# FDE Training Module

This repository is an internal learning module for FDE preparation.

FDE means Forward-Deployed Engineer.

A Forward-Deployed Engineer usually works close to real customer problems and
needs strong software fundamentals, backend understanding, API fluency, and the
ability to quickly learn and ship integrations in production-like environments.

This module is created by the eigi.ai team to help students and engineers build
the foundation required for an FDE role. It is also useful for learners who
want to refresh their programming fundamentals before moving into backend and
API-focused work.

## Module Structure

The content is arranged in learning order.

```text
fundamental_of_programming/
  01_exercise_one/
    order_payment_exercise.py
    orderpaymentsolution.py
  02_exercise_two/
    oop_concepts.py
  03_exercise_three/
    README.md
    01_api_fundamentals.py
    02_python_backend_basics.py
    03_api_calls_sdk_async.py
  04_fastapi_basics/
databases/
  nosql/
    mongodb/
      README.md
```

## What Each Module Covers

- `01_exercise_one`: Python data handling using lists, dictionaries, loops, conditions, and manual record mapping.
- `02_exercise_two`: Object-Oriented Programming in Python, including class, object, constructor, self, encapsulation, inheritance, polymorphism, and abstraction.
- `03_exercise_three`: API fundamentals before FastAPI, including HTTP basics, JSON, headers, status codes, detailed Python exception handling, imports, backend-to-backend communication, webhooks, cURL, sync vs async, and SDK concepts.
- `04_fastapi_basics`: placeholder for the next stage of training, where FastAPI concepts will be introduced after the foundations are complete.
- `databases/nosql/mongodb`: MongoDB basics for freshers, including NoSQL concepts, CRUD operations, PyMongo vs Motor, async usage, indexes, aggregation, ObjectId, DBRef, and Motor agnostic classes.

## Why This Module Exists

This training is designed to help learners build the base skills expected in an
FDE journey:

- programming fundamentals
- structured problem solving
- Python basics for backend systems
- API understanding
- system-to-system communication concepts
- readiness for FastAPI and integration workflows

## Requirements

- Python 3.10 or newer is recommended.

Check your Python version with:

```bash
python3 --version
```

## How To Run The Current Files

From the repository root:

```bash
python3 fundamental_of_programming/01_exercise_one/order_payment_exercise.py
python3 fundamental_of_programming/01_exercise_one/orderpaymentsolution.py
python3 fundamental_of_programming/02_exercise_two/oop_concepts.py
python3 fundamental_of_programming/03_exercise_three/01_api_fundamentals.py
python3 fundamental_of_programming/03_exercise_three/02_python_backend_basics.py
python3 fundamental_of_programming/03_exercise_three/03_api_calls_sdk_async.py
```

Database tutorials are documentation-first modules and can be read directly from their README files.

## Training Flow

The intended learning path is:

1. Start with core Python logic and data handling.
2. Move into Object-Oriented Programming.
3. Learn API and backend fundamentals before FastAPI.
4. Learn database basics, starting with MongoDB.
5. Then begin FastAPI training.

## Notes

- Generated Python cache files are ignored through `.gitignore`.
- Local virtual environments are also ignored.
- Exercise 4 is intentionally kept as the next learning stage placeholder.
