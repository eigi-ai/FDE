# Chapter 4: Motor CRUD Functions

This chapter teaches you every important Motor function step by step.

By the end of this chapter you will know how to:

- insert one document or many documents
- search for documents
- update documents
- delete documents
- count documents
- work with indexes and aggregation
- understand what every function returns and why it matters

---

## 1. What Is Motor?

Motor is a Python library that lets your Python code talk to MongoDB.

It is the **asynchronous** version of PyMongo.

Asynchronous means your code does not freeze and wait while MongoDB is working.
Instead, Python can continue doing other things while waiting for MongoDB to respond.

This is very useful in web APIs where many users send requests at the same time.

In FastAPI, every route function is `async def`. So Motor fits perfectly because all Motor functions use `await`.

---

## 2. What Is CRUD?

CRUD stands for:

| Letter | Meaning | Motor function examples     |
| ------ | ------- | --------------------------- |
| C      | Create  | `insert_one`, `insert_many` |
| R      | Read    | `find_one`, `find`          |
| U      | Update  | `update_one`, `update_many` |
| D      | Delete  | `delete_one`, `delete_many` |

These four operations cover almost everything you do with a database.

---

## 3. Setting Up The Connection

Before calling any Motor function, you need a connection to MongoDB and a reference to the collection you want to work with.

```python
from motor.motor_asyncio import AsyncIOMotorClient


# Step 1: connect to MongoDB
client = AsyncIOMotorClient("mongodb://localhost:27017")

# Step 2: select the database
database = client["training_db"]

# Step 3: select the collection
records_collection = database["records"]
```

What each line does:

- `AsyncIOMotorClient("mongodb://localhost:27017")`: connects to MongoDB running on your machine
- `client["training_db"]`: selects the database named `training_db`
- `database["records"]`: selects the collection named `records`

If the database or collection does not exist yet, MongoDB creates them automatically when you first insert a document.

For MongoDB Atlas, the connection string looks like:

```python
client = AsyncIOMotorClient("mongodb+srv://username:password@cluster.mongodb.net/")
```

The `records` collection contains documents that look like this:

```json
{
  "_id": "6655a9b5b82f41d9dcd2f410",
  "title": "MongoDB first note",
  "category": "database",
  "status": "active",
  "priority": 1,
  "tags": ["mongodb", "training"],
  "created_by": "Neha"
}
```

All the examples in this chapter use `records_collection`.

---

## 4. `insert_one` — Save One Document

### What It Does

`insert_one` saves one new document into a collection.

Think of it like saving one new row into a spreadsheet.

### When To Use It

- when a user fills out a form and submits it
- when creating one new record, appointment, product, or log entry

### Code Example

```python
async def create_record():
    result = await records_collection.insert_one({
        "title": "MongoDB first note",
        "category": "database",
        "status": "active",
        "priority": 1,
        "tags": ["mongodb", "training"],
        "created_by": "Neha",
    })

    # result.inserted_id is the _id that MongoDB assigned to this document
    return str(result.inserted_id)
```

### What Is Happening Here

1. `insert_one({...})` sends the dictionary to MongoDB as a new document
2. MongoDB saves it and automatically creates an `_id` for it
3. `result.inserted_id` gives you that `_id` as an `ObjectId`
4. `str(result.inserted_id)` converts the `ObjectId` to a string so you can return it in an API response

### What `result` Contains

| Field                 | Type     | Meaning                             |
| --------------------- | -------- | ----------------------------------- |
| `result.inserted_id`  | ObjectId | the `_id` of the new document       |
| `result.acknowledged` | bool     | whether MongoDB confirmed the write |

### Beginner Note

- MongoDB will reject the insert if the `_id` value already exists in the collection
- you almost never need to set `_id` yourself — let MongoDB create it

---

## 5. `insert_many` — Save Multiple Documents At Once

### What It Does

`insert_many` saves a list of documents in one operation.

It is much faster than calling `insert_one` in a loop.

### When To Use It

- when loading sample or seed data
- when importing a batch of records
- when creating multiple items from one API request

### Code Example

```python
async def create_many_records():
    result = await records_collection.insert_many([
        {
            "title": "Learn collections",
            "category": "basics",
            "status": "active",
            "priority": 1,
        },
        {
            "title": "Learn indexes",
            "category": "performance",
            "status": "draft",
            "priority": 2,
        },
        {
            "title": "Learn aggregation",
            "category": "advanced",
            "status": "draft",
            "priority": 3,
        },
    ])

    # result.inserted_ids is a list of ObjectId values
    return [str(inserted_id) for inserted_id in result.inserted_ids]
```

