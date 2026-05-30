# Chapter 2: Python Libraries For MongoDB

This chapter explains the Python libraries commonly used to work with MongoDB.

The important libraries are:

- `pymongo`
- `motor`
- `odmantic`

## 1. Install The Libraries

```bash
pip install pymongo motor odmantic
```

In a real project, add them to `requirements.txt`:

```text
pymongo
motor
odmantic
```

## 2. What Is PyMongo?

PyMongo is the official synchronous Python driver for MongoDB.

Synchronous means each database operation waits until MongoDB returns a result before the next line continues.

PyMongo is good for:

- scripts
- command-line tools
- data migration jobs
- small synchronous applications
- learning MongoDB commands for the first time

Example:

```python
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017")
db = client["training_db"]
records_collection = db["records"]

record = records_collection.find_one({"title": "MongoDB first note"})
print(record)
```

## 3. What Is Motor?

Motor is the official asynchronous Python driver for MongoDB.

Motor supports `async` and `await`.

It is commonly seen in async Python backend projects that use:

- FastAPI
- Starlette
- aiohttp
- Tornado

Example:

```python
from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["training_db"]
records_collection = db["records"]


async def get_record(title: str):
    record = await records_collection.find_one({"title": title})
    return record
```

## 4. Sync Vs Async

Synchronous code blocks while it waits.

Asynchronous code can wait for input/output work without blocking the whole event loop.

Database calls are input/output operations because the Python app sends a request to MongoDB and waits for a response.

Simple idea:

```text
sync:  request -> wait -> response -> next task
async: request -> wait without blocking everything -> response
```

## 5. PyMongo Vs Motor

| Topic                | PyMongo                           | Motor                                                |
| -------------------- | --------------------------------- | ---------------------------------------------------- |
| Execution style      | Synchronous                       | Asynchronous                                         |
| Uses `await`         | No                                | Yes                                                  |
| Best for             | Scripts and sync apps             | Async APIs and services                              |
| FastAPI async routes | Can block if used directly        | Works naturally with async routes                    |
| Import example       | `from pymongo import MongoClient` | `from motor.motor_asyncio import AsyncIOMotorClient` |
| Common result style  | Direct result                     | Awaitable result or async cursor                     |

## 6. Why Do We Choose Motor?

In this training, we use Motor because learners are also learning FastAPI and async Python.

Motor is useful because:

- it supports `async` and `await`
- it fits naturally inside `async def` FastAPI routes
- it avoids blocking the event loop during MongoDB calls
- it can handle concurrent API requests efficiently
- its function names are similar to PyMongo, so learning can transfer easily

Important note:

MongoDB driver recommendations can change over time. Motor is still important to understand because many existing FastAPI projects use it, but for new production work always check the current MongoDB Python driver guidance used by the team.

## 7. What Is An ODM?

ODM means Object Document Mapper.

An ODM lets us work with MongoDB documents using Python classes instead of raw dictionaries everywhere.

Without ODM:

```python
record = {
    "title": "MongoDB first note",
    "status": "active",
    "priority": 1,
}
```

With ODM:

```python
record = Record(
    title="MongoDB first note",
    status="active",
    priority=1,
)
```

Why ODMs are useful:

- they make models easier to read
- they provide validation
- they reduce repeated dictionary handling
- they keep database document structure clearer
- they work nicely with type hints

## 8. What Is ODMantic?

ODMantic is an asynchronous ODM for MongoDB.

It is built on top of:

- Motor for async MongoDB communication
- Pydantic for data validation and model parsing

ODMantic is useful when we want model-based MongoDB code in async Python projects.

Example ODMantic model:

```python
from odmantic import Model


class Record(Model):
    title: str
    status: str = "active"
    priority: int = 1
```

Example ODMantic engine:

```python
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine


client = AsyncIOMotorClient("mongodb://localhost:27017")
engine = AIOEngine(client=client, database="training_db")
```

Insert one record:

```python
async def create_record():
    record = Record(
        title="MongoDB first note",
        status="active",
        priority=1,
    )

    saved_record = await engine.save(record)
    return saved_record
```

Find one record:

