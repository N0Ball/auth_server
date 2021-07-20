import json
from json.decoder import JSONDecodeError

from fastapi import HTTPException

from app import logger
from app.modules.schemas import schemas

def get_role(role_string: str) -> list:

    try:
        current_role: list = json.loads(role_string)
    except JSONDecodeError as e:
        logger.error(f'decode user role fails: {e}')        
        
    return json.dumps(current_role)

def check_role(user: schemas.User, role: str) -> bool:

    if not role in get_role(user.roles):
        raise HTTPException(403, "Operation is forbidden")

    return True