from typing import Annotated

import traqapi
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
import tasq.repository.schemas as schemas
import tasq.repository.crud as crud
import tasq.repository.models as models
from tasq.repository.database import get_db
from sqlalchemy.orm import Session

import tasq.repository.crud as crud
import tasq.repository.schemas as schemas
from tasq.repository.database import get_db

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

trao_scheme = APIKeyHeader(name="X-Forwarded-User", scheme_name="traO")

traqapi_config = traqapi.Configuration(access_token="Uc5ZrONZChvN8myK1jaiXYkNEtxvES70MVHt")
traqapi_config.verify_ssl = False
traqapi_client = traqapi.ApiClient(configuration=traqapi_config)
traqUserApi = traqapi.UserApi(api_client=traqapi_client)
traqGroupApi = traqapi.GroupApi(api_client=traqapi_client)


class GroupDetails(schemas.Group):
    user_ids: list[str]


class TaskDetails(schemas.Task):
    assigned_user_ids: list[str]


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
        group = crud.create_group(db, schemas.GroupCreate(id=group_id, remind_channel_id=None, periodic_remind_at=None))
    return GroupDetails(user_ids=map(lambda x: x.id, traq_group.members), **group)


@app.get("/groups/{group_id}/tasks")
def get_group_tasks(group_id: str, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> list[TaskDetails]:
    return crud.read_task_by_groupid(db, group_id)
    # TODO: convert list[task] -> list[task-detail]


@app.post("/tasks")
def create_task(new_task: CreateTaskReqDTO, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> TaskDetails:
    traq_user = get_traq_user_from_name(username)
    db_crud_task = schemas.TaskCreate(title=new_task.title, content=new_task.content, message_id=new_task.message_id, due_date=new_task.due_date, group_id=new_task.group_id)
    db_crud_task = crud.create_task(db, db_crud_task)
    for db_user_id in new_task.assigned_user_ids:
        if crud.read_user(db, db_user_id) is None:
            crud.create_user(db, schemas.UserCreate(id=db_user_id))
    crud.create_task_assignee(db, db_crud_task, new_task.assigned_user_ids)
    return TaskDetails(assigned_user_ids=new_task.assigned_user_ids, title=db_crud_task.title, content=db_crud_task.content, message_id=db_crud_task.message_id, due_date=db_crud_task.due_date, group_id=db_crud_task.group_id, id=db_crud_task.id, created_at=db_crud_task.created_at, updated_at=db_crud_task.updated_at)


@app.patch("/tasks/{task_id}")
def edit_task(task_id: str, new_task: UpdateTaskReqDTO, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)) -> TaskDetails:
    traq_user = get_traq_user_from_name(username)
    db_update_task = crud.update_task(db, task_id, schemas.TaskCreate(new_task.title, new_task.content, new_task.message_id, new_task.due_date, new_task.group_id))
#    db_task_assignee = db.query(models.TaskAssignee).filter(models.TaskAssignee.task_id == task_id).first()
    crud.update_task_assigee(db, db_update_task, new_task.assigned_user_ids)
    return TaskDetails(assigned_user_ids=new_task.assigned_user_ids, **db_update_task)



@app.delete("/tasks/{task_id}")
def delete_task(task_id: str, username: Annotated[str, Depends(trao_scheme)], db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)


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