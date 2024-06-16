from typing import Annotated

from datetime import datetime
import traqapi
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from sqlalchemy.orm import Session
from pydantic.aliases import AliasPath
from pydantic import Field

import tasq.repository.crud as crud
import tasq.repository.schemas as schemas
from tasq.repository.database import get_db
import tasq.repository.models as models

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

trao_scheme = APIKeyHeader(name="X-Forwarded-User", scheme_name="traO")

traqapi_config = traqapi.Configuration(access_token="LnlK5MtZ0ebySrTm0EKtHsApBlsyg2rP8cOh")
traqapi_config.verify_ssl = False
traqapi_client = traqapi.ApiClient(configuration=traqapi_config)
traqUserApi = traqapi.UserApi(api_client=traqapi_client)
traqGroupApi = traqapi.GroupApi(api_client=traqapi_client)


class GroupDetails(schemas.Group):
    user_ids: list[str]


class TaskDetails(schemas.Task):
    labels: list[schemas.Label]
    assigned_users: list[schemas.User] = Field(validation_alias="assignees")


class CreateTaskReqDTO(schemas.TaskCreate):
    assigned_user_ids: list[str]


class UpdateTaskReqDTO(schemas.TaskUpdate):
    assigned_user_ids: list[str]


def get_traq_user_from_name(name: str):
    traq_user = traqUserApi.get_users(name=name)
    if len(traq_user) != 1:
        raise HTTPException(status_code=404, detail="ユーザーが存在しません")
    user_id = traq_user[0].id
    traq_user = traqUserApi.get_user(user_id=user_id)
    return traq_user

def get_or_create_user(db: Session, user_id: str):
    db_user = crud.read_user(db, user_id)
    if not db_user:
        traq_user = traqUserApi.get_user(user_id)
        if not traq_user:
            raise HTTPException(status_code=404, detail="ユーザーが存在しません")
        db_user = crud.create_user(db, models.UserCreate(id=user_id, remind_channel_id=None, periodic_remind_at=None))
        db.add(db_user)
    return db_user

@app.get("/users/me")
def get_user(username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> schemas.User:
    traq_user = get_traq_user_from_name(username)

    user = crud.read_user(db, traq_user.id)
    if not user:
        return crud.create_user(db, schemas.UserCreate(
            id=traq_user.id,
            remind_channel_id=None,
            periodic_remind_at=None
        ))
    return user


@app.get("/users/groups")
def get_user_groups(username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> list[schemas.Group]:
    traq_user = get_traq_user_from_name(username)

    groups = []
    for group_id in traq_user.groups:
        group = crud.read_group(db, group_id)
        if not group:
            groups.append(crud.create_group(db, schemas.GroupCreate(id=group_id, remind_channel_id=None, periodic_remind_at=None)))
        else:
            groups.append(group)
    return groups


@app.get("/groups/{group_id}")
def get_group(group_id: str, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> GroupDetails:
    traq_user = get_traq_user_from_name(username)

    group = crud.read_group(db, group_id)
    traq_group = traqGroupApi.get_user_group(group_id=group_id)
    if not group:
        group = crud.create_group(db, schemas.GroupCreate(id=group_id, remind_channel_id = None, periodic_remind_at = None))
    return GroupDetails(user_ids=map(lambda x: x.id, traq_group.members), **group.__dict__)


@app.get("/groups/{group_id}/tasks")
def get_group_tasks(group_id: str, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> list[TaskDetails]:
    traq_user = get_traq_user_from_name(username)

    db_tasks = db.query(models.Task).filter(models.Task.group_id == group_id).all()
    tasks = []
    for task in db_tasks:
        labels = task.labels
        tasks.append(TaskDetails.model_validate(task))
    return tasks


@app.post("/tasks")
def create_task(new_task: CreateTaskReqDTO, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> TaskDetails:
    pass


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    pass

@app.patch("/tasks/{task_id}/title")
def patch_task_title(task_id: str, title: str, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    traq_user = get_traq_user_from_name(username)
    task = crud.read_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404)
    if not task.group_id in traq_user.groups:
        raise HTTPException(status_code=401)
    task.title = title
    db.commit()
    db.refresh(task)

@app.patch("/tasks/{task_id}/content")
def patch_task_content(task_id: str, content: str, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    traq_user = get_traq_user_from_name(username)
    task = crud.read_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404)
    if not task.group_id in traq_user.groups:
        raise HTTPException(status_code=401)
    task.content = content
    db.commit()
    db.refresh(task)

@app.patch("/tasks/{task_id}/due_date")
def patch_task_due_date(task_id: str, due_date: datetime, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    traq_user = get_traq_user_from_name(username)
    task = crud.read_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404)
    if not task.group_id in traq_user.groups:
        raise HTTPException(status_code=401)
    task.due_date = due_date
    db.commit()
    db.refresh(task)

@app.patch("/tasks/{task_id}/assignees")
def put_task_assignee(task_id: str, user_ids: list[str], username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    traq_user = get_traq_user_from_name(username)
    task = crud.read_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404)
    if not task.group_id in traq_user.groups:
        raise HTTPException(status_code=401)
    group = traqGroupApi.get_user_group_members(group_id=task.group.id)
    task.assignees = []
    for user_id in user_ids:
        if all([x.id != user_id for x in group]):
            raise HTTPException(status_code=400, detail="ユーザーは該当タスクのグループのメンバーではありません")
        task.assignees.append(get_or_create_user(db, user_id))
    db.commit()
    db.refresh(task)

@app.patch("/tasks/{task_id}/labels")
def put_task_assignee(task_id: str, label_ids: list[str], username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    traq_user = get_traq_user_from_name(username)
    task = crud.read_task(db, task_id)
    if not task:
        raise HTTPException(status_code=404)
    if not task.group_id in traq_user.groups:
        raise HTTPException(status_code=401)
    task.labels = []
    for label_id in label_ids:
        db_label = crud.read_label(db, label_id)
        if not db_label:
            raise HTTPException(status_code=404, detail="ラベルが存在しません")
        task.labels.append(db_label)
    db.commit()
    db.refresh(task)


@app.post("/labels")
def create_label(new_label: schemas.LabelCreate, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> schemas.Label:
    pass


@app.patch("/labels/{label_id}")
def edit_label(label_id: str, new_label: schemas.LabelUpdate, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> schemas.Label:
    pass


@app.delete("/labels/{label_id}")
def delete_label(label_id: str, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    pass
