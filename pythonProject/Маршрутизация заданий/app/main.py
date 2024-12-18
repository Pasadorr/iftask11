from fastapi import FastAPI
from backend.user import router as user_router
from backend.task import router as task_router
from backend.db import Base, engine

app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Подключаем маршруты
app.include_router(user_router, prefix="/users")
app.include_router(task_router, prefix="/tasks")