# Chapter 5: Pagination, Filtering, Search, And Query Patterns

This chapter teaches pagination and filtering step by step, starting from zero.

By the end of this chapter, you will understand:

- how to filter data by city, first name, last name, or any field
- how to build a search that works like Google search
- how to split results into pages
- how to combine filters with search and pagination in a real API

---

## 1. The Problem Pagination Solves

Imagine your `users` collection has 50,000 users.

If an API returns all 50,000 users at once:

- the server takes much longer to send the response
- the client takes much longer to receive and display it
- the browser or mobile app may crash trying to show that much data

That is why we split results into pages.

Think of how Google works:

- you search for something
- Google shows you 10 results on page 1
- if you click page 2, it shows the next 10
- it never shows you all results at the same time

That is exactly what pagination does.

---

## 2. Sample Data We Will Use

Throughout this chapter we will work with a `users` collection.

Each document in the collection looks like this:

```json
{
  "_id": "6655a9b5b82f41d9dcd2f410",
  "first_name": "Neha",
  "last_name": "Sharma",
  "email": "neha.sharma@example.com",
  "city": "Pune",
  "state": "Maharashtra",
  "age": 28,
  "role": "doctor",
  "is_active": true
}
```

Fields:

- `first_name`: user's first name
- `last_name`: user's last name
- `email`: user's email
- `city`: the city they are in
- `state`: the state they are in
- `age`: numeric age
- `role`: their role such as doctor, admin, or patient
- `is_active`: whether the user account is active

This is a realistic user document. We will build filters, search, and pagination on top of it.

---

## 3. Setting Up The Connection

```python
from motor.motor_asyncio import AsyncIOMotorClient


client = AsyncIOMotorClient("mongodb://localhost:27017")
database = client["training_db"]
users_collection = database["users"]
```

Everything in this chapter uses `users_collection`.

---

## 4. Filtering By City

The most basic filter is an exact match.

Find all users from Pune:

```python
async def get_users_in_pune():
    cursor = users_collection.find({"city": "Pune"})
    users = await cursor.to_list(length=100)
    return users
```

What is happening here:

- `{"city": "Pune"}` is the filter
- MongoDB looks at every document in the collection
- if the `city` field equals `"Pune"`, the document is included
- `to_list(length=100)` collects up to 100 matching documents

Find all users from Mumbai:

```python
async def get_users_in_mumbai():
    cursor = users_collection.find({"city": "Mumbai"})
    users = await cursor.to_list(length=100)
    return users
```

---

## 5. Filtering By Multiple Cities At Once

If you want users from more than one city, use `$in`.

`$in` means "value must be in this list".

```python
async def get_users_in_maharashtra_cities():
    cursor = users_collection.find({
        "city": {"$in": ["Pune", "Mumbai", "Nagpur", "Nashik"]},
    })
    users = await cursor.to_list(length=100)
    return users
```

Think of it like this: you are asking MongoDB "show me all users where city is Pune OR Mumbai OR Nagpur OR Nashik".

---

## 6. Filtering By First Name

Find all users whose first name is exactly "Neha":

```python
async def get_users_named_neha():
    cursor = users_collection.find({"first_name": "Neha"})
    users = await cursor.to_list(length=100)
    return users
```

Find users by first name, passed in as a variable:

```python
async def get_users_by_first_name(first_name: str):
    cursor = users_collection.find({"first_name": first_name})
    users = await cursor.to_list(length=100)
    return users
```

---

## 7. Filtering By Last Name

```python
async def get_users_by_last_name(last_name: str):
    cursor = users_collection.find({"last_name": last_name})
    users = await cursor.to_list(length=100)
    return users
```

---

## 8. Filtering By Both First Name And Last Name

When you provide both, MongoDB checks both conditions at the same time.

This is like typing a full name into a search box.

```python
async def get_user_by_full_name(first_name: str, last_name: str):
    cursor = users_collection.find({
        "first_name": first_name,
        "last_name": last_name,
    })
    users = await cursor.to_list(length=50)
    return users
```

