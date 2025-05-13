from pydantic import BaseModel, EmailStr, constr, field_validator
from datetime import date
from enum import Enum


UsernameStr = constr(min_length=3, max_length=20)

class User_Create(BaseModel):
    username:UsernameStr 
    email: EmailStr
    

class User_Read(User_Create):
    id:int
    
    

class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in progress"
    completed = "completed"

class Task(BaseModel):
    task_id: int
    title: str
    description: str
    status: TaskStatus
    due_date: date
    user_id: int

class CreateTask(BaseModel):
    title: str
    description: str
    status: TaskStatus
    due_date: date

    @field_validator('due_date')
    @classmethod
    def validate_due_date(cls, v: date):
        if v < date.today():
            raise ValueError("Due date must be today or a future date")
        return v




