from fastapi import FastAPI
from .routers import task, user

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to Taskmanager"}

app.include_router(task.router, prefix="/task", tags=["task"])
app.include_router(user.router, prefix="/user", tags=["user"])