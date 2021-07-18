from fastapi import HTTPException

from app.modules.database import crud, schemas, models
from app.modules.lib import validation, hash

def get_user(uid: int = None, name: str = None, not_none=True) -> models.User:
    
    if uid is not None:
        user = crud.get_user_by_id(uid)

    if name is not None:
        user = crud.get_user_by_name(name)

    if not_none and user is None:
        raise HTTPException(404, "user not found")

    return user

def create_user(new_user: schemas.UserCreate) -> models.User:
    
    user = get_user(name=new_user.name, not_none=False)
    print(user)
    
    if user is not None:
        raise HTTPException(409, "user already exists")

    if not validation.validate_user_name(new_user.name):
        raise HTTPException(422, "username has to start with letters and contains only letters, numbers, '_' and '-' with 4 to 25 characters")

    if not validation.validate_password(new_user.password):
        raise HTTPException(422, "password has to be minimum eight characters, at least one letter and one number")

    new_user.password = hash.hash_password(new_user.password)
    new_user = crud.create_user(new_user)

    return new_user