When you write multiple key-value pairs in the filter dictionary, MongoDB requires all of them to match. This is the same as saying AND.

So `{"first_name": "Neha", "last_name": "Sharma"}` means:
"show me all documents where first_name is Neha AND last_name is Sharma".

---

## 9. Case-Insensitive Partial Search (Google-Style Search)

This is the most important section for freshers.

When you type in a search box, you usually do not type the full exact name. You might type "neh" and expect to see "Neha" or "Nehal". That is called a partial match.

MongoDB handles this using `$regex`.

`$regex` means regular expression. A regular expression is a pattern used to match text.

For freshers, the only thing you need to know right now is:

- `$regex: "neh"` means "match any value that contains the letters neh"
- `"$options": "i"` means ignore uppercase and lowercase differences

Search by first name, partial, case-insensitive:

```python
async def search_users_by_first_name(search_text: str):
    cursor = users_collection.find({
        "first_name": {
            "$regex": search_text,
            "$options": "i",
        },
    })
    users = await cursor.to_list(length=100)
    return users
```

If `search_text` is `"neh"`, this matches:

- "Neha"
- "Nehal"
- "Nehali"

If `search_text` is `"NEHA"`, it still works because `"$options": "i"` makes it case-insensitive.

Search by last name:

```python
async def search_users_by_last_name(search_text: str):
    cursor = users_collection.find({
        "last_name": {
            "$regex": search_text,
            "$options": "i",
        },
    })
    users = await cursor.to_list(length=100)
    return users
```

---

## 10. Google-Style Search Across Multiple Fields

Real search boxes search across multiple fields at the same time.

For example, if someone types "sharma pune", you might want to match users where first_name or last_name or city contains "sharma" or "pune".

But a simpler common approach: search across first_name, last_name, and city with one search term using `$or`.

```python
async def search_users(search_text: str):
    pattern = {"$regex": search_text, "$options": "i"}

    cursor = users_collection.find({
        "$or": [
            {"first_name": pattern},
            {"last_name": pattern},
            {"email": pattern},
            {"city": pattern},
        ],
    })
    users = await cursor.to_list(length=100)
    return users
```

What is happening:

- `pattern` is a dictionary with the regex pattern and the case-insensitive option
- `$or` means "match if at least one of these conditions is true"
- MongoDB will return a user if their first_name, last_name, email, or city contains the search text

So if someone types "sharma", they get back all users named Sharma, or who live in a place with "sharma" in it, or have sharma in their email.

This is how many basic search boxes work.

---

## 11. Combining City Filter With Search

A real API lets users filter AND search at the same time.

Example: show me all active doctors in Pune whose name contains "neh".

```python
async def search_doctors_in_city(city: str, search_text: str):
    pattern = {"$regex": search_text, "$options": "i"}

    cursor = users_collection.find({
        "city": city,
        "role": "doctor",
        "is_active": True,
        "$or": [
            {"first_name": pattern},
            {"last_name": pattern},
        ],
    })
    users = await cursor.to_list(length=100)
    return users
```

Breaking this down:

- `"city": city` means the user must be in the given city (exact match)
- `"role": "doctor"` means the user must be a doctor (exact match)
- `"is_active": True` means the account must be active (exact match)
- `"$or": [...]` means at least one of the name conditions must match

All conditions are joined with AND. So MongoDB requires city AND role AND is_active to match, and then also at least one of the $or conditions.

---

## 12. What Is Pagination?

Before writing code, understand the mental model.

Think of a page of a book:

- page 1 has items 1 to 10
- page 2 has items 11 to 20
- page 3 has items 21 to 30

In MongoDB, we control this using two things:

- `skip`: how many documents to jump over before starting to read
- `limit`: how many documents to read

Formula:

```text
skip = (page - 1) * page_size
```

Examples:

| page | page_size | skip |
| ---- | --------- | ---- |
| 1    | 10        | 0    |
| 2    | 10        | 10   |
| 3    | 10        | 20   |
| 4    | 10        | 30   |

