from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    done: bool

class Task(TaskBase):
    id: int
    done: bool

    class Config:
        orm_mode = True
