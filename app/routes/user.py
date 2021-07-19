from fastapi import APIRouter, Depends

from app.modules.schemas import schemas
from app.modules.core import user, auth

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={
        200: {"discription": "Action success"},
        404: {"description": "Not found"},
        422: {"description": "Authentication failed"}
    }
)


@router.post('/create')
async def register(current_user: schemas.UserCreate):
    return user.create_user(current_user)

@router.get("/me", response_model=schemas.User)
async def read_users_me(current_user: schemas.User = Depends(auth.get_current_active_user)):
    return current_user

@router.get('/search/{user_info}', response_model=schemas.User)
async def get_user_by_name_or_id(user_info: str):

    if user_info.isnumeric():
        return user.get_user(uid=user_info)

    return user.get_user(name=user_info)