from sqlalchemy import Column, String, DateTime, ForeignKey, func, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class TimestampMixin:
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

task_label_association = Table(
    "task_labels",
    Base.metadata,
    Column("task_id", String(256), ForeignKey("tasks.id"), primary_key=True),
    Column("label_id", String(256), ForeignKey("labels.id"), primary_key=True),
)

task_assignee_association = Table(
    "task_assignees",
    Base.metadata,
    Column("task_id", String(256), ForeignKey("tasks.id"), primary_key=True),
    Column("user_id", String(256), ForeignKey("users.id"), primary_key=True),
)

class Task(Base, TimestampMixin):
    __tablename__ = 'tasks'
    id = Column(String(256), primary_key=True, nullable=False)
    title = Column(String(256), nullable=False)
    content = Column(String(256), nullable=False)
    message_id = Column(String(256))
    group_id = Column(String(256), ForeignKey('groups.id'), nullable=False)
    due_date = Column(DateTime)

    group = relationship("Group", back_populates="tasks")
    assignees = relationship("User", secondary=task_assignee_association, back_populates="tasks_assigned")
    labels = relationship("Label", secondary=task_label_association, back_populates="tasks")


class Group(Base, TimestampMixin):
    __tablename__ = 'groups'
    id = Column(String(256), primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    remind_channel_id = Column(String(256))
    periodic_remind_at = Column(String(256))

    tasks = relationship("Task", back_populates="group")
    labels = relationship("Label", back_populates="group")


class User(Base, TimestampMixin):
    __tablename__ = 'users'
    id = Column(String(256), primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    remind_channel_id = Column(String(256))
    periodic_remind_at = Column(String(256))

    tasks_assigned = relationship("Task", secondary=task_assignee_association, back_populates="assignees")


class Label(Base, TimestampMixin):
    __tablename__ = 'labels'
    id = Column(String(256), primary_key=True, nullable=False)
    name = Column(String(256), nullable=False)
    group_id = Column(String(256), ForeignKey('groups.id'), nullable=False)

    group = relationship("Group", back_populates="labels")
    tasks = relationship("Task", secondary=task_label_association, back_populates="labels")