### What Is Happening Here

1. you pass a list of dictionaries to `insert_many`
2. MongoDB inserts all of them
3. `result.inserted_ids` is a list with one `ObjectId` per inserted document
4. the list comprehension converts each `ObjectId` to a string

### What `result` Contains

| Field                 | Type             | Meaning                             |
| --------------------- | ---------------- | ----------------------------------- |
| `result.inserted_ids` | list of ObjectId | one id per inserted document        |
| `result.acknowledged` | bool             | whether MongoDB confirmed the write |

### Beginner Note

- by default MongoDB stops inserting when one document fails (ordered mode)
- set `ordered=False` to continue inserting the rest even if one fails

---

## 6. `find_one` — Get One Matching Document

### What It Does

`find_one` searches the collection and returns the first document that matches your filter.

If no document matches, it returns `None`.

### When To Use It

- when fetching a user by email
- when fetching a record by its id
- when checking whether a document exists

### Code Example

```python
async def get_record_by_title(title: str):
    # pass a filter dictionary — MongoDB finds the first document where title matches
    record = await records_collection.find_one({"title": title})

    # if nothing matched, record is None
    if record is None:
        return None

    return record
```

Find by `_id`:

```python
from bson import ObjectId
from bson.errors import InvalidId


async def get_record_by_id(record_id: str):
    try:
        object_id = ObjectId(record_id)
    except InvalidId:
        # the provided string is not a valid ObjectId format
        return None

    record = await records_collection.find_one({"_id": object_id})
    return record
```

### What Is Happening Here

- `{"title": title}` is the filter — MongoDB reads documents and checks if `title` matches
- when the first match is found, MongoDB returns it immediately
- MongoDB does not continue reading the rest of the collection after a match

### What It Returns

- one document as a Python dictionary
- `None` if no document matches the filter

### Beginner Note

- always check for `None` before using the returned document
- if you try to access a key on `None`, Python will crash with `AttributeError`

---

## 7. `find` — Get Multiple Matching Documents

### What It Does

`find` searches the collection and returns all documents that match your filter.

Unlike `find_one`, it returns a **cursor**, not a list.

A cursor is like a pointer that knows how to read through matching documents one by one.

You then convert the cursor to a list using `to_list`.

### When To Use It

- when listing all active records
- when returning search results
- when building a table or list view in an API

### Code Example

```python
async def get_active_records():
    # find() returns a cursor, not a list
    cursor = records_collection.find({"status": "active"})

    # to_list reads from the cursor and collects results into a Python list
    # length=100 means read at most 100 documents
    records = await cursor.to_list(length=100)

    return records
```

Get all records (no filter):

```python
async def get_all_records():
    cursor = records_collection.find({})  # empty filter means no restriction
    records = await cursor.to_list(length=100)
    return records
```

Using `async for` to process one document at a time:

```python
async def print_all_active_records():
    cursor = records_collection.find({"status": "active"})

    async for record in cursor:
        # process one record at a time instead of loading all into memory
        print(record["title"])
```

### What Is Happening Here

- `find({"status": "active"})` creates a cursor that will read matching documents
- `await cursor.to_list(length=100)` actually runs the query and loads up to 100 documents
- `length` is the maximum number of documents to load at once

### Beginner Note

- `find` itself is NOT awaited because it only creates the cursor, it does not run the query yet
- the query runs when you call `to_list` or iterate with `async for`
- common mistake: `records = await records_collection.find(...)` — this is wrong and will cause an error

---

## 8. Projection — Choosing Which Fields To Return

### What Is Projection

Projection means telling MongoDB which fields to include or exclude in the result.

Without projection, MongoDB returns every field in every document.

With projection, you can say "only give me title and status, skip everything else".

### Why Use It

- return smaller responses (faster API)
- hide sensitive fields like passwords or internal flags
- return only what the frontend actually needs

### Code Example

Return only `title` and `status`, hide everything else including `_id`:

```python
async def get_record_titles():
    cursor = records_collection.find(
        {"status": "active"},          # filter: only active records
        {"title": 1, "status": 1, "_id": 0},  # projection: include title and status, exclude _id
    )

    return await cursor.to_list(length=100)
```

### Rules For Projection

