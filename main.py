from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(
    title="Task API",
    description="API para gerenciamento de tarefas",
    version="1.0.0",
)


class TaskCreate(BaseModel):
    title: str
    description: str
    completed: bool = False


tasks = []
next_id = 1


@app.get("/")
def home():
    return {"message": "Task API funcionando"}


@app.get("/tasks")
def list_tasks():
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada",
    )


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    global next_id

    new_task = {
        "id": next_id,
        "title": task.title,
        "description": task.description,
        "completed": task.completed,
    }

    tasks.append(new_task)
    next_id += 1

    return new_task


@app.put("/tasks/{task_id}")
def update_task(task_id: int, updated_task: TaskCreate):
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = updated_task.title
            task["description"] = updated_task.description
            task["completed"] = updated_task.completed
            return task

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada",
    )


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return {"message": "Tarefa excluída com sucesso"}

    raise HTTPException(
        status_code=404,
        detail="Tarefa não encontrada",
    )