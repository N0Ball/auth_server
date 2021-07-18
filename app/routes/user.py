from fastapi import APIRouter

from app.modules.database import schemas
from app.modules.core import auth

router = APIRouter(
    prefix='/user',
    tags=['user'],
    responses={
        200: {"discription": "Action success"},
        404: {"description": "Not found"}
    }
)

@router.get('/{user_info}', response_model=schemas.User)
async def get_user_by_name_or_id(user_info: str):

    if user_info.isnumeric():
        return auth.get_user(uid=user_info)

    return auth.get_user(name=user_info)
    