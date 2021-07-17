from fastapi import APIRouter

from app.modules.database import get_db

router = APIRouter(
    prefix='',
    tags=['base'],
    responses={404: {"description": "Not found"}},
)

@router.get('/init_db', status_code=201)
def init_and_refresh_db():
    # get_db.del_db()
    get_db.init_db()
    return {"detail": "Finish create new db"}


@router.get('/check_health', status_code=200)
def check_server_is_running():
    return {"detail": "Everything is normal"}