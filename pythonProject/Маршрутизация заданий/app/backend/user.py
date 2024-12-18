from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from .db_depends import get_db
from typing import List
from .models import User, Task
from .schemas import CreateUser, UpdateUser
from sqlalchemy import select, delete
from slugify import slugify

router = APIRouter()

@router.get("/", response_model=List[User])
async def all_users(db: Session = Depends(get_db)):
    users = db.execute(select(User)).scalars().all()
    return users

@router.get("/{user_id}", response_model=User)
async def user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user

@router.get("/{user_id}/tasks", response_model=List[Task])
async def tasks_by_user_id(user_id: int, db: Session = Depends(get_db)):
    tasks = db.execute(select(Task).where(Task.user_id == user_id)).scalars().all()
    return tasks

@router.delete("/delete/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.delete(db_user)
    db.commit()