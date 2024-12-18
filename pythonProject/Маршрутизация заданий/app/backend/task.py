from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .db_depends import get_db
from typing import List
from .models import Task, User
from .schemas import CreateTask, TaskBase
from sqlalchemy import select
from slugify import slugify

router = APIRouter()


@router.get("/", response_model=List[TaskBase])
async def all_tasks(db: Session = Depends(get_db)):
    tasks = db.execute(select(Task)).scalars().all()
    return tasks


@router.get("/{task_id}", response_model=TaskBase)
async def task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def create_task(task: CreateTask, user_id: int, db: Session = Depends(get_db)):
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db_task = Task(**task.dict(), user_id=user_id, slug=slugify(task.title))
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{task_id}", status_code=status.HTTP_200_OK)
async def update_task(task_id: int, task: CreateTask, db: Session = Depends(get_db)):
    db_task = db.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    for key, value in task.dict().items():
        setattr(db_task, key, value)

    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task update is successful!"}


@router.delete("/delete/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.execute(select(Task).where(Task.id == task_id)).scalar_one_or_none()
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.delete(db_task)
    db.commit()