```python
async def get_record_by_title(title: str):
    record = await engine.find_one(Record, Record.title == title)
    return record
```

Find many records:

```python
async def get_active_records():
    records = await engine.find(Record, Record.status == "active")
    return records
```

Delete one record:

```python
async def delete_record(record: Record):
    await engine.delete(record)
```

## 9. PyMongo Vs Motor Vs ODMantic

| Topic          | PyMongo               | Motor                                     | ODMantic                                         |
| -------------- | --------------------- | ----------------------------------------- | ------------------------------------------------ |
| Style          | Raw driver            | Async raw driver                          | Async ODM                                        |
| Uses `await`   | No                    | Yes                                       | Yes                                              |
| Data shape     | Dictionaries          | Dictionaries                              | Python model classes                             |
| Validation     | Manual                | Manual or Pydantic separately             | Pydantic-based models                            |
| Best for       | Sync scripts and apps | Async APIs needing direct MongoDB control | Async APIs that prefer model-based database code |
| Example import | `MongoClient`         | `AsyncIOMotorClient`                      | `Model`, `AIOEngine`                             |

Simple rule:

- use PyMongo for synchronous low-level MongoDB code
- use Motor for asynchronous low-level MongoDB code
- use ODMantic when you want async MongoDB plus Pydantic-style models

Important note:

ODMantic is helpful, but beginners should still understand MongoDB and Motor basics first. ODMantic hides some low-level details, and those details are important when debugging real backend issues.

## 10. Basic Motor Connection

```python
from motor.motor_asyncio import AsyncIOMotorClient


MONGODB_URL = "mongodb://localhost:27017"
DATABASE_NAME = "training_db"

client = AsyncIOMotorClient(MONGODB_URL)
database = client[DATABASE_NAME]
records_collection = database["records"]
```

Important objects:

- `AsyncIOMotorClient`: connection to MongoDB server
- `database`: selected database
- `records_collection`: selected collection

## 11. Environment Variables

Do not hardcode real database credentials in code.

Use environment variables.

Example `.env`:

```text
MONGODB_URL=mongodb+srv://username:password@cluster-name.mongodb.net/
MONGODB_DATABASE=training_db
```

Example Python usage:

```python
import os


MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "training_db")
```

## 12. Recommended FastAPI Pattern

Keep the MongoDB client in one database file.

Example `database.py`:

```python
import os

from motor.motor_asyncio import AsyncIOMotorClient


MONGODB_URL = os.getenv("MONGODB_URL")
MONGODB_DATABASE = os.getenv("MONGODB_DATABASE", "training_db")

client = AsyncIOMotorClient(MONGODB_URL)
database = client[MONGODB_DATABASE]
```

Example usage:

```python
from database import database


records_collection = database["records"]


async def get_record_by_title(title: str):
    return await records_collection.find_one({"title": title})
```

## 13. What Is The Agnostic Thing In Motor?

In Motor documentation and source code, you may see names like:

- `AgnosticClient`
- `AgnosticDatabase`
- `AgnosticCollection`
- `AgnosticCursor`

Here, agnostic means not tied to one async framework.

Motor has shared core classes that describe MongoDB behavior in a framework-independent way. Then Motor exposes framework-specific clients such as:

- `motor.motor_asyncio.AsyncIOMotorClient` for Python `asyncio`
- `motor.motor_tornado.MotorClient` for Tornado

As a beginner using FastAPI, normally use this:

```python
from motor.motor_asyncio import AsyncIOMotorClient
```

Do not directly use this in normal beginner projects:

```python
from motor.core import AgnosticClient
```

Simple explanation:

- agnostic classes are Motor's shared internal layer
- `AsyncIOMotorClient` is the practical class used in FastAPI-style async projects

## 14. Quick Revision

- PyMongo is synchronous.
- Motor is asynchronous.
- ODMantic is an async ODM built on Motor and Pydantic.
- Motor supports `async` and `await`.
- Async FastAPI projects commonly use Motor-style database calls.
- ODMantic is useful when we want model-based MongoDB code.
- Use environment variables for MongoDB URLs.
- Beginners should use `AsyncIOMotorClient`, not Motor agnostic classes directly.
