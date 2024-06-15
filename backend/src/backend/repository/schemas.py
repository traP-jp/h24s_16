from pydantic import BaseModel


class TaskBase(BaseModel):
    title: str
    content: str
    message_id: str | None = None
    group_id: str
    due_date: str | None = None


class TaskCreate(TaskBase):
    pass


class TaskResponse(TaskBase):
    id: str
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

# Define other schemas similarly if needed
