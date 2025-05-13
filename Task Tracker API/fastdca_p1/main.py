from schemas import Task, User_Read, User_Create, CreateTask
from models import USERS, TASKS
from fastapi import FastAPI, HTTPException

# Initialize unique ID counters
user_id = 1
task_id = 1

# Initialize FastAPI app
app = FastAPI(
    title="Task Tracker API",
    description="This app will handle task tracking"
)

# ✅ Root Endpoint - Health check
@app.get("/")
def get_root():
    return {"message": "Task Tracking App is running..."}

# 👤 Create a new user
@app.post("/users/", response_model=User_Read)
def create_user(user: User_Create):
    global user_id
    # Create new user and assign unique ID
    new_user = User_Read(id=user_id, **user.model_dump())
    USERS[user_id] = new_user
    user_id += 1
    return new_user

# 👤 Retrieve user by ID
@app.get("/users/{user_id}")
def get_users(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail=f"User id {user_id} not found")
    return user

# ✅ Create a task for a specific user
@app.post("/user/{user_id}/tasks", response_model=Task)
def create_task(user_id: int, task: CreateTask):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail=f"User id {user_id} not found in Memory")
    global task_id
    # Create task and assign to user
    new_task = Task(task_id=task_id, user_id=user_id, **task.model_dump())
    TASKS[task_id] = new_task  # 🛠️ FIXED: Save using task_id as key
    task_id += 1
    return new_task

# 📋 Retrieve a task by its ID
@app.get("/tasks/{task_id}")
def get_tasks(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task id {task_id} not found")
    return task

# 🔁 Update task status (only the status field)
@app.put("/tasks/{task_id}")
def update_status(task_id: int, status: str):
    # Validate allowed statuses
    if status.lower() not in {"pending", "completed", "in progress"}:
        raise HTTPException(status_code=400, detail=f"'{status}' is not a valid status")
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail=f"Task with task_id {task_id} not found")
    task.status = status
    return task

# 📄 List all tasks for a specific user
@app.get("/users/{user_id}/tasks")
def get_user_tasks(user_id: int):
    return [task for task in TASKS.values() if user_id == task.user_id]
