from sqlalchemy.orm import Session
import tasq.repository.models as models
import tasq.repository.schemas as schemas


def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.model_dump())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def read_task(db: Session, task_id: str):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    return db_task

def read_task_by_groupid(db: Session, groupid: str):
    db_task = db.query(models.Task).filter(models.Task.group_id == groupid).all()
    return db_task

def update_task(db: Session, task_id: str, task: schemas.TaskUpdate):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        for key, value in task.model_dump(exclude_unset=True).items():
            setattr(db_task, key, value)
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: str):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    return db_task

def create_label(db: Session, label: schemas.LabelCreate):
    db_label = models.Label(**label.model_dump())
    db.add(db_label)
    db.commit()
    db.refresh(db_label)
    return db_label

def read_label(db: Session, label_id: str):
    db_label = db.query(models.Label).filter(models.Label.id == label_id).first()
    return db_label

def update_label(db: Session, label_id: str,label: schemas.LabelUpdate):
    db_label = db.query(models.Label).filter(models.Label.id == label_id).first()
    if db_label:
        for key, value in label.model_dump(exclude_unset=True).items():
            setattr(db_label, key, value)
        db.commit()
        db.refresh(db_label)
    return db_label

def delete_label(db: Session, label_id: str):
    db_label = db.query(models.Label).filter(models.Label.id == label_id).first()
    if db_label:
        db.delete(db_label)
        db.commit()
    return db_label

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.model_dump())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def read_user(db: Session, user_id: str):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    return db_user

def update_user(db: Session, user_id: str,user: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user:
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
    return db_user

def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(**group.model_dump())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def read_group(db: Session, group_id: str):
    db_group = db.query(models.Group).filter(models.Group.id == group_id).first()
    return db_group

def update_group(db: Session, group_id: str, group: schemas.GroupUpdate):
    db_group = db.query(models.Group).filter(models.Group.id == group_id).first()
    if db_group:
        for key, value in group.model_dump(exclude_unset=True).items():
            setattr(db_group, key, value)
        db.commit()
        db.refresh(db_group)
    return db_group

def create_task_assignee(db: Session, task: schemas.Task, users: list[str]):
    db_task_assignee = models.TaskAssignee(task_id=task.id, label_id=users)
    db.add(db_task_assignee)
    db.commit()
    db.refresh(db_task_assignee)
    return db_task_assignee

def read_task_assignee_from_task(db: Session, task_id: str):
    db_task_assignee = db.query(models.TaskAssignee).filter(models.TaskAssignee.id == task_id).all()
    return db_task_assignee

def read_task_assignee_from_user(db: Session, user_id: str):
    db_task_assignee = db.query(models.TaskAssignee).filter(user_id in models.TaskAssignee.user_id).all()
    return db_task_assignee

def update_task_assigee(db: Session, task: schemas.Task, users: list[str]):
    db_task_assignee = db.query(models.TaskAssignee).filter(models.TaskAssignee.task_id == task.id).first()
    if db_task_assignee:
        db_task_assignee.user_id = users
        db.commit()
        db.refresh(db_task_assignee)
    return db_task_assignee

def create_task_label(db: Session, task: schemas.Task, labels: list[str]):
    db_task_label = models.TaskLabel(task_id=task.id, label_id=labels)
    db.add(db_task_label)
    db.commit()
    db.refresh(db_task_label)
    return db_task_label

def read_task_label_from_task(db: Session, task_id: str):
    db_task_label = db.query(models.TaskLabel).filter(models.TaskLabel.task_id == task_id).first()
    return db_task_label

def read_task_label_from_label(db: Session, label_id: str):
    db_task_label = db.query(models.TaskLabel).filter(label_id in models.TaskLabel.label_id).all()
    return db_task_label

def update_task_label(db: Session, task: schemas.Task, labels: list[str]):
    db_task_label = db.query(models.TaskLabel).filter(models.TaskLabel.task_id == task.id).first()
    if db_task_label:
        db_task_label.label_id = labels
        db.commit()
        db.refresh(db_task_label)
    return db_task_label

def delete_task_label(db: Session, task: schemas.Task, labels: list[str]):
    db_task_label = db.query(models.TaskLabel).filter(models.TaskLabel.task_id == task.id).first()
    if db_task_label:
        db.delete(db_task_label)
        db.commit()
    return db_task_label