- `1` means include this field
- `0` means exclude this field
- `_id` is included by default even if you do not list it — you must explicitly set `"_id": 0` to hide it
- you cannot mix `1` and `0` in the same projection (except for `_id`)

---

## 9. `update_one` — Change One Document

### What It Does

`update_one` finds the first document that matches your filter and updates it.

### When To Use It

- when changing one user's profile
- when updating one record's status
- when modifying one document by its id

### Code Example

```python
async def mark_record_completed(title: str):
    result = await records_collection.update_one(
        {"title": title},             # filter: find this document
        {"$set": {"status": "completed"}},  # update: set the status field to "completed"
    )

    return {
        "matched_count": result.matched_count,
        "modified_count": result.modified_count,
    }
```

### What Is Happening Here

- the first argument is the filter — which document to find
- the second argument is the update — what to change
- `$set` is an update operator that sets a specific field without touching the other fields
- `result.matched_count` tells you if MongoDB found a matching document
- `result.modified_count` tells you if MongoDB actually changed something

### Understanding `matched_count` vs `modified_count`

| Situation                                     | matched_count | modified_count |
| --------------------------------------------- | ------------- | -------------- |
| Document found and changed                    | 1             | 1              |
| Document found but value was already the same | 1             | 0              |
| No document found                             | 0             | 0              |

### Beginner Note

- always use update operators like `$set` inside the update argument
- do not pass the full document directly — that would be `replace_one`, which removes all other fields

---

## 10. `update_many` — Change All Matching Documents

### What It Does

`update_many` finds all documents that match your filter and updates all of them.

### When To Use It

- when archiving all draft records at once
- when marking all records in a category as reviewed
- when applying a batch update

### Code Example

```python
async def archive_all_draft_records():
    result = await records_collection.update_many(
        {"status": "draft"},              # filter: all draft records
        {"$set": {"status": "archived"}}, # update: change status to archived
    )

    return {
        "matched": result.matched_count,
        "modified": result.modified_count,
    }
```

### Beginner Note

- be very careful with the filter
- `update_many({}, {"$set": {...}})` means update EVERY document in the collection because `{}` matches everything

---

## 11. Common Update Operators

These operators go inside the update argument and control exactly what MongoDB changes.

| Operator    | What It Does                                            | Example                              |
| ----------- | ------------------------------------------------------- | ------------------------------------ |
| `$set`      | Set one or more fields to a new value                   | `{"$set": {"status": "active"}}`     |
| `$unset`    | Remove a field from the document completely             | `{"$unset": {"temp_flag": ""}}`      |
| `$inc`      | Add a number to a numeric field                         | `{"$inc": {"priority": 1}}`          |
| `$push`     | Add one value to the end of an array field              | `{"$push": {"tags": "important"}}`   |
| `$pull`     | Remove a specific value from an array field             | `{"$pull": {"tags": "old"}}`         |
| `$addToSet` | Add a value to an array only if it is not already there | `{"$addToSet": {"tags": "mongodb"}}` |

### Examples

Increase priority by 1:

```python
await records_collection.update_one(
    {"title": "Learn collections"},
    {"$inc": {"priority": 1}},
)
```

Add a tag to the tags array:

```python
await records_collection.update_one(
    {"title": "Learn collections"},
    {"$push": {"tags": "important"}},
)
```

Remove a tag from the tags array:

```python
await records_collection.update_one(
    {"title": "Learn collections"},
    {"$pull": {"tags": "old"}},
)
```

Remove a field entirely:

```python
await records_collection.update_one(
    {"title": "Learn collections"},
    {"$unset": {"temp_flag": ""}},  # the value "" is required by MongoDB but ignored
)
```

---

## 12. `replace_one` — Overwrite One Complete Document

### What It Does

`replace_one` replaces the entire document (except `_id`) with a new document you provide.

It is different from `update_one`:

- `update_one` with `$set` only changes the fields you specify, leaving the rest untouched
- `replace_one` removes ALL existing fields and replaces them with the new document

### When To Use It

- when you want to completely overwrite a document with a fresh version
- rarely used in practice — `update_one` with `$set` is usually better

### Code Example

```python
async def replace_record(title: str):
    result = await records_collection.replace_one(
        {"title": title},   # filter: find this document
        {                   # replacement: the full new document
            "title": title,
            "category": "database",
            "status": "active",
            "priority": 1,
        },
    )

    return result.modified_count
```

### Beginner Note