For page 1: skip 0 documents, take 10.
For page 2: skip the first 10 documents, take the next 10.
For page 3: skip the first 20 documents, take the next 10.

---

## 13. Basic Pagination Example

Get all users, page by page:

```python
async def get_users_page(page: int = 1, page_size: int = 10):
    # make sure page number is at least 1
    page = max(page, 1)
    # keep page_size between 1 and 100
    page_size = min(max(page_size, 1), 100)

    skip = (page - 1) * page_size

    cursor = (
        users_collection
        .find({})                    # no filter, get all users
        .sort("first_name", 1)      # sort alphabetically by first name
        .skip(skip)                  # jump over previous pages
        .limit(page_size)            # take only this many documents
    )

    users = await cursor.to_list(length=page_size)
    total = await users_collection.count_documents({})

    return {
        "page": page,
        "page_size": page_size,
        "total": total,
        "items": users,
    }
```

Example API call:

```text
GET /users?page=1&page_size=10   -> first 10 users
GET /users?page=2&page_size=10   -> next 10 users
GET /users?page=3&page_size=10   -> next 10 users
```

---

## 14. Total Pages Calculation

Knowing total pages lets the frontend show page buttons.

```python
import math


def total_pages(total: int, page_size: int) -> int:
    if page_size <= 0:
        return 0
    return math.ceil(total / page_size)
```

Examples:

- 35 users, 10 per page: `ceil(35 / 10) = 4` pages
- 30 users, 10 per page: `ceil(30 / 10) = 3` pages
- 1 user, 10 per page: `ceil(1 / 10) = 1` page

---

## 15. Pagination With City Filter

Get users from a specific city, paginated:

```python
import math


async def get_users_by_city_paginated(
    city: str,
    page: int = 1,
    page_size: int = 10,
):
    page = max(page, 1)
    page_size = min(max(page_size, 1), 100)
    skip = (page - 1) * page_size

    filter_query = {"city": city, "is_active": True}

    cursor = (
        users_collection
        .find(filter_query)
        .sort("first_name", 1)
        .skip(skip)
        .limit(page_size)
    )

    users = await cursor.to_list(length=page_size)
    total = await users_collection.count_documents(filter_query)

    return {
        "city": city,
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": math.ceil(total / page_size),
        "items": users,
    }
```

Example API calls:

```text
GET /users?city=Pune&page=1&page_size=10   -> page 1 of users in Pune
GET /users?city=Pune&page=2&page_size=10   -> page 2 of users in Pune
GET /users?city=Mumbai&page=1&page_size=10 -> page 1 of users in Mumbai
```

---

## 16. Pagination With Name Search

Search users by name (partial, case-insensitive), paginated:

```python
import math


async def search_users_paginated(
    search: str = "",
    page: int = 1,
    page_size: int = 10,
):
    page = max(page, 1)
    page_size = min(max(page_size, 1), 100)
    skip = (page - 1) * page_size

    # if search is empty, return all users
    # if search has text, apply regex filter
    if search.strip():
        pattern = {"$regex": search.strip(), "$options": "i"}
        filter_query = {
            "$or": [
                {"first_name": pattern},
                {"last_name": pattern},
            ],
        }
    else:
        filter_query = {}

    cursor = (
        users_collection
        .find(filter_query)
        .sort("first_name", 1)
        .skip(skip)
        .limit(page_size)
    )

    users = await cursor.to_list(length=page_size)
    total = await users_collection.count_documents(filter_query)

    return {
        "search": search,
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": math.ceil(total / page_size),
        "items": users,
    }
```

Example API calls:

```text
GET /users?search=neh&page=1    -> page 1 of users whose name contains "neh"
GET /users?search=sharma&page=1 -> page 1 of users with "sharma" in first or last name
GET /users?search=&page=1       -> page 1 of all users (no filter)
```

---

## 17. Full Realistic Pagination With All Filters

This is what a real production-style search + filter + pagination function looks like.

