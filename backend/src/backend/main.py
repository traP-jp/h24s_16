from fastapi import FastAPI, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Annotated, Optional
from starlette.requests import Request
from fastapi.security import APIKeyHeader

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

trao_scheme = APIKeyHeader(name="X-Forwarded-User", scheme_name="traO")

class Task(BaseModel):
    id: str
    title: str
    content: str
    message_id: str | None
    group_id: str
    due_date: datetime | None
    assigned_user_ids: list[str]

class CreateTaskRequest(BaseModel):
    title: str
    content :str
    group_id: str
    due_date: datetime | None
    assigned_user_ids: list[str]

class Label(BaseModel):
    id: str
    name: str
    group_id: str

class CreateLabelRequest(BaseModel):
    name: str
    group_id: str

class User(BaseModel):
    id: str
    remind_channel_id: str | None
    periodic_remind_at: str | None

class Group(BaseModel):
    id: str
    remind_channel_id: str | None
    periodic_remind_at: str | None
    user_ids: list[str]


@app.get("/users/me")
def get_user(user_id: Annotated[str, Depends(trao_scheme)]) -> User:
    pass

@app.get("/users/groups")
def get_user_groups(user_id: Annotated[str, Depends(trao_scheme)]) -> list[Group]:
    pass

@app.get("/groups/{group_id}")
def get_group(group_id: str, user_id: Annotated[str, Depends(trao_scheme)]) -> Group:
    pass

@app.get("/groups/{group_id}/tasks")
def get_group_tasks(group_id: str, user_id: Annotated[str, Depends(trao_scheme)]) -> list[Task]:
    pass

@app.post("/tasks")
def create_task(new_task: CreateTaskRequest, user_id: Annotated[str, Depends(trao_scheme)]) -> Task:
    pass

@app.patch("/tasks/{task_id}")
def edit_task(task_id: str, user_id: Annotated[str, Depends(trao_scheme)]):
    pass

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str, user_id: Annotated[str, Depends(trao_scheme)]):
    pass

@app.post("/labels")
def create_label(new_label: CreateLabelRequest, user_id: Annotated[str, Depends(trao_scheme)]) -> Label:
    pass

@app.patch("/labels/{label_id}")
def edit_label(label_id: str, user_id: Annotated[str, Depends(trao_scheme)]):
    pass

@app.delete("/labels/{label_id}")
def delete_label(label_id: str, user_id: Annotated[str, Depends(trao_scheme)]):
    pass