- if the original document had fields like `tags` or `created_by`, they are gone after `replace_one`
- only fields in the replacement document survive

---

## 13. `delete_one` — Remove One Document

### What It Does

`delete_one` finds the first document that matches your filter and deletes it.

### When To Use It

- when deleting one record by its id
- when removing one specific document

### Code Example

```python
async def delete_record_by_title(title: str):
    result = await records_collection.delete_one({"title": title})

    # deleted_count tells you how many documents were deleted (0 or 1)
    return result.deleted_count
```

Delete by id (most common in APIs):

```python
from bson import ObjectId
from bson.errors import InvalidId


async def delete_record_by_id(record_id: str):
    try:
        object_id = ObjectId(record_id)
    except InvalidId:
        return 0

    result = await records_collection.delete_one({"_id": object_id})
    return result.deleted_count
```

### What `result` Contains

| Field                  | Type | Meaning                              |
| ---------------------- | ---- | ------------------------------------ |
| `result.deleted_count` | int  | number of documents deleted (0 or 1) |
| `result.acknowledged`  | bool | whether MongoDB confirmed the delete |

---

## 14. `delete_many` — Remove All Matching Documents

### What It Does

`delete_many` finds all documents that match your filter and deletes all of them.

### When To Use It

- when clearing all draft records
- when deleting all expired log entries
- when cleaning up test data

### Code Example

```python
async def delete_all_draft_records():
    result = await records_collection.delete_many({"status": "draft"})
    return result.deleted_count
```

### Beginner Note

- `delete_many({})` with an empty filter deletes EVERY document in the collection
- always double-check your filter before calling `delete_many`

---

## 15. `count_documents` — Count Matching Documents

### What It Does

`count_documents` counts how many documents match your filter.

It always returns an accurate count based on your filter.

### When To Use It

- when calculating total pages for pagination
- when showing "35 active records found"
- when checking how many records a user has

### Code Example

```python
async def count_active_records():
    count = await records_collection.count_documents({"status": "active"})
    return count
```

Count all documents (no filter):

```python
async def count_all_records():
    count = await records_collection.count_documents({})
    return count
```

---

## 16. `estimated_document_count` — Quick Total Count

### What It Does

`estimated_document_count` gives a fast but approximate count of all documents in the collection.

It does not accept a filter.

### When To Use It

- when you just want to know roughly how many documents are in a collection
- when a rough total is acceptable and speed matters more than accuracy

### Code Example

```python
async def get_approximate_total():
    count = await records_collection.estimated_document_count()
    return count
```

### `count_documents` vs `estimated_document_count`

| Comparison     | `count_documents` | `estimated_document_count` |
| -------------- | ----------------- | -------------------------- |
| Accepts filter | Yes               | No                         |
| Accuracy       | Exact             | Estimated                  |
| Speed          | Slower            | Faster                     |
| Best for       | Pagination totals | Quick stats                |

---

## 17. `distinct` — Get Unique Values For One Field

### What It Does

`distinct` returns a list of all unique values that exist in one field across the collection.

### When To Use It

- when building a status filter dropdown — show only statuses that actually exist
- when listing all categories
- when finding all unique cities or roles

### Code Example

```python
async def get_all_statuses():
    statuses = await records_collection.distinct("status")
    # returns something like: ["active", "draft", "archived", "completed"]
    return statuses
```

`distinct` with a filter — only among active records:

```python
async def get_categories_in_active_records():
    categories = await records_collection.distinct(
        "category",           # field to get unique values from
        {"status": "active"}, # filter: only look within active records
    )
    return categories
```

---

## 18. `find_one_and_update` — Update And Get The Document Back

### What It Does

`find_one_and_update` does two things atomically (at the same time):

1. finds one matching document
2. updates it
3. returns the document

The key advantage over `update_one` is that you get the document back in the same operation, without a second `find_one` call.

### When To Use It

- when the API response needs to return the updated document
- when you want to guarantee no one else changes the document between your update and your read

### Code Example

```python
from pymongo import ReturnDocument


async def activate_record(title: str):
    updated_record = await records_collection.find_one_and_update(
        {"title": title},                   # filter: find this document
        {"$set": {"status": "active"}},     # update: set status to active
        return_document=ReturnDocument.AFTER,  # return the document AFTER the update
    )

    # if no document matched, updated_record is None
    return updated_record
```

### `ReturnDocument.BEFORE` vs `ReturnDocument.AFTER`