It combines:

- city filter
- role filter
- Google-style name or email search
- pagination
- total pages

```python
import math


async def search_and_filter_users(
    city: str = "",
    role: str = "",
    search: str = "",
    page: int = 1,
    page_size: int = 10,
):
    page = max(page, 1)
    page_size = min(max(page_size, 1), 100)
    skip = (page - 1) * page_size

    # start with an empty filter
    filter_query = {}

    # add city filter only if city is provided
    if city.strip():
        filter_query["city"] = city.strip()

    # add role filter only if role is provided
    if role.strip():
        filter_query["role"] = role.strip()

    # add search filter only if search text is provided
    if search.strip():
        pattern = {"$regex": search.strip(), "$options": "i"}
        filter_query["$or"] = [
            {"first_name": pattern},
            {"last_name": pattern},
            {"email": pattern},
            {"city": pattern},
        ]

    cursor = (
        users_collection
        .find(filter_query, {"_id": 0, "first_name": 1, "last_name": 1, "email": 1, "city": 1, "role": 1})
        .sort("first_name", 1)
        .skip(skip)
        .limit(page_size)
    )

    users = await cursor.to_list(length=page_size)
    total = await users_collection.count_documents(filter_query)

    return {
        "filters": {
            "city": city,
            "role": role,
            "search": search,
        },
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": math.ceil(total / page_size) if total > 0 else 0,
        "items": users,
    }
```

Example API calls:

```text
# Page 1 of all active doctors in Pune
GET /users?city=Pune&role=doctor&page=1

# Search for "neh" across all cities
GET /users?search=neh&page=1

# All doctors, page 2
GET /users?role=doctor&page=2

# Doctors in Mumbai named something with "sha"
GET /users?city=Mumbai&role=doctor&search=sha&page=1
```

Example response:

```json
{
  "filters": {
    "city": "Pune",
    "role": "doctor",
    "search": ""
  },
  "page": 1,
  "page_size": 10,
  "total": 35,
  "total_pages": 4,
  "items": [
    {
      "first_name": "Aarav",
      "last_name": "Kulkarni",
      "email": "aarav.kulkarni@example.com",
      "city": "Pune",
      "role": "doctor"
    }
  ]
}
```

---

## 18. Full FastAPI Route With Filters And Pagination

This is how the above function looks as an actual FastAPI endpoint:

```python
import math
from fastapi import FastAPI, Query
from motor.motor_asyncio import AsyncIOMotorClient


app = FastAPI()

client = AsyncIOMotorClient("mongodb://localhost:27017")
database = client["training_db"]
users_collection = database["users"]


@app.get("/users")
async def list_users(
    city: str = Query(default=""),
    role: str = Query(default=""),
    search: str = Query(default=""),
    page: int = Query(default=1, ge=1),
    page_size: int = Query(default=10, ge=1, le=100),
):
    skip = (page - 1) * page_size

    filter_query = {}

    if city.strip():
        filter_query["city"] = city.strip()

    if role.strip():
        filter_query["role"] = role.strip()

    if search.strip():
        pattern = {"$regex": search.strip(), "$options": "i"}
        filter_query["$or"] = [
            {"first_name": pattern},
            {"last_name": pattern},
            {"email": pattern},
        ]

    cursor = (
        users_collection
        .find(filter_query, {"_id": 0, "first_name": 1, "last_name": 1, "email": 1, "city": 1, "role": 1})
        .sort("first_name", 1)
        .skip(skip)
        .limit(page_size)
    )

    users = await cursor.to_list(length=page_size)
    total = await users_collection.count_documents(filter_query)

    return {
        "page": page,
        "page_size": page_size,
        "total": total,
        "total_pages": math.ceil(total / page_size) if total > 0 else 0,
        "items": users,
    }
```

---

## 19. Cursor-Based Pagination (Advanced)

Skip and limit work well for small and medium collections.

But when a collection has millions of documents, using a large `skip` becomes slow. MongoDB still has to count through all skipped documents one by one.

