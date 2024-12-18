from fastapi import FastAPI
from .routers import task, user
from .backend.db import engine, Base

app = FastAPI()

# Создание таблиц в базе данных и печать SQL-запросов
Base.metadata.create_all(bind=engine)

# Печать SQL-запросов
print(Base.metadata.tables)

@app.get("/")
async def read_root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router, prefix="/task", tags=["task"])
app.include_router(user.router, prefix="/user", tags=["user"])