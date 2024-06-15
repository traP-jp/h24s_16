from fastapi import FastAPI, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Annotated, Optional
from fastapi.security.http import HTTPBase
from fastapi.openapi.models import HTTPBase as HTTPBaseModel
from starlette.requests import Request

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
def get_user() -> User:
    pass

@app.get("/users/groups")
def get_user_groups() -> list[Group]:
    pass

@app.get("/groups/{group_id}")
def get_group(group_id: str) -> Group:
    pass

@app.get("/groups/{group_id}/tasks")
def get_group_tasks(group_id: str) -> list[Task]:
    pass

@app.post("/tasks")
def create_task(new_task: CreateTaskRequest) -> Task:
    pass

@app.patch("/tasks/{task_id}")
def edit_task(task_id: str):
    pass

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    pass

@app.post("/labels")
def create_label(new_label: CreateLabelRequest) -> Label:
    pass

@app.patch("/labels/{label_id}")
def edit_label(label_id: str):
    pass

@app.delete("/labels/{label_id}")
def delete_label(label_id: str):
    pass
