from app.modules.database import crud
from typing import List

from fastapi import APIRouter, Depends

from app.modules.schemas import schemas
from app.modules.core import user, auth
from app.modules.lib import core

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={
        200: {"discription": "Action success"},
        404: {"description": "Not found"},
        422: {"description": "Authentication failed"}
    }
)

@router.get("/all", response_model=List[schemas.User])
async def get_all_users(current_user: schemas.User = Depends(auth.get_current_active_user)):
    core.check_role(current_user, 'admin')
    return crud.get_all_users()

@router.get("/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(auth.get_current_active_user)):
    return current_user

@router.get('/search/{user_info}', response_model=schemas.User)
async def get_user_by_name_or_id(user_info: str, current_user: schemas.User = Depends(auth.get_current_active_user)):
    core.check_role(current_user, 'admin')
    if user_info.isnumeric():
        return user.get_user(uid=user_info)

    return user.get_user(name=user_info)