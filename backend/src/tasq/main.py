from fastapi import FastAPI, Header, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Annotated, Optional
from starlette.requests import Request
from fastapi.security import APIKeyHeader
import tasq.repository.schemas as schemas
import tasq.repository.crud as crud
import tasq.repository.models as models
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
    return crud.read_user(db, user_id)

@app.get("/users/groups")
def get_user_groups(user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> list[GroupDetails]:
    pass

@app.get("/groups/{group_id}")
def get_group(group_id: str, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> GroupDetails:
    pass

@app.get("/groups/{group_id}/tasks")
def get_group_tasks(group_id: str, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> list[TaskDetails]:
    return crud.read_task_by_groupid(db, group_id)
    # TODO: convert list[task] -> list[task-detail]

@app.post("/tasks")
def create_task(new_task: CreateTaskReqDTO, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> TaskDetails:
    db_crud_task = schemas.TaskCreate(new_task.title, new_task.content, new_task.message_id, new_task.due_date, new_task.group_id)
    db_crud_task = crud.create_task(db, db_crud_task)
    for db_user_id in new_task.assigned_user_ids:
        if crud.read_user(db, db_user_id) is None:
            crud.create_user(db, schemas.UserCreate(db_user_id))
    crud.create_task_assignee(db, db_crud_task, new_task.assigned_user_ids)
    return TaskDetails(assigned_user_ids=new_task.assigned_user_ids, **db_crud_task)

@app.patch("/tasks/{task_id}")
def edit_task(task_id: str, new_task: UpdateTaskReqDTO, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> TaskDetails:
    db_update_task = crud.update_task(db, task_id, schemas.TaskCreate(new_task.title, new_task.content, new_task.message_id, new_task.due_date, new_task.group_id))
#    db_task_assignee = db.query(models.TaskAssignee).filter(models.TaskAssignee.task_id == task_id).first()
    crud.update_task_assigee(db, db_update_task, new_task.assigned_user_ids)
    return TaskDetails(assigned_user_ids=new_task.assigned_user_ids, **db_update_task)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)

@app.post("/labels")
def create_label(new_label: schemas.LabelCreate, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> schemas.Label:
    return crud.create_label(db, new_label)

@app.patch("/labels/{label_id}")
def edit_label(label_id: str, new_label: schemas.LabelUpdate, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> schemas.Label:
    return crud.update_label(db, label_id, new_label)

@app.delete("/labels/{label_id}")
def delete_label(label_id: str, user_id: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    return crud.delete_label(db, label_id)

