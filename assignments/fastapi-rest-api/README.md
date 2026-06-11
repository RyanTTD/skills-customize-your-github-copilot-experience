# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework in Python. You will create endpoints, validate request data, and return JSON responses for a small student task manager service.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Endpoints

#### Description
Set up a FastAPI app and implement basic endpoints so the API can be tested in a browser and with API tools.

#### Requirements
Completed program should:

- Create a FastAPI app instance.
- Add a `GET /` endpoint that returns a welcome JSON message.
- Add a `GET /health` endpoint that returns `{ "status": "ok" }`.
- Run successfully with Uvicorn.


### 🛠️ Implement Task CRUD Operations

#### Description
Add endpoints to create and retrieve tasks. Store tasks in an in-memory list of dictionaries while the app is running.

#### Requirements
Completed program should:

- Add a `GET /tasks` endpoint that returns all tasks.
- Add a `POST /tasks` endpoint that creates a new task with `id`, `title`, and `completed` fields.
- Ensure each new task gets a unique numeric `id`.
- Return the created task as JSON.


### 🛠️ Validate Data and Handle Errors

#### Description
Use Pydantic models to validate input data and return clear errors when a task is not found.

#### Requirements
Completed program should:

- Define a request model requiring `title` as a non-empty string.
- Add a `PUT /tasks/{task_id}` endpoint to update `completed` status.
- Return HTTP 404 when updating a task that does not exist.
- Keep API responses in JSON format and test each endpoint in `/docs`.
