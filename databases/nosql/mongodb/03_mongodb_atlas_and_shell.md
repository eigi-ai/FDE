# Chapter 3: MongoDB Atlas And Shell

This chapter explains MongoDB Atlas and basic MongoDB Shell commands.

## 1. What Is MongoDB Atlas?

MongoDB Atlas is MongoDB's hosted cloud database platform.

Instead of installing and managing MongoDB yourself, Atlas lets you create a database cluster in the cloud.

Atlas is useful because:

- no local database installation is required
- a free tier is available
- it gives a connection string
- it supports production-style access control
- it includes monitoring and backups depending on the plan
- it is commonly used in real projects

## 2. Basic Atlas Setup Flow

The usual beginner flow is:

1. Create a MongoDB Atlas account.
2. Create a free cluster.
3. Create a database user.
4. Add your current IP address to Network Access.
5. Copy the connection string.
6. Use the connection string in `mongosh` or Python.

## 3. Atlas Connection String

Atlas usually gives a connection string like this:

```text
mongodb+srv://username:password@cluster-name.mongodb.net/
```

Example with database name:

```text
mongodb+srv://username:password@cluster-name.mongodb.net/training_db
```

Important:

- replace `username` with your Atlas database username
- replace `password` with your Atlas database password
- do not commit this connection string to Git
- special characters in the password may need URL encoding

## 4. What Is MongoDB Shell?

MongoDB Shell is called `mongosh`.

It lets us connect to MongoDB and run database commands directly.

It is useful for:

- testing queries
- checking inserted data
- creating collections
- creating indexes
- debugging database issues
- learning MongoDB syntax

## 5. Connect Atlas Using `mongosh`

After installing MongoDB Shell, connect using the Atlas connection string:

```bash
mongosh "mongodb+srv://username:password@cluster-name.mongodb.net/"
```

Connect to a specific database:

```bash
mongosh "mongodb+srv://username:password@cluster-name.mongodb.net/training_db"
```

After connecting, the shell prompt lets you run MongoDB commands.

## 6. Show Databases

```javascript
show dbs
```

This lists databases that contain data.

If a database has no collection or no document, it may not appear yet.

## 7. Select Or Create A Database

```javascript
use training_db
```

MongoDB creates the database only after data is inserted.

## 8. Show Current Database

```javascript
db;
```

## 9. Create A Records Collection

MongoDB can create collections automatically when we insert data, but beginners can create one explicitly.

```javascript
db.createCollection("records");
```

Show collections:

```javascript
show collections
```

## 10. Insert One Record

```javascript
db.records.insertOne({
  title: "MongoDB first note",
  category: "database",
  status: "active",
  priority: 1,
  tags: ["mongodb", "training"],
  created_by: "student@example.com",
  created_at: new Date(),
});
```

MongoDB adds `_id` automatically if we do not provide it.

## 11. Insert Many Records

```javascript
db.records.insertMany([
  {
    title: "Learn collections",
    category: "database",
    status: "active",
    priority: 2,
    tags: ["collections"],
    created_at: new Date(),
  },
  {
    title: "Learn indexes",
    category: "performance",
    status: "draft",
    priority: 3,
    tags: ["indexes"],
    created_at: new Date(),
  },
]);
```

## 12. Find Records

Find all records:

```javascript
db.records.find();
```

Make output easier to read:

```javascript
db.records.find().pretty();
```

Find active records:

```javascript
db.records.find({ status: "active" });
```

Find one record:

```javascript
db.records.findOne({ title: "MongoDB first note" });
```

## 13. Projection In Shell

Projection means choosing which fields should be returned.

```javascript
db.records.find({ status: "active" }, { title: 1, status: 1, _id: 0 });
```

Here:

- `1` means include the field
- `0` means exclude the field

## 14. Update One Record

```javascript
db.records.updateOne(
  { title: "MongoDB first note" },
  { $set: { status: "completed" } },
);
```

## 15. Update Many Records

```javascript
db.records.updateMany({ category: "database" }, { $set: { reviewed: true } });
```

## 16. Delete One Record

```javascript
db.records.deleteOne({ title: "Learn indexes" });
```

## 17. Delete Many Records

```javascript
db.records.deleteMany({ status: "draft" });
```

## 18. Count Records

```javascript
db.records.countDocuments({ status: "active" });
```

## 19. Sort, Limit, And Skip In Shell

Sort by newest first:

```javascript
db.records.find().sort({ created_at: -1 });
```

Limit to 10 records:

```javascript
db.records.find().limit(10);
```

Skip 10 and get the next 10:

```javascript
db.records.find().sort({ created_at: -1 }).skip(10).limit(10);
```

## 20. Create An Index

Create an index on `status`:

```javascript
db.records.createIndex({ status: 1 });
```

Create a unique index on `title`:

```javascript
db.records.createIndex({ title: 1 }, { unique: true });
```

List indexes:

```javascript
db.records.getIndexes();
```

## 21. Aggregation In Shell

Count records by status:

```javascript
db.records.aggregate([
  { $group: { _id: "$status", total: { $sum: 1 } } },
  { $sort: { total: -1 } },
]);
```

## 22. Common Shell Commands

| Command                          | Purpose                  |
| -------------------------------- | ------------------------ |
| `show dbs`                       | Show databases           |
| `use training_db`                | Select database          |
| `db`                             | Show current database    |
| `show collections`               | Show collections         |
| `db.createCollection("records")` | Create collection        |
| `db.records.insertOne(...)`      | Insert one document      |
| `db.records.insertMany(...)`     | Insert many documents    |
| `db.records.find(...)`           | Find documents           |
| `db.records.findOne(...)`        | Find one document        |
| `db.records.updateOne(...)`      | Update one document      |
| `db.records.updateMany(...)`     | Update many documents    |
| `db.records.deleteOne(...)`      | Delete one document      |
| `db.records.deleteMany(...)`     | Delete many documents    |
| `db.records.countDocuments(...)` | Count matching documents |
| `db.records.createIndex(...)`    | Create an index          |
| `db.records.getIndexes()`        | List indexes             |
| `db.records.aggregate(...)`      | Run aggregation pipeline |

## 23. Quick Revision

- Atlas is MongoDB's hosted cloud platform.
- `mongosh` is MongoDB Shell.
- Use `show dbs` to list databases.
- Use `use training_db` to select a database.
- Use `db.createCollection("records")` to create a collection.
- Use `db.records.find()` to read documents from the `records` collection.
- Never commit Atlas passwords or connection strings to Git.
