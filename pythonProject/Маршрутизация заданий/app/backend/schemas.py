from pydantic import BaseModel

class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

class CreateTask(BaseModel):
    title: str
    content: str
    priority: int

class TaskBase(BaseModel):
    id: int
    title: str
    content: str
    priority: int
    user_id: int
    completed: bool
    slug: str

    class Config:
        orm_mode = True