| Option                  | What you get                             |
| ----------------------- | ---------------------------------------- |
| `ReturnDocument.BEFORE` | the document as it was before the update |
| `ReturnDocument.AFTER`  | the document as it is after the update   |

### Beginner Note

- use `ReturnDocument.AFTER` when you want to return the updated values to the API caller
- if no document matches, the function returns `None`

---

## 19. `find_one_and_delete` — Delete And Get The Document Back

### What It Does

`find_one_and_delete` finds one document, deletes it, and returns the deleted document.

This is different from `delete_one`, which only tells you how many documents were deleted.

### When To Use It

- when you need to show or log what was deleted
- when processing a queue (pop the first item and return it)

### Code Example

```python
async def pop_oldest_draft_record():
    deleted_record = await records_collection.find_one_and_delete(
        {"status": "draft"},
    )

    # deleted_record is the document that was just deleted
    # it is None if no document matched
    return deleted_record
```

---

## 20. `find_one_and_replace` — Replace And Get The Document Back

### What It Does

`find_one_and_replace` replaces one full document and returns either the old or new version.

### When To Use It

- when you need full document replacement and also need the result returned

### Code Example

```python
from pymongo import ReturnDocument


async def replace_and_return_record(title: str):
    record = await records_collection.find_one_and_replace(
        {"title": title},
        {
            "title": title,
            "category": "database",
            "status": "active",
            "priority": 1,
        },
        return_document=ReturnDocument.AFTER,
    )

    return record
```

### Beginner Note

- like `replace_one`, this removes all fields not in the replacement document
- for partial updates, `find_one_and_update` with `$set` is safer

---

## 21. `create_index` — Make Searches Faster

### What Is An Index?

Without an index, MongoDB reads every document in the collection to find matches. This is called a full collection scan. On 100 documents it is fine. On 1,000,000 documents it is very slow.

An index is like the index at the back of a book. Instead of reading every page to find a word, you look it up in the index and jump directly to the right page.

### When To Create Indexes

- on fields you use frequently in filters: `{"status": "active"}`
- on fields you sort by: `.sort("created_at", -1)`
- on fields that must be unique: `email`

### Code Examples

Index on status (for filters):

```python
async def create_status_index():
    index_name = await records_collection.create_index("status")
    return index_name
```

Index on created_at (for sorting newest first):

```python
async def create_created_at_index():
    index_name = await records_collection.create_index("created_at")
    return index_name
```

Unique index on title (no two records can have the same title):

```python
async def create_unique_title_index():
    index_name = await records_collection.create_index("title", unique=True)
    return index_name
```

Compound index (for filtering by status AND sorting by created_at together):

```python
async def create_compound_index():
    index_name = await records_collection.create_index([
        ("status", 1),       # 1 = ascending
        ("created_at", -1),  # -1 = descending
    ])
    return index_name
```

### Beginner Note

- `1` means ascending order in the index
- `-1` means descending order in the index
- indexes improve reads but add a small cost to writes
- do not create indexes on fields you rarely filter or sort on

---

## 22. `create_indexes` — Create Multiple Indexes At Once

Use `create_indexes` to set up all indexes in one call, usually during application startup.

```python
from pymongo import IndexModel


async def setup_records_indexes():
    index_names = await records_collection.create_indexes([
        IndexModel([("status", 1)]),
        IndexModel([("created_at", -1)]),
        IndexModel([("title", 1)], unique=True),
        IndexModel([("status", 1), ("created_at", -1)]),
    ])

    return index_names
```

---

## 23. `list_indexes` — See All Existing Indexes

```python
async def list_all_indexes():
    indexes = []

    async for index in records_collection.list_indexes():
        indexes.append(index)

    return indexes
```

Every collection always has at least one index: the `_id` index that MongoDB creates automatically.

---

## 24. `drop_index` And `drop_indexes` — Remove Indexes

Remove one specific index by name:

```python
async def remove_status_index():
    await records_collection.drop_index("status_1")
```

The index name is the field name plus `_1` or `_-1` depending on sort direction. Use `list_indexes` to find the exact name.

Remove all indexes except the `_id` index:

```python
async def remove_all_indexes():
    await records_collection.drop_indexes()
```

### Beginner Note

- `drop_indexes()` removes all indexes except the required `_id` index
- this will make all your queries slower until you recreate the indexes

---

## 25. `aggregate` — Data Processing Pipeline

### What Is Aggregation?

