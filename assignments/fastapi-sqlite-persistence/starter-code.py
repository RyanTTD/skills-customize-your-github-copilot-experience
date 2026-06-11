import sqlite3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Task API with SQLite")
DB_PATH = "tasks.db"


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)


class TaskUpdate(BaseModel):
    completed: bool


def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db() -> None:
    with get_connection() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                completed INTEGER NOT NULL DEFAULT 0
            )
            """
        )


@app.on_event("startup")
def startup_event() -> None:
    init_db()


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok"}


@app.get("/tasks")
def list_tasks() -> list[dict]:
    with get_connection() as conn:
        rows = conn.execute("SELECT id, title, completed FROM tasks ORDER BY id").fetchall()

    return [
        {"id": row["id"], "title": row["title"], "completed": bool(row["completed"])}
        for row in rows
    ]


@app.post("/tasks")
def create_task(task: TaskCreate) -> dict:
    with get_connection() as conn:
        cursor = conn.execute(
            "INSERT INTO tasks (title, completed) VALUES (?, ?)",
            (task.title, 0),
        )
        task_id = cursor.lastrowid

    return {"id": task_id, "title": task.title, "completed": False}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, payload: TaskUpdate) -> dict:
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE tasks SET completed = ? WHERE id = ?",
            (1 if payload.completed else 0, task_id),
        )

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Task not found")

        row = conn.execute(
            "SELECT id, title, completed FROM tasks WHERE id = ?",
            (task_id,),
        ).fetchone()

    return {
        "id": row["id"],
        "title": row["title"],
        "completed": bool(row["completed"]),
    }
