# MongoDB Tutorial For Freshers

This module teaches MongoDB from the beginning for learners who are new to databases, backend development, and async Python database access.

MongoDB is a NoSQL document database. It stores data in collections as JSON-like documents instead of fixed rows and columns.

## How To Read This Module

Each topic is split into a separate chapter file.

Recommended way to learn:

1. Read the chapters in order.
2. Try the shell commands in MongoDB Atlas or `mongosh`.
3. Then practice the Python examples using Motor.
4. Revisit pagination, indexes, and aggregation after learning CRUD basics.

## Learning Order

1. `01_mongodb_basics.md`
   Learn what MongoDB is, how databases, collections, records, documents, fields, BSON, and `_id` work.

2. `02_python_libraries.md`
   Learn the Python libraries used with MongoDB, including PyMongo, Motor, ODMantic, and why async FastAPI projects usually choose Motor.

3. `03_mongodb_atlas_and_shell.md`
   Learn what MongoDB Atlas is, how to connect using MongoDB Shell, and how to run basic shell commands.

4. `04_motor_crud_functions.md`
   Learn the common Motor collection functions such as `insert_one`, `find_one`, `find`, `update_one`, `update_many`, `delete_one`, `delete_many`, `aggregate`, and index helpers with detailed fresher-friendly explanations.

5. `05_pagination_queries_and_patterns.md`
   Learn pagination, sorting, filtering, projections, indexes, aggregation, ObjectId handling, DBRef, relationships, and common backend patterns.

## Important Terms

- Database: container for collections.
- Collection: group of documents. A collection is similar to a table in SQL.
- Document: one record inside a collection.
- Record: beginner-friendly word for one stored item. In MongoDB, a record is a document.
- Field: one key-value pair inside a document.
- BSON: Binary JSON, the format MongoDB uses internally.
- `_id`: unique id field that every MongoDB document has.
- PyMongo: official synchronous Python driver for MongoDB.
- Motor: official asynchronous Python driver for MongoDB.
- ODMantic: asynchronous ODM for MongoDB built on Motor and Pydantic.
- Atlas: MongoDB's hosted cloud database platform.
- `mongosh`: MongoDB Shell used to run database commands directly.

## What This Module Covers

- basics of MongoDB
- records collection examples
- Python libraries used for MongoDB
- PyMongo vs Motor
- ODMantic and ODM basics
- async and await with MongoDB
- MongoDB Atlas
- MongoDB Shell usage
- common shell commands
- Motor CRUD functions
- update, delete, count, distinct, and aggregate functions
- pagination patterns
- indexes
- ObjectId
- DBRef
- embedded vs referenced relationships
- FastAPI-friendly MongoDB patterns

## Beginner Notes

- MongoDB stores documents inside collections.
- A collection named `records` is commonly useful for practice because it lets learners insert simple sample documents.
- Use PyMongo when the application is synchronous.
- Use Motor when the application is asynchronous, especially with FastAPI.
- Do not commit MongoDB Atlas passwords or connection strings to Git.
- Use environment variables for real database credentials.
