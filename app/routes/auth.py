from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.modules.core import auth, user
from app.modules.schemas import token
from app.modules.schemas import schemas

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={
        404: {"description": "Not found"},
        409: {"description": "Input conflict with server"},
        422: {"description": "Validaiton failed"}
    }
)

@router.post("/token", response_model=token.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return auth.authenticate_user(form_data.username, form_data.password)