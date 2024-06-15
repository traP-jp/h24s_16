from typing import Annotated

import traqapi
from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
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

traqapi_config = traqapi.Configuration(access_token="")
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
    return traq_user[0]


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
