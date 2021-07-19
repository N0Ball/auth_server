from app.modules.lib.core import get_role
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.modules.core import auth, user
from app.modules.schemas import token
from app.modules.schemas import schemas

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
    responses={
        403: {"description": "Operation is forbidden"},
        404: {"description": "Not found"},
        409: {"description": "Input conflict with server"},
        422: {"description": "Validaiton failed"}
    }
)

@router.post('/create/user')
async def register(new_user: schemas.UserCreate, current_user: schemas.User = Depends(auth.get_current_active_user)):

    if 'admin' not in get_role(current_user.roles):
        raise HTTPException(403, "Operation is forbidden")

    return user.create_user(new_user)

@router.post("/token", response_model=token.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return auth.authenticate_user(form_data.username, form_data.password)