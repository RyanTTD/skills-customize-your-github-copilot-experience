from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Student Task API")

tasks = [
    {"id": 1, "title": "Finish math worksheet", "completed": False},
    {"id": 2, "title": "Read chapter 3", "completed": True},
]


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)


class TaskUpdate(BaseModel):
    completed: bool


@app.get("/")
def root():
    return {"message": "Welcome to the Student Task API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks")
def create_task(task: TaskCreate):
    next_id = max((item["id"] for item in tasks), default=0) + 1
    new_task = {"id": next_id, "title": task.title, "completed": False}
    tasks.append(new_task)
    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, payload: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = payload.completed
            return task
    raise HTTPException(status_code=404, detail="Task not found")
