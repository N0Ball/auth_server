from fastapi import APIRouter, Depends

from app import logger
from app.modules.schemas import schemas
from app.modules.core import auth, description
from app.modules.lib import core

router = APIRouter(
    prefix='/description',
    tags=['user'],
    responses={
        404: {"description": "Not found"},
    }
)

@router.post("/create", response_model=schemas.UserInfoDescription)
def create_description(new_description: schemas.UserInfoDescriptionCreate, current_user: schemas.User = Depends(auth.get_current_active_user)):
    core.check_role(current_user, 'admin')
    return description.create_description(new_description)

@router.get("/{name}", response_model=schemas.UserInfoDescription)
def get_descriptions_by_name(name: str, current_user: schemas.User = Depends(auth.get_current_active_user)):
    core.check_role(current_user, 'admin')
    return description.get_description_by_name(name)