Cursor-based pagination solves this by remembering where the last page ended.

Think of it like this:

- page 1 ends at user with id "abc"
- to get page 2, we say "give me users that come after id abc"
- MongoDB goes directly to that point instead of counting from the start

Example:

```python
from bson import ObjectId


async def get_users_after_id(
    last_id: str | None = None,
    limit: int = 10,
):
    limit = min(max(limit, 1), 100)

    filter_query = {}

    # if a last_id was given, only return documents that come before it
    # we use $lt because ObjectId values contain a timestamp
    # documents inserted earlier have smaller ObjectId values
    if last_id:
        filter_query["_id"] = {"$lt": ObjectId(last_id)}

    cursor = (
        users_collection
        .find(filter_query)
        .sort("_id", -1)     # newest first
        .limit(limit)
    )

    users = await cursor.to_list(length=limit)

    # give the client the id of the last document so they can request the next page
    next_cursor = str(users[-1]["_id"]) if users else None

    return {
        "items": users,
        "next_cursor": next_cursor,
    }
```

Client usage:

```text
# first page, no last_id
GET /users?limit=10

# server returns next_cursor = "6655a9b5b82f41d9dcd2f410"

# second page, pass next_cursor as last_id
GET /users?limit=10&last_id=6655a9b5b82f41d9dcd2f410

# continue until next_cursor is null, meaning no more pages
```

---

## 20. Query Operators Reference

These are the most common MongoDB query operators.

### Comparison

| Operator | Meaning                | Python Example                          |
| -------- | ---------------------- | --------------------------------------- |
| `$eq`    | Equal to               | `{"age": {"$eq": 25}}`                  |
| `$ne`    | Not equal to           | `{"role": {"$ne": "admin"}}`            |
| `$gt`    | Greater than           | `{"age": {"$gt": 18}}`                  |
| `$gte`   | Greater than or equal  | `{"age": {"$gte": 18}}`                 |
| `$lt`    | Less than              | `{"age": {"$lt": 60}}`                  |
| `$lte`   | Less than or equal     | `{"age": {"$lte": 60}}`                 |
| `$in`    | Value is in a list     | `{"city": {"$in": ["Pune", "Mumbai"]}}` |
| `$nin`   | Value is not in a list | `{"role": {"$nin": ["blocked"]}}`       |

### Logical

| Operator | Meaning                           | Python Example                                          |
| -------- | --------------------------------- | ------------------------------------------------------- |
| `$and`   | All conditions must match         | `{"$and": [{"age": {"$gt": 18}}, {"is_active": True}]}` |
| `$or`    | At least one condition must match | `{"$or": [{"city": "Pune"}, {"city": "Mumbai"}]}`       |
| `$not`   | Condition must not match          | `{"age": {"$not": {"$lt": 18}}}`                        |

### Text Matching

| Operator | Meaning                   | Python Example                                       |
| -------- | ------------------------- | ---------------------------------------------------- |
| `$regex` | Pattern match in a string | `{"first_name": {"$regex": "neh", "$options": "i"}}` |

Regex `$options`:

- `"i"` = case-insensitive
- `"m"` = treat string as multi-line

---

## 21. Sorting

Sort ascending (A to Z, smallest to largest):

```python
cursor = users_collection.find({}).sort("first_name", 1)
```

Sort descending (Z to A, largest to smallest):

```python
cursor = users_collection.find({}).sort("created_at", -1)
```

Sort by multiple fields (first by city, then by first name within the same city):

```python
cursor = users_collection.find({}).sort([("city", 1), ("first_name", 1)])
```

---

## 22. Projection (Choosing Which Fields To Return)

Projection means telling MongoDB which fields to include or exclude in the result.

Why use projection:

- reduce response size
- hide sensitive fields like passwords
- return only what the API needs

Include specific fields:

```python
# only return first_name, last_name, city. exclude _id.
cursor = users_collection.find(
    {"city": "Pune"},
    {"first_name": 1, "last_name": 1, "city": 1, "_id": 0},
)
```

