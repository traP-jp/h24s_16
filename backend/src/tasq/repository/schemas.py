from pydantic import BaseModel
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    content: str
    message_id: str | None = None
    due_date: datetime | None = None


class TaskCreate(TaskBase):
    group_id: str

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: str
    group_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class LabelBase(BaseModel):
    name: str

class LabelCreate(LabelBase):
    group_id: str
    pass

class LabelUpdate(LabelBase):
    pass

class Label(LabelBase):
    id: str
    group_id: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class UserBase(BaseModel):
    id: str
    name: str
    remind_channel_id: str | None = None
    periodic_remind_at: str | None = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class GroupBase(BaseModel):
    id: str
    name: str
    remind_channel_id: str | None
    periodic_remind_at: str | None

class GroupCreate(GroupBase):
    pass

class GroupUpdate(GroupBase):
    pass

class Group(GroupBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class TaskAssigneeBase(BaseModel):
    task_id: str
    user_id: list[str]

class TaskAssigneeCreate(TaskAssigneeBase):
    pass

class TaskAssigneeUpdate(TaskAssigneeBase):
    pass

class TaskAssignee(TaskAssigneeBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# user+group: c+r+u

class TaskLabelBase(BaseModel):
    task_id: str
    label_id: list[str]

class TaskLabelCreate(TaskLabelBase):
    pass

class TaskLabelUpdate(TaskLabelBase):
    pass

class TaskLabel(TaskLabelBase):
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
