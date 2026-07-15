from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("/", response_model=list[schemas.TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


@router.get("/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada",
        )

    return task


@router.post(
    "/",
    response_model=schemas.TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task_data: schemas.TaskCreate,
    db: Session = Depends(get_db),
):
    task = models.Task(
        title=task_data.title,
        description=task_data.description,
        completed=task_data.completed,
    )

    db.add(task)
    db.commit()
    db.refresh(task)

    return task


@router.put("/{task_id}", response_model=schemas.TaskResponse)
def update_task(
    task_id: int,
    task_data: schemas.TaskCreate,
    db: Session = Depends(get_db),
):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada",
        )

    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed

    db.commit()
    db.refresh(task)

    return task


@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()

    if task is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarefa não encontrada",
        )

    db.delete(task)
    db.commit()

    return {"message": "Tarefa excluída com sucesso"}