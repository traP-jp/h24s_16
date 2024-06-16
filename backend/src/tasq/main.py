import os
from typing import Annotated

from datetime import datetime
import traqapi
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
import tasq.repository.schemas as schemas
import tasq.repository.crud as crud
import tasq.repository.models as models
from tasq.repository.database import get_db
from sqlalchemy.orm import Session
from pydantic.aliases import AliasPath
from pydantic import Field

import tasq.repository.crud as crud
import tasq.repository.schemas as schemas
from tasq.repository.database import get_db
import tasq.repository.models as models

import asyncio
from aiotraq_bot import TraqHttpBot
from aiotraq_message import TraqMessage, TraqMessageManager

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

trao_scheme = APIKeyHeader(name="X-Forwarded-User", scheme_name="traO")

traqapi_config = traqapi.Configuration(access_token=os.getenv("BOT_ACCESS_TOKEN"))
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
    traq_user = get_traq_user_from_name(username)
    if not new_task.group_id in traq_user.groups:
        raise HTTPException(status_code=404, detail="ユーザーがこのグループに所属していません")
    db_crud_task = schemas.TaskCreate(title=new_task.title, content=new_task.content, message_id=new_task.message_id, due_date=new_task.due_date, group_id=new_task.group_id)
    db_crud_task = crud.create_task(db, db_crud_task)
    for db_user_id in new_task.assigned_user_ids:
        if crud.read_user(db, db_user_id) is None:
            crud.create_user(db, schemas.UserCreate(id=db_user_id))
    crud.create_task_assignee(db, db_crud_task, new_task.assigned_user_ids)
    return TaskDetails(assigned_user_ids=new_task.assigned_user_ids, title=db_crud_task.title, content=db_crud_task.content, message_id=db_crud_task.message_id, due_date=db_crud_task.due_date, group_id=db_crud_task.group_id, id=db_crud_task.id, created_at=db_crud_task.created_at, updated_at=db_crud_task.updated_at)


@app.delete("/tasks/{task_id}")
def delete_task(task_id: str, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    traq_user = get_traq_user_from_name(username)
    db_read_task = crud.read_task(db, task_id)
    if db_read_task is None:
        raise HTTPException(status_code=404, detail="このラベルが存在しません")
    if not db_read_task.group_id in traq_user.groups:
        raise HTTPException(status_code=404, detail="ユーザーがこのグループに所属していません")
    return crud.delete_task(db, task_id)


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
    traq_user = get_traq_user_from_name(username)
    if new_label.group_id in traq_user.groups:
        return crud.create_label(db, new_label)
    else:
        raise HTTPException(status_code=404, detail="ユーザーがこのグループに所属していません")


@app.patch("/labels/{label_id}")
def edit_label(label_id: str, new_label: schemas.LabelUpdate, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> schemas.Label:
    traq_user = get_traq_user_from_name(username)
    db_read_label = crud.read_label(db, label_id)
    if db_read_label is None:
        raise HTTPException(status_code=404, detail="このラベルが存在しません")
    if not db_read_label.group_id in traq_user.groups:
        raise HTTPException(status_code=404, detail="ユーザーがこのグループに所属していません")
    return crud.update_label(db, label_id, new_label)


@app.delete("/labels/{label_id}")
def delete_label(label_id: str, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    traq_user = get_traq_user_from_name(username)
    db_read_label = crud.read_label(db, label_id)
    if db_read_label is None:
        raise HTTPException(status_code=404, detail="このラベルが存在しません")
    if not db_read_label.group_id in traq_user.groups:
        raise HTTPException(status_code=404, detail="ユーザーがこのグループに所属していません")
    return crud.delete_label(db, label_id)

@app.on_event("startup")
def startup_process():
    scheduler = BackgroundScheduler()
    scheduler.add_job(remind_user, "interval", second=60)
    scheduler.add_job(remind_group, "interval", second=60)
    scheduler.start()


base_url = "https://q.trap.jp/api/v3"
bot_verification_token = os.getenv("BOT_VERIFICATION_TOKEN", "")
bot_access_token = os.getenv("BOT_ACCESS_TOKEN", "")

bot = TraqHttpBot(verification_token=bot_verification_token)
response = TraqMessageManager(bot, bot_access_token, base_url=base_url, base_client_url="https://q.trap.jp")

async def component(am: TraqMessage, payload:str):
    am.write(payload)

async def send_message_user(message: str, user_id: str):
    await response(component,user_id=user_id,payload=message)

def remind_user():
    now = datetime.now()
    db = next(get_db())
    users_to_remind = db.query(models.User).filter(models.User.periodic_remind_at == f"{now.hour}:{now.minute}").all()
    for user in users_to_remind:
        tasks = db.query(models.Task).filter(models.Task.assignees.any(user))
        remind_channel_id = user.remind_channel_id
        name = user.name
        message = f"""@{user.name}
|名前|期日|
|----|----|
"""
        for task in tasks:
            message += f"""|{task.title}|{task.strftime('%m月%d年 %H時%M分')}
"""
        # TODO: メッセージ送ってほしい
        send_message_user(message=message, user_id=remind_channel_id)
    db.close()

async def send_message_group(message: str,group_id: str):
    await response(component,group_id=group_id,payload=message)

def remind_group():
    now = datetime.now()
    db = next(get_db())
    groups_to_remind = db.query(models.Group).filter(models.Group.periodic_remind_at == f"{now.hour}:{now.minute}").all()
    for group in groups_to_remind:
        tasks = db.query(models.Group).filter(models.Group.periodic_remind_at == f"{now.hour}:{now.minute}").all()
        remind_channel_id = group.remind_channel_id
        name = group.name
        message = f"""
|名前|期日|
|----|----|
"""
        for task in tasks:
            message += f"""|{task.title}|{task.strftime('%m月%d年 %H時%M分')}
"""
        # TODO: メッセージ送ってほしい
        send_message_group(message=message, group_id=remind_channel_id)
    db.close()
