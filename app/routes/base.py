from fastapi import APIRouter

from app.modules.database import get_db

router = APIRouter(
    prefix='',
    tags=['base'],
    responses={
        404: {"description": "Not found"}
    },
)

@router.get('/init_db', status_code=201)
def init_and_refresh_db():
    get_db.del_db()
    get_db.init_db()
    return {"detail": "Finish create new db"}


@router.get('/check_health', status_code=200)
def check_server_is_running():
    return {"detail": "Everything is normal"}

from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.modules.core import auth

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(form_data.username, form_data.password)
    return user