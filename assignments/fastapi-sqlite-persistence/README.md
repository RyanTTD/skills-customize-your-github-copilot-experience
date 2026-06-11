# 📘 Assignment: Persisting FastAPI Data with SQLite

## 🎯 Objective

Learn how to store FastAPI data in a SQLite database instead of an in-memory list. You will build endpoints that create, read, and update tasks that remain available even after restarting the server.

## 📝 Tasks

### 🛠️ Set Up SQLite and Database Initialization

#### Description
Create a SQLite database file and initialize a `tasks` table when the app starts.

#### Requirements
Completed program should:

- Connect to a local SQLite database file named `tasks.db`.
- Create a `tasks` table with columns: `id`, `title`, and `completed`.
- Use `id` as an auto-incrementing primary key.
- Keep the table creation step safe to run multiple times.


### 🛠️ Store and Read Tasks from the Database

#### Description
Replace in-memory task storage with database queries for creating and listing tasks.

#### Requirements
Completed program should:

- Add a `POST /tasks` endpoint that inserts a new task row.
- Add a `GET /tasks` endpoint that returns all tasks from SQLite.
- Return task data in JSON format with `id`, `title`, and `completed` fields.
- Confirm tasks still exist after restarting the FastAPI server.


### 🛠️ Update Task Status with Error Handling

#### Description
Implement task updates and return clear HTTP errors when a task does not exist.

#### Requirements
Completed program should:

- Add a `PUT /tasks/{task_id}` endpoint that updates `completed` status.
- Return the updated task as JSON.
- Return HTTP 404 when `task_id` is not found in the database.
- Test all endpoints using FastAPI docs at `/docs`.
