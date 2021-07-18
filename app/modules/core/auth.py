from fastapi import HTTPException

from app.modules.database import crud, schemas, models

def get_user(uid: int = None, name: int = None) -> models.User:
    
    if uid is not None:
        user = crud.get_user_by_id(uid)

    if name is not None:
        user = crud.get_user_by_name(name)

    if user is None:
        raise HTTPException(404, "user not found")

    return user


def create_user(new_user = schemas.UserCreate) -> models.User:
    
    user = get_user(name=new_user.name)
    
    if user is not None:
        pass