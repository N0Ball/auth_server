from typing import List

from app.modules.schemas import schemas
from . import get_db, models

db = get_db()

def create_user(user: schemas.UserCreate) -> models.User:
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_user_by_id(id: int) -> models.User:
    return db.query(models.User).filter(models.User.uid == id).first()

def get_user_by_name(name: str) -> models.User:
    return db.query(models.User).filter(models.User.name == name).first()

def get_all_users() -> List[models.User]:
    return db.query(models.User).all()

def create_descriptions(description: schemas.UserInfoDescriptionCreate) -> bool:
    new_description = models.UserInfoDescription(**description.dict())
    db.add(new_description)
    db.commit()
    db.refresh(new_description)
    return new_description

def get_description(id: int = None, name: str = None) -> models.UserInfoDescription:

    model = models.UserInfoDescription

    if id is not None:
        description = db.query(model).filter(model.id == id).first()
    
    if name is not None:
        description = db.query(model).filter(model.name == name).first()

    return description
