from fastapi import APIRouter

router = APIRouter(
    prefix='',
    tags=['base'],
    responses={404: {"description": "Not found"}},
)

@router.get('/check_health', status_code=200)
def check_server_is_running():
    return {"detail": "Everything is normal"}