Here:

- `1` means include this field
- `0` means exclude this field
- by default `_id` is always included, so you must explicitly set `"_id": 0` to hide it

---

## 23. ObjectId: Working With Document IDs

Every MongoDB document has a field called `_id`.

When MongoDB creates it automatically, `_id` is of type `ObjectId`, not a plain string.

An `ObjectId` looks like this in JSON:

```json
{ "_id": { "$oid": "6655a9b5b82f41d9dcd2f410" } }
```

When your API receives an id from the client, it comes as a plain string like `"6655a9b5b82f41d9dcd2f410"`.

You must convert that string to an `ObjectId` before using it in a MongoDB query.

```python
from bson import ObjectId
from bson.errors import InvalidId


async def get_user_by_id(user_id: str):
    try:
        object_id = ObjectId(user_id)
    except InvalidId:
        # the id string was not a valid ObjectId format
        return None

    user = await users_collection.find_one({"_id": object_id})
    return user
```

Why the `try` block:

- if someone sends a bad id like `"not-a-valid-id"`, `ObjectId()` will raise `InvalidId`
- the try block catches that and returns `None` instead of crashing

---

## 24. Indexes For Search And Filter

Without indexes, MongoDB reads every document in the collection to find matches. This is called a collection scan and it is slow on large collections.

An index is like a sorted list of one field's values. MongoDB can search the index directly instead of reading all documents.

Create indexes for fields you filter or sort on:

```python
async def create_user_indexes():
    # filter by city
    await users_collection.create_index("city")

    # filter by role
    await users_collection.create_index("role")

    # each user should have a unique email
    await users_collection.create_index("email", unique=True)

    # compound index: filter by city AND sort by first_name together
    await users_collection.create_index([("city", 1), ("first_name", 1)])
```

For text search using `$regex`:

- regex queries can use an index on the field if the regex is a prefix match (starts-with pattern)
- a regex like `"^neh"` (starts with "neh") can use an index on `first_name`
- a regex like `"neh"` (contains "neh") cannot fully use an index and does a scan

For full Google-style search on large collections, consider MongoDB Atlas Search (built on Lucene) which is more powerful than regex.

---

## 25. DBRef (Database Reference)

DBRef is a MongoDB convention for storing a reference to a document in another collection.

Example:

```json
{
  "appointment_id": "6655a9b5b82f41d9dcd2f500",
  "patient": {
    "$ref": "users",
    "$id": "6655a9b5b82f41d9dcd2f410",
    "$db": "training_db"
  }
}
```

In practice, most modern projects store just the `_id` value directly instead of a full DBRef object.

Common approach (simpler):

```json
{
  "appointment_id": "6655a9b5b82f41d9dcd2f500",
  "patient_id": "6655a9b5b82f41d9dcd2f410",
  "doctor_id": "6655a9b5b82f41d9dcd2f411"
}
```

Why direct ids are preferred:

- easier to query
- easier to understand
- Pydantic models handle them as plain strings
- avoids extra DBRef handling in Python

---

## 26. Relationships In MongoDB

MongoDB does not have joins like SQL.

Instead, relationships are handled in two ways.

### Embedded Documents

Store all related data inside one document.

Example: store address inside the user document.

```json
{
  "first_name": "Neha",
  "last_name": "Sharma",
  "address": {
    "city": "Pune",
    "state": "Maharashtra",
    "pincode": "411001"
  }
}
```

Use embedding when:

- the related data is small
- the related data is always read together with the parent
- the related data does not change often independently

### Referenced Documents

Store only the related document's id.

Example: appointment references user and doctor.

```json
{
  "patient_id": "6655a9b5b82f41d9dcd2f410",
  "doctor_id": "6655a9b5b82f41d9dcd2f411",
  "appointment_date": "2026-05-30",
  "status": "confirmed"
}
```

Use references when:

- the related document is large
- the related document is shared by many other documents
- the related document changes independently

