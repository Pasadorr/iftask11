from fastapi import FastAPI

app = FastAPI()

from .routers import task, user

app.include_router(task.router)
app.include_router(user.router)