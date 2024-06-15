from fastapi import FastAPI, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Annotated, Optional
from starlette.requests import Request
from fastapi.security import APIKeyHeader
import tasq.repository.schemas as schemas
import tasq.repository.crud as crud
from tasq.repository.database import get_db
from sqlalchemy.orm import Session


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

trao_scheme = APIKeyHeader(name="X-Forwarded-User", scheme_name="traO")


class GroupDetails(schemas.Group):
    user_ids: list[str]

class TaskDetails(schemas.Task):
    assigned_user_ids: list[str]

class CreateTaskReqDTO(schemas.TaskCreate):
    assigned_user_ids: list[str]

class UpdateTaskReqDTO(schemas.TaskUpdate):
    assigned_user_ids: list[str]


@app.get("/users/me")
def get_user(user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> schemas.User:
    pass

@app.get("/users/groups")
def get_user_groups(user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> list[GroupDetails]:
    pass

@app.get("/groups/{group_id}")
def get_group(group_id: str, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> GroupDetails:
    pass

@app.get("/groups/{group_id}/tasks")
def get_group_tasks(group_id: str, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> list[TaskDetails]:
    pass

@app.post("/tasks")
def create_task(new_task: CreateTaskReqDTO, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> TaskDetails:
    pass

@app.patch("/tasks/{task_id}")
def edit_task(task_id: str, new_task: UpdateTaskReqDTO, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> TaskDetails:
    pass

@app.delete("/tasks/{task_id}")
def delete_task(task_id: str, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    pass

@app.post("/labels")
def create_label(new_label: schemas.LabelCreate, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> schemas.Label:
    pass

@app.patch("/labels/{label_id}")
def edit_label(label_id: str, new_label: schemas.LabelUpdate, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> schemas.Label:
    pass

@app.delete("/labels/{label_id}")
def delete_label(label_id: str, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    pass

