from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    content: str
    message_id: str | None = None
    due_date: str | None = None


class TaskCreate(TaskBase):
    group_id: str

class TaskUpdate(TaskBase):
    pass

class Task(TaskBase):
    id: str
    group_id: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

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
    created_at: str
    updated_at: str

class UserBase(BaseModel):
    id: str
    remind_channel_id: str
    periodic_remind_at: str

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    created_at: str
    updated_at: str

class GroupBase(BaseModel):
    id: str
    remind_channel_id: str
    periodic_remind_at: str

class GroupCreate(GroupBase):
    pass

class GroupUpdate(GroupBase):
    pass

class Group(GroupBase):
    created_at: str
    updated_at: str

class TaskAssigneeBase(BaseModel):
    task_id: str
    user_id: list[str]

class TaskAssigneeCreate(TaskAssigneeBase):
    pass

class TaskAssigneeUpdate(TaskAssigneeBase):
    pass

class TaskAssignee(TaskAssigneeBase):
    created_at: str
    updated_at: str

# user+group: c+r+u

class TaskLabelBase(BaseModel):
    task_id: str
    label_id: list[str]

class TaskLabelCreate(TaskLabelBase):
    pass

class TaskLabelUpdate(TaskLabelBase):
    pass

class TaskLabel(TaskLabelBase):
    created_at: str
    updated_at: str