Aggregation is for when you need more than just "get documents". You need to group, count, calculate, reshape, or join data.

Think of it like SQL's `GROUP BY` or an Excel pivot table.

### How It Works

Aggregation works as a pipeline. Each stage takes the output of the previous stage and processes it further.

```text
Collection → $match → $group → $sort → Result
```

### Example: Count Records By Status

```python
async def count_records_by_status():
    pipeline = [
        # Stage 1: group by status, count each group
        {"$group": {"_id": "$status", "total": {"$sum": 1}}},

        # Stage 2: sort by total, highest first
        {"$sort": {"total": -1}},
    ]

    cursor = records_collection.aggregate(pipeline)
    return await cursor.to_list(length=100)
```

Result:

```json
[
  { "_id": "active", "total": 45 },
  { "_id": "draft", "total": 20 },
  { "_id": "archived", "total": 8 }
]
```

### Example: Filter First, Then Count

```python
async def count_active_by_category():
    pipeline = [
        # Stage 1: filter only active records
        {"$match": {"status": "active"}},

        # Stage 2: group the filtered results by category
        {"$group": {"_id": "$category", "total": {"$sum": 1}}},

        # Stage 3: sort by total
        {"$sort": {"total": -1}},
    ]

    cursor = records_collection.aggregate(pipeline)
    return await cursor.to_list(length=100)
```

### Common Aggregation Stages

| Stage      | What It Does                                              |
| ---------- | --------------------------------------------------------- |
| `$match`   | Filter documents — like the filter in `find`              |
| `$group`   | Group documents by a field and compute totals or averages |
| `$sort`    | Sort the results                                          |
| `$project` | Choose or reshape which fields appear in the output       |
| `$lookup`  | Join data from another collection                         |
| `$unwind`  | Split one array element into separate documents           |
| `$limit`   | Stop after this many documents                            |
| `$skip`    | Skip this many documents                                  |

### Beginner Note

- put `$match` as the first stage whenever possible — it filters early and makes later stages faster
- aggregation is powerful but start simple: learn `$match`, `$group`, and `$sort` first

---

## 26. `bulk_write` — Run Many Write Operations In One Call

### What Is It?

`bulk_write` lets you send many insert, update, and delete operations to MongoDB in a single network call instead of many separate calls.

### When To Use It

- when importing large amounts of data
- when updating many different documents with different changes
- when you want to reduce the number of database round trips

### Code Example

```python
from pymongo import DeleteOne, InsertOne, UpdateOne


async def run_bulk_operations():
    result = await records_collection.bulk_write([
        InsertOne({"title": "Bulk record one", "status": "active"}),
        InsertOne({"title": "Bulk record two", "status": "draft"}),
        UpdateOne(
            {"title": "MongoDB first note"},  # filter
            {"$set": {"status": "completed"}},  # update
        ),
        DeleteOne({"status": "deleted"}),
    ])

    return {
        "inserted_count": result.inserted_count,
        "modified_count": result.modified_count,
        "deleted_count": result.deleted_count,
    }
```

### Beginner Note

- while learning, use normal single functions: `insert_one`, `update_one`, and `delete_one`
- move to `bulk_write` only when you have batch operations and need performance

---

## 27. `watch` — Listen For Changes In Real Time

### What Is It?

`watch` opens a change stream. Your code listens for inserts, updates, or deletes as they happen in MongoDB, in real time.

### When To Use It

- when building real-time notifications
- when syncing changes to a cache or another service
- when reacting to data changes automatically

### Code Example

```python
async def watch_records_collection():
    async with records_collection.watch() as stream:
        async for change in stream:
            # change is a dictionary describing what happened
            print(change["operationType"])  # "insert", "update", or "delete"
            print(change)
```

### Beginner Note

- change streams require MongoDB to run as a replica set or sharded cluster
- a plain local MongoDB instance without replica set configuration does not support `watch`
- this is an advanced feature — focus on CRUD first

---

## 28. All Motor Collection Functions At A Glance

