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

@router.get('/{user_id}', response_model=schemas.User)
async def get_user_by_id(user_id: int):
    return auth.get_user(uid=user_id)