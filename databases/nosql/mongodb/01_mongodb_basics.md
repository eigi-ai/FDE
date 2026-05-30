# Chapter 1: Basics Of MongoDB

This chapter explains MongoDB from the beginning.

MongoDB is a NoSQL document database. It stores data as documents inside collections.

## 1. What Is A Database?

A database is a system used to store, organize, search, update, and delete data.

Examples of data stored in applications:

- users
- orders
- products
- appointments
- payments
- patient records
- chat messages
- logs

Without a database, data usually disappears when the program stops running.

## 2. SQL Vs NoSQL

SQL databases store data in tables.

Examples:

- PostgreSQL
- MySQL
- SQLite

NoSQL databases store data in non-table formats such as documents, key-value pairs, graphs, or wide-column records.

MongoDB is a document database.

| Concept        | SQL Database     | MongoDB              |
| -------------- | ---------------- | -------------------- |
| Main structure | Table            | Collection           |
| Single record  | Row              | Document             |
| Beginner word  | Record           | Record or document   |
| Data format    | Columns and rows | BSON document        |
| Schema         | Usually strict   | Flexible             |
| Query language | SQL              | MongoDB query syntax |

## 3. What Is MongoDB?

MongoDB stores data as JSON-like documents.

Example document:

```json
{
  "name": "Aarav",
  "email": "aarav@example.com",
  "age": 24,
  "is_active": true
}
```

Internally, MongoDB stores documents as BSON.

BSON means Binary JSON. It is similar to JSON but supports extra data types like `ObjectId`, `Date`, decimal values, and binary data.

## 4. Main MongoDB Terms

### Database

A database is a container for collections.

Example database names:

```text
training_db
medi_hub
shop_app
```

### Collection

A collection is a group of documents.

Example collections:

```text
users
appointments
patient_records
hospitals
records
```

### Document

A document is one stored item inside a collection.

Example user document:

```json
{
  "_id": "6655a9b5b82f41d9dcd2f410",
  "name": "Neha",
  "email": "neha@example.com",
  "role": "doctor"
}
```

### Record

Record is a common beginner-friendly word for one piece of stored data.

In MongoDB:

```text
record = document
```

So if someone says "insert one record into MongoDB", they usually mean "insert one document into a collection".

### Field

A field is one key-value pair inside a document.

Example field:

```json
"email": "neha@example.com"
```

### `_id`

Every MongoDB document has a unique `_id` field.

If we do not provide `_id`, MongoDB creates one automatically using `ObjectId`.

Example:

```json
{
  "_id": { "$oid": "6655a9b5b82f41d9dcd2f410" },
  "title": "First record"
}
```

## 5. Records Collection For Practice

For freshers, a collection named `records` is useful because it keeps examples simple.

Example `records` collection document:

```json
{
  "title": "MongoDB first note",
  "category": "database",
  "status": "active",
  "priority": 1,
  "tags": ["mongodb", "training"],
  "created_by": "student@example.com"
}
```

This document has:

- string fields: `title`, `category`, `status`, `created_by`
- number field: `priority`
- array field: `tags`

## 6. Document Data Types

Common MongoDB document value types:

| Type     | Example                                |
| -------- | -------------------------------------- |
| String   | `"Neha"`                               |
| Number   | `24`                                   |
| Boolean  | `true`                                 |
| Array    | `["doctor", "admin"]`                  |
| Object   | `{ "city": "Pune" }`                   |
| Date     | `ISODate("2026-05-30T10:00:00Z")`      |
| ObjectId | `ObjectId("6655a9b5b82f41d9dcd2f410")` |
| Null     | `null`                                 |

## 7. Flexible Schema

MongoDB has a flexible schema.

That means documents in the same collection do not always need the exact same fields.

Example:

```json
{
  "title": "Basic record",
  "status": "active"
}
```

```json
{
  "title": "Detailed record",
  "status": "active",
  "priority": 2,
  "tags": ["mongodb", "backend"]
}
```

This flexibility is useful, but it does not mean the application should accept bad data.

In backend projects, validate request data using tools such as Pydantic.

## 8. Embedded Documents

An embedded document means one object is stored inside another document.

Example:

```json
{
  "name": "Neha",
  "address": {
    "city": "Pune",
    "state": "Maharashtra"
  }
}
```

Use embedded documents when related data is usually read together.

## 9. Arrays

MongoDB documents can contain arrays.

Example:

```json
{
  "title": "MongoDB lesson",
  "tags": ["database", "nosql", "backend"]
}
```

Arrays are useful for tags, roles, permissions, comments, or small repeated values.

## 10. When Should We Use MongoDB?

MongoDB is useful when:

- the data structure may change over time
- the application stores JSON-like data
- records can have nested objects or arrays
- the project needs fast development
- the backend works heavily with APIs or event data
- documents are usually read and written as a whole

Common use cases:

- user profiles
- product catalogs
- logs
- chat applications
- content management systems
- IoT data
- appointment or booking systems

MongoDB may not be the best choice when the project needs many strict joins and complex relational constraints. In that case, PostgreSQL or another SQL database may be better.

## 11. Basic Mental Model

Think of MongoDB like this:

```text
MongoDB server
  -> database
    -> collection
      -> document or record
        -> field
```

Example:

```text
MongoDB server
  -> training_db
    -> records
      -> { "title": "First record", "status": "active" }
```

## 12. Quick Revision

- MongoDB is a NoSQL document database.
- A database contains collections.
- A collection contains documents.
- A document is also commonly called a record.
- A document contains fields.
- MongoDB stores data as BSON.
- Every document has an `_id`.
- The `records` collection is useful for beginner practice.
- MongoDB supports nested objects and arrays.
