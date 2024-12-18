from fastapi import FastAPI
from .user import router as user_router
from .db import Base, engine

app = FastAPI()

# Создание таблиц
Base.metadata.create_all(bind=engine)

# Подключаем маршруты
app.include_router(user_router, prefix="/users")