To fetch the full patient and doctor data for an appointment, the application loads the appointment first, then queries the `users` collection separately using the stored ids.

---

## 27. Aggregation For Reports

Aggregation is used when you need grouped or calculated results.

Example: count how many users are in each city.

```python
async def count_users_by_city():
    pipeline = [
        {"$group": {"_id": "$city", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}},
    ]

    cursor = users_collection.aggregate(pipeline)
    return await cursor.to_list(length=100)
```

Result:

```json
[
  { "_id": "Pune", "total": 120 },
  { "_id": "Mumbai", "total": 95 },
  { "_id": "Nagpur", "total": 42 }
]
```

Example: count doctors by city, only active users.

```python
async def count_doctors_by_city():
    pipeline = [
        {"$match": {"role": "doctor", "is_active": True}},
        {"$group": {"_id": "$city", "total": {"$sum": 1}}},
        {"$sort": {"total": -1}},
    ]

    cursor = users_collection.aggregate(pipeline)
    return await cursor.to_list(length=100)
```

Common aggregation stages:

| Stage      | What It Does                                     |
| ---------- | ------------------------------------------------ |
| `$match`   | Filter documents. Like the filter in `find`.     |
| `$group`   | Group documents by a field and calculate values. |
| `$sort`    | Sort the output.                                 |
| `$project` | Choose or reshape fields in the output.          |
| `$lookup`  | Join with another collection.                    |
| `$unwind`  | Split one array field into many documents.       |
| `$limit`   | Stop after this many documents.                  |
| `$skip`    | Skip this many documents.                        |

---

## 28. Common Mistakes Freshers Make With Pagination And Queries

### 1. Forgetting `await` before cursor methods

Wrong:

```python
cursor = records_collection.find(...)
users = cursor.to_list(length=10)  # missing await
```

Correct:

```python
cursor = records_collection.find(...)
users = await cursor.to_list(length=10)
```

### 2. Treating `find` result as a list directly

Wrong:

```python
users = records_collection.find({"status": "active"})
for user in users:  # this does not work with Motor
    print(user)
```

Correct:

```python
cursor = records_collection.find({"status": "active"})
users = await cursor.to_list(length=100)
for user in users:
    print(user)
```

### 3. Querying `_id` using a plain string

Wrong:

```python
user = await users_collection.find_one({"_id": "6655a9b5b82f41d9dcd2f410"})
# returns None, no error, just silently finds nothing
```

Correct:

```python
from bson import ObjectId

user = await users_collection.find_one({"_id": ObjectId("6655a9b5b82f41d9dcd2f410")})
```

### 4. Using empty filter for `delete_many` or `update_many`

Wrong (deletes ALL documents):

```python
await users_collection.delete_many({})
```

Always add a filter unless you intentionally want all documents affected.

### 5. Not limiting `page_size` from the client

If the client sends `page_size=100000`, the server will try to return 100,000 documents. Always clamp `page_size` to a safe maximum:

```python
page_size = min(max(page_size, 1), 100)
```

### 6. Building regex from untrusted input without being careful

The `$regex` operator can be slow if the pattern is very complex. For a search box, keep the pattern simple: just the user's search text.

---

## 29. Quick Revision

- Pagination splits results into pages so the server does not return all data at once.
- `skip` jumps over previous pages.
- `limit` controls how many documents to return.
- Formula: `skip = (page - 1) * page_size`
- Filter by exact value: `{"city": "Pune"}`
- Filter by multiple values: `{"city": {"$in": ["Pune", "Mumbai"]}}`
- Partial name search: `{"first_name": {"$regex": "neh", "$options": "i"}}`
- Google-style search across fields: use `$or` with `$regex` on each field
- `$and` is the default: multiple filters in one dictionary all have to match
- `$or` means at least one condition must match
- Projection controls which fields are returned
- Convert string id to `ObjectId` before filtering by `_id`
- Indexes make filters and sorts faster
- `count_documents` gives exact total for pagination math
- Cursor-based pagination is better than skip+limit for very large collections
