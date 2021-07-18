from fastapi import APIRouter

from app.modules.core import auth
from app.modules.database import schemas

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={
        404: {"description": "Not found"},
        409: {"description": "Input conflict with server"},
        422: {"description": "Validaiton failed"}
    }
)

@router.post('/register')
async def register(user: schemas.UserCreate):
    return auth.create_user(user)