| Function                   | What It Does                                      |
| -------------------------- | ------------------------------------------------- |
| `insert_one`               | Insert one document                               |
| `insert_many`              | Insert many documents                             |
| `find_one`                 | Find and return one document (or None)            |
| `find`                     | Find and return a cursor for multiple documents   |
| `update_one`               | Update the first matching document                |
| `update_many`              | Update all matching documents                     |
| `replace_one`              | Replace one complete document                     |
| `delete_one`               | Delete the first matching document                |
| `delete_many`              | Delete all matching documents                     |
| `count_documents`          | Count matching documents (accurate)               |
| `estimated_document_count` | Count all documents (estimated, fast)             |
| `distinct`                 | Get unique values for one field                   |
| `aggregate`                | Run a data processing pipeline                    |
| `create_index`             | Create one index                                  |
| `create_indexes`           | Create many indexes at once                       |
| `list_indexes`             | List all indexes on the collection                |
| `drop_index`               | Remove one index                                  |
| `drop_indexes`             | Remove all indexes except `_id`                   |
| `find_one_and_update`      | Find, update, and return the document atomically  |
| `find_one_and_delete`      | Find, delete, and return the document atomically  |
| `find_one_and_replace`     | Find, replace, and return the document atomically |
| `bulk_write`               | Run many write operations in one call             |
| `watch`                    | Listen to real-time change streams                |

---

## 29. Common Mistakes Freshers Make

### 1. Awaiting `find` directly

Wrong:

```python
records = await records_collection.find({"status": "active"})  # TypeError
```

`find` creates a cursor and does not need `await`. The `await` goes on `to_list`:

```python
cursor = records_collection.find({"status": "active"})
records = await cursor.to_list(length=100)
```

### 2. Treating `find` result as a list

Wrong:

```python
cursor = records_collection.find({})
for record in cursor:  # does not work with Motor's async cursor
    print(record)
```

Correct:

```python
cursor = records_collection.find({})
records = await cursor.to_list(length=100)
for record in records:
    print(record)
```

### 3. Querying `_id` using a plain string

Wrong:

```python
# this returns None silently — MongoDB never raises an error
record = await records_collection.find_one({"_id": "6655a9b5b82f41d9dcd2f410"})
```

Correct:

```python
from bson import ObjectId

record = await records_collection.find_one({"_id": ObjectId("6655a9b5b82f41d9dcd2f410")})
```

### 4. Using `replace_one` when you only wanted to change one field

Wrong (removes all other fields):

```python
await records_collection.replace_one(
    {"title": "Learn collections"},
    {"status": "archived"},  # this removes title, category, tags, and everything else
)
```

Correct (only changes status):

```python
await records_collection.update_one(
    {"title": "Learn collections"},
    {"$set": {"status": "archived"}},
)
```

### 5. Forgetting `await` on Motor functions

Wrong:

```python
result = records_collection.insert_one({"title": "test"})  # returns a coroutine, not a result
```

Correct:

```python
result = await records_collection.insert_one({"title": "test"})
```

### 6. Empty filter in `delete_many` or `update_many`

Wrong (deletes or updates everything in the collection):

```python
await records_collection.delete_many({})
await records_collection.update_many({}, {"$set": {"status": "deleted"}})
```

Always double-check your filter before running `delete_many` or `update_many`.

### 7. Not checking for `None` after `find_one`

Wrong:

```python
record = await records_collection.find_one({"title": "missing"})
print(record["title"])  # AttributeError: 'NoneType' object has no attribute '__getitem__'
```

Correct:

```python
record = await records_collection.find_one({"title": "missing"})
if record is None:
    return None
print(record["title"])
```

---

## 30. Quick Revision

- Motor is the async Python driver for MongoDB. Use `await` with all its functions.
- `insert_one` saves one document. `insert_many` saves a list of documents.
- `find_one` returns one document or `None`. Always check for `None`.
- `find` returns a cursor. Convert it to a list using `await cursor.to_list(length=N)`.
- `update_one` changes one document. `update_many` changes all matching documents.
- Always use update operators like `$set` inside the update argument of `update_one` and `update_many`.
- `replace_one` overwrites the entire document. Be careful — fields not in the replacement are deleted.
- `delete_one` deletes one document. `delete_many` deletes all matching documents.
- Never pass an empty filter `{}` to `delete_many` or `update_many` unless you intend to affect all documents.
- `count_documents` gives an accurate count with a filter. `estimated_document_count` gives a fast rough count.
- `distinct` returns a list of unique values for one field.
- `find_one_and_update`, `find_one_and_delete`, and `find_one_and_replace` combine two operations atomically and return the document.
- `aggregate` runs a pipeline for grouping, reporting, and data processing.
- `create_index` makes queries on that field faster.
- `bulk_write` sends many operations in one network call.
- `watch` listens for real-time changes — advanced feature, requires replica set.
