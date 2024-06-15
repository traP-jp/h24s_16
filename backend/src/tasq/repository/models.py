from sqlalchemy import Column, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TimestampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)


class Task(Base, TimestampMixin):
    __tablename__ = 'tasks'
    id = Column(String, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    message_id = Column(String)
    group_id = Column(String, ForeignKey('groups.id'), nullable=False)
    due_date = Column(DateTime)

    group = relationship("Group", back_populates="tasks")
    assignees = relationship("TaskAssignee", back_populates="task")
    labels = relationship("TaskLabel", back_populates="task")


class TaskAssignee(Base, TimestampMixin):
    __tablename__ = 'task_assignees'
    task_id = Column(String, ForeignKey('tasks.id'), primary_key=True, nullable=False)
    user_id = Column(String, ForeignKey('users.id'), primary_key=True, nullable=False)

    task = relationship("Task", back_populates="assignees")
    user = relationship("User", back_populates="tasks_assigned")


class Group(Base, TimestampMixin):
    __tablename__ = 'groups'
    id = Column(String, primary_key=True, nullable=False)
    remind_channel_id = Column(String)
    periodic_remind_at = Column(String)

    tasks = relationship("Task", back_populates="group")
    labels = relationship("Label", back_populates="group")


class User(Base, TimestampMixin):
    __tablename__ = 'users'
    id = Column(String, primary_key=True, nullable=False)
    remind_channel_id = Column(String)
    periodic_remind_at = Column(String)

    tasks_assigned = relationship("TaskAssignee", back_populates="user")


class Label(Base, TimestampMixin):
    __tablename__ = 'labels'
    id = Column(String, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    group_id = Column(String, ForeignKey('groups.id'), nullable=False)

    group = relationship("Group", back_populates="labels")
    tasks = relationship("TaskLabel", back_populates="label")


class TaskLabel(Base, TimestampMixin):
    __tablename__ = 'task_labels'
    task_id = Column(String, ForeignKey('tasks.id'), primary_key=True, nullable=False)
    label_id = Column(String, ForeignKey('labels.id'), primary_key=True, nullable=False)

    task = relationship("Task", back_populates="labels")
    label = relationship("Label", back_populates="tasks")
